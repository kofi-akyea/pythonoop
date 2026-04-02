import datetime
from tasks import Task, RecurringTask


class TaskFactory:
    @staticmethod
    def create_task(title, date_due, **kwargs):
        interval = kwargs.get("interval")
        if interval is not None:
            return RecurringTask(title, date_due, interval)
        return Task(title, date_due)
