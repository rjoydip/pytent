from collections.abc import Generator
from contextlib import contextmanager
import sys
from typing import Any

from loguru import logger


def setup_logging(level: str = "INFO", json_format: bool = False, include_timestamp: bool = True) -> None:
    """Set up Loguru logging configuration."""
    # Remove default handler
    logger.remove()

    # Build format string
    if json_format:
        # JSON format
        format_str = "{time} | {level} | {name} | {message}"
        serialize = True
    else:
        # Console format with colors
        if include_timestamp:
            format_str = (
                "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                "<level>{level: <8}</level> | "
                "<cyan>{name}</cyan>:"
                "<cyan>{function}</cyan>:"
                "<cyan>{line}</cyan> - "
                "<level>{message}</level>"
            )
        else:
            format_str = (
                "<level>{level: <8}</level> | "
                "<cyan>{name}</cyan>:"
                "<cyan>{function}</cyan>:"
                "<cyan>{line}</cyan> - "
                "<level>{message}</level>"
            )
        serialize = False

    # Add handler with configuration
    logger.add(
        sys.stdout,
        format=format_str,
        level=level.upper(),
        colorize=not json_format,  # Only colorize for console output
        serialize=serialize,  # JSON serialization
        backtrace=True,  # Include backtrace in exceptions
        diagnose=True,  # Include variable values in exceptions
    )


def get_logger(name: str | None = None) -> Any:
    """Get a configured logger instance."""
    if name:
        return logger.bind(name=name)
    return logger


# Context manager for adding context to logs
class LogContext:
    """Context manager for adding structured context to logs."""

    def __init__(self, logger_instance: Any = None, **context: Any):
        self.logger = logger_instance or logger
        self.context = context
        self.bound_logger: Any = None

    def __enter__(self) -> Any:
        self.bound_logger = self.logger.bind(**self.context)
        return self.bound_logger

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


# Alternative: Context manager function (more Pythonic)
@contextmanager
def log_context(**context: Any) -> Generator[Any, None, None]:
    """Context manager function for adding structured context to logs."""
    bound_logger = logger.bind(**context)
    yield bound_logger
