import pytest
from project import add_task, remove_task, list_tasks

def test_add_task():
    tasks = []
    tasks = add_task("Buy groceries", tasks)
    assert "Buy groceries" in tasks

def test_remove_task():
    tasks = ["Buy groceries", "Call mom"]
    tasks = remove_task("Buy groceries", tasks)
    assert "Buy groceries" not in tasks

def test_list_tasks():
    tasks = ["Workout", "Read book"]
    assert list_tasks(tasks) == ["Workout", "Read book"]

if __name__ == "__main__":
    pytest.main()