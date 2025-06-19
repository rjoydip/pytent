"""Database connection management."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from urllib.parse import quote_plus

from pytent_error import DatabaseError
from pytent_log import get_logger
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

logger = get_logger(__name__)


class DatabaseManager:
    """Manages database connections and sessions."""

    def __init__(self):
        self._engine: AsyncEngine | None = None
        self._session_factory: async_sessionmaker[AsyncSession] | None = None

    def initialize(
        self,
        host: str,
        port: int,
        database: str,
        username: str,
        password: str,
        pool_size: int = 10,
        max_overflow: int = 20,
    ) -> None:
        """Initialize database connection."""
        try:
            # URL encode password to handle special characters
            encoded_password = quote_plus(password)
            database_url = f"postgresql+asyncpg://{username}:{encoded_password}@{host}:{port}/{database}"

            self._engine = create_async_engine(
                database_url,
                pool_size=pool_size,
                max_overflow=max_overflow,
                echo=False,  # Set to True for SQL logging
            )

            self._session_factory = async_sessionmaker(
                self._engine,
                class_=AsyncSession,
                expire_on_commit=False,
            )

            logger.info(
                "Database connection initialized",
                host=host,
                port=port,
                database=database,
                pool_size=pool_size,
            )

        except Exception as e:
            logger.error("Failed to initialize database", error=str(e))
            raise DatabaseError(
                "Failed to initialize database connection",
                details={"host": host, "port": port, "database": database},
            ) from e

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Get database session context manager."""
        if not self._session_factory:
            raise DatabaseError("Database not initialized")

        async with self._session_factory() as session:
            try:
                yield session
                await session.commit()
            except Exception as e:
                await session.rollback()
                logger.error("Database session error", error=str(e))
                raise DatabaseError("Database operation failed") from e

    async def close(self) -> None:
        """Close database connections."""
        if self._engine:
            await self._engine.dispose()
            logger.info("Database connections closed")


# Global database manager instance
_db_manager = DatabaseManager()


def get_db_manager() -> DatabaseManager:
    """Get the global database manager instance."""
    return _db_manager
