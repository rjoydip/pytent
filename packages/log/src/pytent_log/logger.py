"""Logger configuration and utilities."""

import logging
import sys
from typing import Any

import structlog
from structlog.stdlib import LoggerFactory


def setup_logging(
    level: str = "INFO", json_format: bool = False, include_timestamp: bool = True
) -> None:
    """Set up structured logging configuration."""

    processors = [
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]

    if include_timestamp:
        processors.append(structlog.processors.TimeStamper(fmt="ISO"))

    if json_format:
        processors.append(structlog.processors.JSONRenderer())
    else:
        processors.append(structlog.dev.ConsoleRenderer(colors=True))

    structlog.configure(
        processors=processors,
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    # Configure standard library logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, level.upper()),
    )


def get_logger(name: str | None = None) -> structlog.stdlib.BoundLogger:
    """Get a configured logger instance."""
    return structlog.get_logger(name)


# Context manager for adding context to logs
class LogContext:
    """Context manager for adding structured context to logs."""

    def __init__(self, logger: structlog.stdlib.BoundLogger, **context: Any):
        self.logger = logger
        self.context = context
        self.bound_logger: structlog.stdlib.BoundLogger | None = None

    def __enter__(self) -> structlog.stdlib.BoundLogger:
        self.bound_logger = self.logger.bind(**self.context)
        return self.bound_logger

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
