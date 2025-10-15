"""
Task 2: Work with namedtuple.
"""
from __future__ import annotations

from collections import namedtuple
from typing import List
import logging

Book = namedtuple("Book", ["title", "author", "genre"])


def sample_books() -> List[Book]:
    """Create several Book instances for demonstration.

    Returns:
        List[Book]: List of sample books.
    """
    return [
        Book(title="The Hobbit", author="J.R.R. Tolkien", genre="Fantasy"),
        Book(title="1984", author="George Orwell", genre="Dystopian"),
        Book(title="Clean Code", author="Robert C. Martin", genre="Programming"),
    ]


def run_task2(logger_name: str = "task_manager") -> None:
    """Execute Task 2 and print book information using attributes."""
    logger = logging.getLogger(logger_name)
    books = sample_books()
    logger.info("Books count: %d", len(books))
    print("=== Task 2: namedtuple(Book) ===")
    for b in books:
        print(f"- '{b.title}' by {b.author} [{b.genre}]")
