import datetime


class TaskList:
    def __init__(self, owner):
        self.owner = owner
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

    def check_task_index(self, ix):
        return 0 <= ix < len(self.tasks)

    @property
    def uncompleted_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def view_tasks(self):
        if not self.uncompleted_tasks:
            print("No tasks to do!")
            return
        print("The following tasks are still to be done:")
        for task in self.uncompleted_tasks:
            ix = self.tasks.index(task) + 1
            print(f"{ix}: {task}")

    def view_overdue_tasks(self):
        overdue = [t for t in self.uncompleted_tasks
                   if datetime.datetime.now() > t.date_due]
        if not overdue:
            print("No overdue tasks.")
            return
        print("Overdue tasks:")
        for task in overdue:
            ix = self.tasks.index(task) + 1
            print(f"{ix}: {task}")

    def list_options(self):
        print(f"\n--- {self.owner}'s To-Do List ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. View overdue tasks")
        print("5. Mark task completed")
        print("6. Load tasks from file")
        print("7. Save tasks to file")
        print("8. Quit")
