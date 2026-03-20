"""
Task 3: Work with defaultdict(list).
"""
from __future__ import annotations

from collections import defaultdict
from typing import DefaultDict, List, Tuple
import logging


def build_grouped_data() -> DefaultDict[str, List[str]]:
    """Build a defaultdict(list) and populate it with data.

    Returns:
        DefaultDict[str, List[str]]: Keys mapped to lists of values.
    """
    groups: DefaultDict[str, List[str]] = defaultdict(list)
    data: List[Tuple[str, str]] = [
        ("fruit", "apple"),
        ("fruit", "banana"),
        ("vegetable", "carrot"),
        ("fruit", "orange"),
        ("vegetable", "broccoli"),
        ("grain", "rice"),
        ("grain", "wheat"),
    ]
    for key, value in data:
        groups[key].append(value)
    return groups


def run_task3(logger_name: str = "task_manager") -> None:
    """Execute Task 3 and print the grouped defaultdict contents."""
    logger = logging.getLogger(logger_name)
    groups = build_grouped_data()
    logger.info("Groups: %s", {k: len(v) for k, v in groups.items()})
    print("=== Task 3: defaultdict(list) ===")
    for key, values in groups.items():
        print(f"- {key}: {values}")
