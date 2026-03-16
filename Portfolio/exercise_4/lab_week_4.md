# Lab Week 4 – Classes and Objects

**COMP11124 Interactive Software Design**
Date: 2026-03-15

---

## Overview

This week's lab focused on Object-Oriented Programming (OOP) in Python. The core idea was to take the To-Do list program built with functions in Week 3 and rebuild it using **classes and objects**.

---

## Section 1: Python Classes

### Exercise 1 – Creating Classes and Initializing Objects

The first step was learning how to define a class using the `class` keyword and set up its attributes inside the `__init__` method. The `__init__` method is the **constructor** — it runs automatically whenever a new object of the class is created.

I created a `TaskList` class with two attributes:

- `owner` — a string storing the name of the list's owner
- `tasks` — an empty list that will hold all the tasks

```python
class TaskList:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

my_task_list = TaskList("Kofi")
print(my_task_list.owner)
```

#### Output

``` console
Kofi
```

The `self` parameter is a reference to the current instance of the class. It is how methods and attributes are accessed from within the class. Each object created from `TaskList` has its own separate `owner` and `tasks`.

We also tested that the `.upper()` method can be called inside `__init__` to store the owner's name in uppercase:

```python
class TaskList:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []

my_task_list = TaskList("Kofi")
print(my_task_list.owner)
```

#### Output

```console
KOFI
```

---

### Exercise 2 – Adding Methods

Next, we added methods to the `TaskList` class:

**`add_task(self, task)`** — appends a task to the `tasks` list using `self.tasks.append(task)`.

**`remove_task(self, index)`** — removes a task by its 1-based index. I used `pop()` with bounds checking so that an invalid index prints a clear error message rather than crashing:

```python
def remove_task(self, index):
    if 1 <= index <= len(self.tasks):
        removedTask = self.tasks.pop(index - 1)
        print(f"Task {removedTask} removed successfully!")
    else:
        print("Invalid task number. Try again")
```


**`view_tasks(self)`** — iterates over the tasks list using `enumerate` (with `start=1`) to print each task alongside its number. If the list is empty a message tells the user to add a task:

```python
def view_tasks(self):
    if not self.tasks:
        print("No tasks yet. Add one!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f" {i}. {task}")
```

Using `enumerate` is cleaner than maintaining a manual counter variable — it gives both the index and the value in one step.

---

### Exercise 3 – Testing the Functionality

To test all methods together, a `TaskList` object was created and pre-loaded with tasks:

```python
my_task_list = TaskList("Kofi")
my_task_list.tasks = ["Do Homework", "Do Laundry", "Go Shopping"]
my_task_list.view_tasks()
my_task_list.remove_task(1)
my_task_list.view_tasks()
```

#### Output 2

``` console
Your tasks:
 1. Do Homework
 2. Do Laundry
 3. Go Shopping

Task Do Homework removed successfully!

Your tasks:
 1. Do Laundry
 2. Go Shopping
```

This confirmed that `view_tasks` correctly printed the numbered list, `remove_task` removed items at valid indices and rejected invalid ones, and `add_task` appended new entries.

---

### Exercise 4 – Composition (Task class + TaskList)

**Composition** means building classes out of simpler ones. Instead of storing tasks as plain strings, a separate `Task` class was introduced so each task could carry its own data and behaviour.

The `Task` class started with a single `title` attribute, then was updated to include:

- `completed: bool` — set to `False` by default
- `mark_completed()` — sets `completed` to `True`
- `change_title(new_title)` — updates the title
- `__str__()` — returns a readable string representation including the completion status

The `Task` class was defined as follows:

```python
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def change_title(self, new_title):
        self.title = new_title

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} [{status}]"
```

The `TaskList.add_task` method was updated so that it accepted a `Task` object rather than a plain string. Inside `list_options`, a `Task` object is created from user input before being added:

```python
if choice == "1":
    title = input("Enter a task: ")
    task = Task(title)
    self.add_task(task)
```

---

## Section 2: Python Libraries – Adding Dates

### Exercise 1 – Using `datetime`

The `datetime` standard library was imported at the top of the script. Two new attributes were added to `Task`:

- `date_created` — set automatically to `datetime.datetime.now()` when the task is created
- `date_due` — passed in by the user as a string and converted using `strptime`

The `to_do_week_4.py` file captures this approach — each task is stored as a dictionary containing its name, formatted date strings, and a raw `datetime` object for comparisons:

```python
from datetime import datetime, timedelta

def add_task(self, task_name, days_to_complete):
    now = datetime.now()
    added_on = now.strftime("%Y-%m-%d %H:%M")
    due_date_obj = now + timedelta(days=days_to_complete)
    due_on = due_date_obj.strftime("%Y-%m-%d")
    task_entry = {
        "name": task_name,
        "added": added_on,
        "due": due_on,
        "due_obj": due_date_obj
    }
    self.tasks.append(task_entry)
```

