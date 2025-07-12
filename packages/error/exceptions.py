from typing import Any


class MyProjectError(Exception):
    """Base exception for MyProject."""

    def __init__(
        self,
        message: str,
        error_code: str | None = None,
        details: dict[str, Any] | None = None,
    ):
        super().__init__(message)
        self.message = message
        self.error_code = error_code or self.__class__.__name__
        self.details = details or {}

    def to_dict(self) -> dict[str, Any]:
        """Convert exception to dictionary representation."""
        return {
            "error_code": self.error_code,
            "message": self.message,
            "details": self.details,
        }


class ValidationError(MyProjectError):
    """Raised when data validation fails."""

    pass


class NotFoundError(MyProjectError):
    """Raised when a resource is not found."""

    pass


class DatabaseError(MyProjectError):
    """Raised when database operations fail."""

    pass
