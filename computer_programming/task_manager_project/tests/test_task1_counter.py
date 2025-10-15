from collections import Counter
from task_manager.tasks.task1_counter import generate_random_list, top_n

def _report(title, expected, actual, ok):
    status = "PASS" if ok else "FAIL"
    print(f"\n[{status}] {title}\n  Expected: {expected}\n  Actual  : {actual}")
    assert ok, f"{title} failed. Expected={expected} Actual={actual}"

def test_generate_random_list_seed_42_fixed_sequence():
    nums = generate_random_list(size=10, min_val=0, max_val=10, seed=42)
    expected = [10, 1, 0, 4, 3, 3, 2, 1, 10, 8]
    _report("Task1: fixed sequence (seed=42, size=10, 0..10)", expected, nums, nums == expected)

def test_top_n_counts_are_correct():
    nums = [10, 1, 0, 4, 3, 3, 2, 1, 10, 8]
    c = Counter(nums)
    top = top_n(c, 3)
    exp_values = {10, 1, 3}
    exp_counts = {10: 2, 1: 2, 3: 2}
    got_values = {v for v, _ in top}
    got_counts = {v: n for v, n in top}
    ok = (got_values == exp_values) and all(got_counts[v] == exp_counts[v] for v in exp_values)
    _report("Task1: top3 most common", f"values={exp_values}, counts={exp_counts}",
            f"values={got_values}, counts={got_counts}", ok)
