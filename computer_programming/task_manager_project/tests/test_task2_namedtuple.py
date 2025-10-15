from task_manager.tasks.task2_namedtuple import Book, sample_books

def _report(title, expected, actual, ok):
    status = "PASS" if ok else "FAIL"
    print(f"\n[{status}] {title}\n  Expected: {expected}\n  Actual  : {actual}")
    assert ok, f"{title} failed. Expected={expected} Actual={actual}"

def test_sample_books_structure_and_types():
    books = sample_books()
    ok = isinstance(books, list) and len(books) >= 3 and isinstance(books[0], Book)
    _report("Task2: structure/types", "list[Book] length>=3", f"type={type(books)} len={len(books)} first={type(books[0])}", ok)

def test_sample_books_expected_values_present():
    titles = {b.title for b in sample_books()}
    expected = {"The Hobbit", "1984", "Clean Code"}
    _report("Task2: expected titles present", expected, titles, expected.issubset(titles))
