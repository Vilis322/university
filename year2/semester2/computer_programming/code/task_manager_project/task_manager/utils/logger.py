"""
Basic logger utility for the task manager.
"""
from __future__ import annotations

import logging
from logging import Logger
from typing import Optional


def get_logger(name: str = "task_manager", level: int = logging.INFO, logfile: Optional[str] = "task_manager.log") -> Logger:
    """Create or get a configured logger.

    Args:
        name: Logger name.
        level: Logging level (e.g., logging.INFO).
        logfile: Optional path to file for logging.

    Returns:
        Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(level)

    fmt = logging.Formatter("[%(levelname)s] %(asctime)s - %(name)s - %(message)s")

    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    if logfile:
        fh = logging.FileHandler(logfile)
        fh.setLevel(level)
        fh.setFormatter(fmt)
        logger.addHandler(fh)

    return logger
