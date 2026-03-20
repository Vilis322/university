"""
Task Manager CLI for Python collections tasks (will be more in the future).

Run examples:
    python -m task_manager.main task1 --size 30 --seed 42
    python -m task_manager.main task2
    python -m task_manager.main task3
    python -m task_manager.main task4
    python -m task_manager.main task5 --count 5

Tip:
    You can also use Make targets for convenience, e.g.:
        make install
        make task1 size=30 seed=42
        make task5 count=7
"""
from __future__ import annotations

import argparse
from task_manager.tasks.task1_counter import run_task1
from task_manager.tasks.task2_namedtuple import run_task2
from task_manager.tasks.task3_defaultdict import run_task3
from task_manager.tasks.task4_deque_operations import run_task4
from task_manager.tasks.task5_queue_deque import run_task5
from task_manager.utils.logger import get_logger


def build_parser() -> argparse.ArgumentParser:
    """Build the top-level argument parser.

    Returns:
        argparse.ArgumentParser: Configured parser with subcommands.
    """
    parser = argparse.ArgumentParser(
        prog="task_manager",
        description="Task Manager for Python collections demos",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Task 1: Counter with sequence analysis
    counter_cmd = subparsers.add_parser(
        "task1",
        help="Counter: analyze a random list of integers",
    )
    counter_cmd.add_argument("--size", type=int, default=20, help="List size (default: 20)")
    counter_cmd.add_argument("--min", dest="min_val", type=int, default=0, help="Min value (default: 0)")
    counter_cmd.add_argument("--max", dest="max_val", type=int, default=10, help="Max value (inclusive, default: 10)")
    counter_cmd.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility (default: 42)")

    # Task 2: namedtuple(Book)
    subparsers.add_parser("task2", help="namedtuple Book: create and print instances")

    # Task 3: defaultdict(list)
    subparsers.add_parser("task3", help="defaultdict(list): group values under keys")

    # Task 4: deque operations demo
    subparsers.add_parser("task4", help="deque operations: append/appendleft/pop/popleft demo")

    # Task 5: queue via deque (flag --count)
    queue_cmd = subparsers.add_parser("task5", help="Queue via deque: enqueue/dequeue demo")
    queue_cmd.add_argument("--count", type=int, default=5, help="How many items to enqueue (default: 5)")

    return parser


def main() -> None:
    """Entrypoint for the CLI."""
    logger = get_logger()
    parser = build_parser()
    args = parser.parse_args()

    logger.info("Command: %s", args.command)

    if args.command == "task1":
        logger.info("Params: size=%s, min=%s, max=%s, seed=%s", args.size, args.min_val, args.max_val, args.seed)
        run_task1(size=args.size, min_val=args.min_val, max_val=args.max_val, seed=args.seed, logger_name=logger.name)
    elif args.command == "task2":
        run_task2(logger_name=logger.name)
    elif args.command == "task3":
        run_task3(logger_name=logger.name)
    elif args.command == "task4":
        run_task4(logger_name=logger.name)
    elif args.command == "task5":
        logger.info("Params: count=%s", args.count)
        run_task5(count=args.count, logger_name=logger.name)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
