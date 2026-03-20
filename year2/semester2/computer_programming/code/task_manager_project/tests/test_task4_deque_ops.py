from task_manager.tasks.task4_deque_operations import demo_deque_operations

def _report(title, expected, actual, ok):
    status = "PASS" if ok else "FAIL"
    print(f"\n[{status}] {title}\n  Expected: {expected}\n  Actual  : {actual}")
    assert ok, f"{title} failed. Expected={expected} Actual={actual}"

def test_demo_deque_operations_shape_and_content():
    steps = demo_deque_operations()
    exp_op, exp_state = "append(1)", [1]
    got_op, got_state = steps[0]
    ok = got_op.startswith(exp_op) and got_state == exp_state and isinstance(steps[-1][1], list)
    _report("Task4: first snapshot and list state", f"{exp_op} -> {exp_state}", f"{got_op} -> {got_state}, last_is_list={isinstance(steps[-1][1], list)}", ok)

