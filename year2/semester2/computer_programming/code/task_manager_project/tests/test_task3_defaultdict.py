from collections import defaultdict
from task_manager.tasks.task3_defaultdict import build_grouped_data

def _report(title, expected, actual, ok):
    status = "PASS" if ok else "FAIL"
    print(f"\n[{status}] {title}\n  Expected: {expected}\n  Actual  : {actual}")
    assert ok, f"{title} failed. Expected={expected} Actual={actual}"

def test_build_grouped_data_type_and_keys():
    groups = build_grouped_data()
    ok = isinstance(groups, defaultdict) and set(groups.keys()) == {"fruit", "vegetable", "grain"}
    _report("Task3: type and keys", "defaultdict with fruit/vegetable/grain", f"type={type(groups)} keys={set(groups.keys())}", ok)

def test_build_grouped_data_values():
    groups = build_grouped_data()
    expected = {
        "fruit": {"apple", "banana", "orange"},
        "vegetable": {"carrot", "broccoli"},
        "grain": {"rice", "wheat"},
    }
    actual = {k: set(v) for k, v in groups.items()}
    _report("Task3: grouped values", expected, actual, actual == expected)

