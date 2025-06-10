"""Error handling utilities for MyProject."""

from .exceptions import (
    DatabaseError,
    MyProjectError,
    NotFoundError,
    ValidationError,
)
from .handler import ErrorHandler, handle_error

__all__ = [
    "MyProjectError",
    "ValidationError",
    "NotFoundError",
    "DatabaseError",
    "ErrorHandler",
    "handle_error",
]
