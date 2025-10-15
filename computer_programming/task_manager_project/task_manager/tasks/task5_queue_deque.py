"""
Task 5: Implement a simple FIFO queue using deque.
"""
from __future__ import annotations

from collections import deque
from typing import Deque, Optional, Any
import logging


def enqueue(queue: Deque[Any], item: Any) -> None:
    """Add an item to the end of the queue.

    Args:
        queue: The queue implemented via deque.
        item: The item to enqueue.
    """
    queue.append(item)


def dequeue(queue: Deque[Any]) -> Optional[Any]:
    """Remove and return the item from the front of the queue.

    Args:
        queue: The queue implemented via deque.

    Returns:
        Optional[Any]: The dequeued item, or None if the queue is empty.
    """
    if queue:
        return queue.popleft()
    return None


def run_task5(count: int = 5, logger_name: str = "task_manager") -> None:
    """Execute Task 5: demonstrate enqueue/dequeue on an empty queue.

    Args:
        count: How many sequential integers to enqueue (0..count-1).
        logger_name: Logger name to use.
    """
    logger = logging.getLogger(logger_name)
    q: Deque[int] = deque()
    logger.info("Queue demo start with count=%d", count)
    print("=== Task 5: queue via deque ===")
    print(f"Initial queue: {list(q)}")

    for i in range(count):
        enqueue(q, i)
        logger.debug("enqueue(%s) -> %s", i, list(q))
        print(f"enqueue({i}) -> {list(q)}")

    while True:
        item = dequeue(q)
        if item is None:
            logger.info("dequeue() -> None (empty)")
            print("dequeue() -> None (queue is empty)")
            break
        logger.debug("dequeue() -> %s, now %s", item, list(q))
        print(f"dequeue() -> {item}, queue now: {list(q)}")
