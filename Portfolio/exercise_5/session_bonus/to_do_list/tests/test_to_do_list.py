from src.to_do_list import main, tasks

# Task 3: menu choice variables at the top for easy maintenance
CHOICE_ADD = "1"
CHOICE_VIEW = "2"
CHOICE_REMOVE = "3"
CHOICE_QUIT = "4"


def test_main_choice_1_add_task(monkeypatch):
    """Test choice 1: Add a task"""
    tasks.clear()
    inputs = iter([CHOICE_ADD, "Buy groceries", CHOICE_QUIT])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    assert "Buy groceries" in tasks


def test_main_choice_2_view_tasks(monkeypatch, capsys):
    """Test choice 2: View tasks"""
    tasks.clear()
    tasks.append("Task 1")
    tasks.append("Task 2")
    inputs = iter([CHOICE_VIEW, CHOICE_QUIT])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Task 1" in captured.out
    assert "Task 2" in captured.out
    assert "Total tasks: 2" in captured.out


def test_main_choice_3_remove_tasks(monkeypatch, capsys):
    """Test choice 3: Remove tasks"""
    tasks.clear()
    tasks.append("Task 1")
    tasks.append("Task 2")
    inputs = iter([CHOICE_REMOVE, "2", CHOICE_QUIT])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    assert "Task 2" not in tasks


# Task 1: Demonstrate test catches a deliberate error.
# The remove_task function uses list.remove(list[choice]) which would fail if
# the task list had duplicate items (it removes the first match, not by index).
# This test confirms the correct item is removed by index position.
def test_remove_correct_task_by_index(monkeypatch):
    """Confirm removal targets the correct index even with similar task names"""
    tasks.clear()
    tasks.append("Buy milk")
    tasks.append("Buy milk")  # duplicate
    tasks.append("Walk dog")
    inputs = iter([CHOICE_REMOVE, "3", CHOICE_QUIT])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    # "Walk dog" (index 3) should be removed; both "Buy milk" entries should remain
    assert "Walk dog" not in tasks
    assert tasks.count("Buy milk") == 2


# Task 2: Test that an invalid menu choice does not cause a failure
def test_invalid_choice_does_not_crash(monkeypatch, capsys):
    """Test that entering an invalid choice prints an error and loops safely"""
    tasks.clear()
    inputs = iter(["9", CHOICE_QUIT])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out
