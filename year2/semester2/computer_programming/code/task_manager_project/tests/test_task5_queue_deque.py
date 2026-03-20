from collections import deque
from task_manager.tasks.task5_queue_deque import enqueue, dequeue

def _report(title, expected, actual, ok):
    status = "PASS" if ok else "FAIL"
    print(f"\n[{status}] {title}\n  Expected: {expected}\n  Actual  : {actual}")
    assert ok, f"{title} failed. Expected={expected} Actual={actual}"

def test_enqueue_dequeue_fifo_and_empty():
    q = deque()
    seq = ["a", "b", "c"]
    for x in seq:
        enqueue(q, x)
    _report("Task5: enqueue order", seq, list(q), list(q) == seq)

    got = [dequeue(q), dequeue(q), dequeue(q), dequeue(q)]
    expected = ["a", "b", "c", None]
    _report("Task5: dequeue FIFO then None", expected, got, got == expected)

