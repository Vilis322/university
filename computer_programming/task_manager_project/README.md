# ***Task Manager — Python Collections Mini-Project***
- A small, CLI-driven project demonstrating Python’s collections module across 5 tasks:
  - Task 1: Counter — analyze a random list (top-N frequencies)
  - Task 2: namedtuple — simple Book entries 
  - Task 3: defaultdict(list) — grouping values by key
  - Task 4: deque ops — append/appendleft/pop/popleft demo
  - Task 5: Simple FIFO queue using deque 
# ***Requirements***
- Python 3.10+

# ***Project Structure***
```bash
task_manager/
├── __init__.py
├── main.py
├── tasks/
│   ├── __init__.py
│   ├── task1_counter.py
│   ├── task2_namedtuple.py
│   ├── task3_defaultdict.py
│   ├── task4_deque_ops.py
│   └── task5_queue_deque.py
├── utils/
│   └── logger.py
tests/
├── test_task1_counter.py
├── test_task2_namedtuple.py
├── test_task3_defaultdict.py
├── test_task4_deque_ops.py
└── test_task5_queue_deque.py
Makefile
pyproject.toml
requirements.txt
```
# ***Quick Start (Make)***
```bash
# 1) Create venv, install deps, and install package in editable mode
make install

# 2) Run tasks
make task1 size=30 seed=42     # others default: min=0 max=10
make task2
make task3
make task4
make task5 count=7             # enqueue from 0 to 6 then dequeue

# 3) Run tests
make test

# 4) Coverage report
make cov

# 5) Command usage
make help
```
# ***Quick start (without Make)***
```bash
# 1) Create & activate a virtual environment (macOS, Linux)
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip

# Windows (CMD) 
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip

# 2) Install dependencies and the package (editable)
python -m pip install -r requirements.txt
python -m pip install -e .

# 3) Run tasks
python -m task_manager.main task1 --size 30 --seed 42
python -m task_manager.main task2
python -m task_manager.main task3
python -m task_manager.main task4
python -m task_manager.main task5 --count 7

# 4) Run tests
python -m pytest -s -vv -rA

# 5) Coverage report 
python -m pytest -s -vv -rA --maxfail=1 --disable-warnings --cov=task_manager --cov-report=term-missing
```
