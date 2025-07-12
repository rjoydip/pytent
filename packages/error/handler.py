from collections.abc import Callable
import traceback
from typing import Any, TypeVar

from packages.log import get_logger

from .exceptions import MyProjectError

T = TypeVar("T")
logger = get_logger(__name__)


class ErrorHandler:
    """Centralized error handling."""

    def __init__(self):
        self._handlers: dict[type[Exception], Callable] = {}

    def register(self, exception_type: type[Exception]):
        """Decorator to register error handlers."""

        def decorator(handler_func: Callable):
            self._handlers[exception_type] = handler_func
            return handler_func

        return decorator

    def handle(self, error: Exception) -> dict[str, Any]:
        """Handle an exception and return error response."""
        error_type = type(error)

        # Check for specific handler
        if error_type in self._handlers:
            return self._handlers[error_type](error)

        # Check for MyProject errors
        if isinstance(error, MyProjectError):
            logger.error(
                "MyProject error occurred",
                error_code=error.error_code,
                message=error.message,
                details=error.details,
            )
            return error.to_dict()

        # Handle unexpected errors
        logger.error(
            "Unexpected error occurred",
            error_type=error_type.__name__,
            message=str(error),
            traceback=traceback.format_exc(),
        )

        return {
            "error_code": "INTERNAL_ERROR",
            "message": "An unexpected error occurred",
            "details": {},
        }


# Global error handler instance
_error_handler = ErrorHandler()


def handle_error(error: Exception) -> dict[str, Any]:
    """Handle an error using the global error handler."""
    return _error_handler.handle(error)


def error_handler(exception_type: type[Exception]):
    """Decorator to register error handlers with global handler."""
    return _error_handler.register(exception_type)
