# Session 4 – Classes, Objects and a Modular Programme

## Section 1: Python Classes

### Exercise 1 – Creating Classes and Initialising Objects

A **class** is a blueprint for creating objects. Objects are instances of a class. Classes are defined using the `class` keyword. Every class has a special method called `__init__`, which is the **constructor** — it runs automatically whenever a new object of the class is created.

We created a `TaskList` class with two attributes:

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

```console
Kofi
```

The `self` parameter is a reference to the current instance of the class. It is required as the first parameter of every method and is used to access the instance's own attributes and methods. Each object created from `TaskList` has its own separate `owner` and `tasks`.

We also tested that string methods such as `.upper()` can be called on an attribute directly inside `__init__`:

```python
self.owner = owner.upper()
```

---

### Exercise 2 – Adding Methods

We added three methods to the `TaskList` class to give it behaviour.

**`add_task(self, task)`** — appends a task to the `tasks` list:

```python
def add_task(self, task):
    self.tasks.append(task)
```

**`remove_task(self, index)`** — removes a task by its 1-based position. Bounds checking prevents an invalid index from crashing the programme:

```python
def remove_task(self, index):
    if 1 <= index <= len(self.tasks):
        removedTask = self.tasks.pop(index - 1)
        print(f"Task {removedTask} removed successfully!")
    else:
        print("Invalid task number. Try again")
```

`pop(index - 1)` converts the user's 1-based number to a 0-based list index before removing the element.

**`view_tasks(self)`** — prints all tasks using `enumerate` with `start=1`, or tells the user the list is empty:

```python
def view_tasks(self):
    if not self.tasks:
        print("No tasks yet. Add one!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f" {i}. {task}")
    print()
```

Using `enumerate` avoids the need for a manual counter — it gives both the position and the value in one step.

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

#### Output 1

```console
Your tasks:
 1. Do Homework
 2. Do Laundry
 3. Go Shopping

Task Do Homework removed successfully!

Your tasks:
 1. Do Laundry
 2. Go Shopping
```

This confirmed that `view_tasks` correctly numbered the list, `remove_task` removed items at valid indices and rejected invalid ones, and `add_task` appended new entries.

---

### Exercise 4 – Composition (Task class + TaskList)

**Composition** means building a class out of instances of simpler classes. Instead of storing tasks as plain strings, a separate `Task` class was introduced so that each task could carry its own data and behaviour.

The `Task` class was given:

- `title` — the name of the task
- `completed` — a boolean, defaulting to `False`
- `mark_completed()` — sets `completed` to `True`
- `change_title(new_title)` — updates the title
- `__str__()` — returns a readable string representation including the completion status

The `TaskList.add_task` method was updated to accept a `Task` object rather than a plain string. Inside the menu, a `Task` object is created from user input before being added:

```python
if choice == "1":
    title = input("Enter a task: ")
    task = Task(title)
    self.add_task(task)
```

---

## Section 2: Python Libraries – Adding Dates

### Exercise 1 – Using `datetime`

The `datetime` standard library provides tools for working with dates and times. We imported it at the top of the script and added two new attributes to `Task`:

- `date_created` — set automatically to `datetime.datetime.now()` when the task is created
- `date_due` — calculated from the current time using `timedelta(days=days_to_complete)`

```python
from datetime import datetime, timedelta

class TaskList:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

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
        print(f"\n Task '{task_name}' added successfully!")
        print(f"   Deadline: {due_on}")
```

`strftime` formats a datetime object as a string. `timedelta` represents a duration — adding it to a datetime gives the due date.

Tasks are checked against the current time when displayed. If the due date has passed, `[!] OVERDUE` is shown:

```python
def view_tasks(self):
    now = datetime.now()
    for i, task in enumerate(self.tasks, start=1):
        status = " [!] OVERDUE" if now > task["due_obj"] else ""
        print(f"{i}. {task['name']}{status}")
        print(f"   Added: {task['added']} | Due: {task['due']}")
```

#### Output 3

```console
--- KOFI'S TODO LIST ---
1. Submit assignment [!] OVERDUE
   Added: 2026-03-10 14:00 Due: 2026-03-14
2. Buy groceries
   Added: 2026-03-15 09:30 Due: 2026-03-17
------------------------------
```

A `change_date_due` method was also added to `Task` to allow the due date to be updated after creation. The menu was extended to let users change both the title and due date of an existing task.

---

## Section 3: Modularising the Code

### Exercise 1 – Restructuring into Modules

The single-file programme was split into three separate files inside a `ToDoApp/` folder to keep each class in its own module.

**`tasks.py`** — defines the `Task` class with `description`, `created_at`, and `due_date` attributes, an `is_overdue()` method, and a `__str__` method that formats output:

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

**`task_list.py`** — imports `Task` and defines `TaskManager` with methods for adding, removing, and retrieving tasks:

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

**`main.py`** — contains a `run_app()` function with the full interactive menu loop. All user interaction (input, print, menu logic) lives here, keeping `TaskManager` and `Task` responsible only for data:

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

The `if __name__ == "__main__"` guard ensures `run_app()` only runs when `main.py` is executed directly — not when it is imported as a module by another file. This is a standard Python pattern for entry points.

The separation of concerns across three files is a key OOP principle: `Task` models a single task, `TaskManager` manages the collection, and `main.py` handles all user interaction.

---

## Section 4: Type Hints and Docstrings

### Type Hints

Type hints were added to all method signatures to make the expected input and output types explicit:

```python
def add_task(self, task: Task) -> None:
    ...

def __str__(self) -> str:
    ...
```

The `->` arrow specifies the return type. `None` means the method returns nothing. Type hints do not affect how Python runs the code but help IDEs like VS Code catch type mismatches early and make the code easier to read.
