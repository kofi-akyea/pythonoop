import datetime
from tasks import Task
from users import Owner


class TaskList:
    def __init__(self, owner):
        self.owner = owner  # Owner instance
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, ix):
        if 1 <= ix <= len(self.tasks):
            self.tasks.pop(ix - 1)
        else:
            print("Invalid task number.")

    def get_task(self, ix):
        return self.tasks[ix - 1]

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def view_overdue_tasks(self):
        overdue = [t for t in self.tasks
                   if not t.completed and datetime.datetime.now() > t.date_due]
        if not overdue:
            print("No overdue tasks.")
            return
        for i, task in enumerate(overdue, start=1):
            print(f"{i}. {task}")

    def list_options(self):
        print(f"\n--- {self.owner.name}'s To-Do List ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. View overdue tasks")
        print("5. Mark task completed")
        print("6. Quit")
