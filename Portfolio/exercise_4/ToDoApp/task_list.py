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