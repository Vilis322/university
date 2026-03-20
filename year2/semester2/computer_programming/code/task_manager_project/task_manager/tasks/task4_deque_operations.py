"""
Task 4: Use deque to process data with push/pop operations.
"""
from __future__ import annotations

from collections import deque
from typing import Deque, List, Tuple
import logging


def demo_deque_operations() -> List[Tuple[str, List[int]]]:
    """Demonstrate deque operations and capture the state after each step.

    Returns:
        List[Tuple[str, List[int]]]: (operation, current_state) snapshots.
    """
    dq: Deque[int] = deque()
    states: List[Tuple[str, List[int]]] = []

    dq.append(1); states.append(("append(1)", list(dq)))
    dq.append(2); states.append(("append(2)", list(dq)))
    dq.appendleft(0); states.append(("appendleft(0)", list(dq)))
    dq.pop(); states.append(("pop()", list(dq)))
    dq.popleft(); states.append(("popleft()", list(dq)))
    dq.append(3); states.append(("append(3)", list(dq)))
    dq.appendleft(-1); states.append(("appendleft(-1)", list(dq)))

    return states


def run_task4(logger_name: str = "task_manager") -> None:
    """Execute Task 4 and print the deque state after each operation."""
    logger = logging.getLogger(logger_name)
    snapshots = demo_deque_operations()
    logger.info("Deque steps: %d", len(snapshots))
    print("=== Task 4: deque operations ===")
    for op, state in snapshots:
        print(f"- after {op:>14}: {state}")
