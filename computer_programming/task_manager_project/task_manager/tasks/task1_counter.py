"""
Task 1: Analyze a random list of numbers using Counter.

- Generate a random list of integers
- Count unique elements with Counter
- Print three most common elements
"""
from __future__ import annotations

from collections import Counter
from random import randint, seed as set_seed
from typing import List, Tuple, Optional
import logging


def generate_random_list(size: int, min_val: int, max_val: int, seed: Optional[int] = None) -> List[int]:
    """Generate a list of random integers.

    Args:
        size: Number of elements to generate.
        min_val: Minimum inclusive bound for values.
        max_val: Maximum inclusive bound for values.
        seed: Optional seed for reproducibility.

    Returns:
        List[int]: List of random integers.
    """
    if seed is not None:
        set_seed(seed)
    return [randint(min_val, max_val) for _ in range(size)]


def top_n(counter: Counter[int], n: int = 3) -> List[Tuple[int, int]]:
    """Return the n most common elements.

    Args:
        counter: Counter object with frequencies.
        n: Number of top items to return.

    Returns:
        List[Tuple[int, int]]: (value, count) pairs.
    """
    return counter.most_common(n)


def run_task1(size: int = 20, min_val: int = 0, max_val: int = 10, seed: Optional[int] = 42, logger_name: str = "task_manager") -> None:
    """Execute Task 1 end-to-end and print results.

    Args:
        size: Length of the random list to generate.
        min_val: Minimum value (inclusive).
        max_val: Maximum value (inclusive).
        seed: Seed for reproducibility (default 42).
        logger_name: Logger name to use.
    """
    logger = logging.getLogger(logger_name)

    numbers = generate_random_list(size, min_val, max_val, seed=seed)
    logger.debug("Generated numbers: %s", numbers)

    frequency = Counter(numbers)
    unique_count = len(frequency)
    top_3 = top_n(frequency, 3)
    logger.info("Unique=%d, Top3=%s", unique_count, top_3)

    print("=== Task 1: Counter ===")
    print("Generated numbers:", numbers)
    print(f"Unique elements: {unique_count}")
    print("Top 3 most common (value -> count):")
    for value, count in top_3:
        print(f"  {value} -> {count}")
