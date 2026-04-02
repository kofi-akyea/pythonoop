from task_list import TaskList
from task_factory import TaskFactory


class TaskManagerController:
    def __init__(self, owner):
        self.task_list = TaskList(owner)

    def add_task(self, title, date_due, **kwargs):
        task = TaskFactory.create_task(title, date_due, **kwargs)
        self.task_list.add_task(task)

    def remove_task(self, ix):
        self.task_list.remove_task(ix)

    def complete_task(self, ix):
        try:
            task = self.task_list.get_task(ix)
            task.mark_completed()
            return task
        except IndexError:
            return None

    def get_all_tasks(self):
        return self.task_list.tasks

    def get_uncompleted_tasks(self):
        return self.task_list.uncompleted_tasks

    def get_overdue_tasks(self):
        import datetime
        return [t for t in self.task_list.uncompleted_tasks
                if datetime.datetime.now() > t.date_due]

    def load_tasks(self, dao):
        loaded = dao.get_all_tasks()
        for task in loaded:
            self.task_list.add_task(task)
        return len(loaded)

    def save_tasks(self, dao):
        dao.save_all_tasks(self.task_list.tasks)

    def check_task_index(self, ix):
        return self.task_list.check_task_index(ix - 1)