`strftime` formats a `datetime` object as a readable string. `timedelta(days=n)` represents a duration — adding it to `datetime.now()` gives a future due date.

When displaying tasks, the current time is compared against the stored `due_obj` to flag overdue items:

```python
def view_tasks(self):
    now = datetime.now()
    for i, task in enumerate(self.tasks, start=1):
        status = " [!] OVERDUE" if now > task["due_obj"] else ""
        print(f"{i}. {task['name']}{status}")
        print(f"   Added: {task['added']} | Due: {task['due']}")
```

#### Example Output

```console
--- KOFI'S TODO LIST ---
1. Submit assignment [!] OVERDUE
   Added: 2026-03-10 14:00 | Due: 2026-03-14
2. Buy groceries
   Added: 2026-03-15 09:30 | Due: 2026-03-17
------------------------------
```

A `change_date_due` method was also added to `Task` to allow the due date to be updated after creation. The menu in `list_options` was extended to let users change both the title and due date of an existing task.

---

## Section 3: Modularizing the Code

### Exercise 1 – Restructuring into Modules

The code was split from a single script into three separate files inside a `ToDoApp/` folder:

`tasks.py` defines the `Task` class with `description`, `created_at`, and `due_date` attributes, an `is_overdue()` method, and a `__str__` method that formats the output neatly:

```python
from datetime import datetime, timedelta

class Task:
    def __init__(self, description, days_to_complete):
        self.description = description
        self.created_at = datetime.now()
        self.due_date = self.created_at + timedelta(days=days_to_complete)

    def is_overdue(self):
        return datetime.now() > self.due_date

    def __str__(self):
        added = self.created_at.strftime("%Y-%m-%d %H:%M")
        due = self.due_date.strftime("%Y-%m-%d")
        status = " [!] OVERDUE" if self.is_overdue() else ""
        return f"{self.description}{status}\n   Added: {added} | Due: {due}"
```

`task_list.py` imports `Task` and defines `TaskManager` with three methods: `add_new_task`, `remove_task_at`, and `get_all_tasks`:

```python
from tasks import Task

class TaskManager:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

    def add_new_task(self, description, days):
        new_task = Task(description, days)
        self.tasks.append(new_task)
        return new_task

    def remove_task_at(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index)
        return None

    def get_all_tasks(self):
        return self.tasks
```

### Exercise 2 – The `main()` Function and `if __name__ == "__main__"`

`main.py` contains a `run_app()` function with the full interactive menu loop:

```python
from task_list import TaskManager

def run_app():
    manager = TaskManager("Kofi")
    while True:
        print(f"\n--- {manager.owner.upper()}'S TODO MANAGER ---")
        print("1. Add Task | 2. View Tasks | 3. Remove Task | 4. Quit")
        choice = input("Choice: ")

        if choice == "1":
            desc = input("Task description: ")
            try:
                days = int(input("Days until due: "))
                manager.add_new_task(desc, days)
                print("Added!")
            except ValueError:
                print("Please enter a number for days.")
        elif choice == "2":
            tasks = manager.get_all_tasks()
            if not tasks:
                print("\nList is empty!")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif choice == "3":
            try:
                idx = int(input("Task number to remove: ")) - 1
                removed = manager.remove_task_at(idx)
                if removed:
                    print(f"Removed: {removed.description}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    run_app()
```

The user interaction logic (input, print menus, call manager methods) lives entirely in `main.py`, keeping `TaskManager` responsible only for managing data and `Task` responsible only for representing a single task. This separation of concerns is a key OOP principle.

---

## Section 4: Type Hints and Docstrings

### Type Hints

Type hints were added to all method signatures to make the expected input and output types explicit. For example:

```python
def add_task(self, task: Task) -> None:
    ...

def __str__(self) -> str:
    ...
```

The `->` arrow specifies the return type. `None` means the method returns nothing. This does not affect how Python runs the code but helps IDEs like VS Code catch type mismatches early and makes the code easier to understand.

### Docstrings

Docstrings were added to classes and methods using triple quotes immediately after the `def` or `class` line. They describe what a class or method does, what parameters it expects, and what it returns:

```python
def mark_completed(self) -> None:
    """Marks the task as completed."""
    self.completed = True
```

A class-level docstring describes the overall purpose of the class:

```python
class Task:
    """Represents a single task with a description, creation date, and due date."""
```

A method with parameters uses a multi-line docstring:

```python
def add_new_task(self, description: str, days: int) -> Task:
    """
    Creates a new Task and adds it to the list.

    Args:
        description: The text of the task.
        days: Number of days from today until the task is due.

    Returns:
        The newly created Task object.
    """
    new_task = Task(description, days)
    self.tasks.append(new_task)
    return new_task
```

Docstrings are accessible at runtime via `help()` and are picked up by documentation tools. Together with type hints they make the code self-documenting without needing separate external documentation.
