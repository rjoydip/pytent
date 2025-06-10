"""Database session utilities."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession

from .connection import get_db_manager


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Get database session - convenience wrapper."""
    db_manager = get_db_manager()
    async with db_manager.get_session() as session:
        yield session
