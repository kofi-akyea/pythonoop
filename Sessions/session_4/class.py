class TaskList:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)

