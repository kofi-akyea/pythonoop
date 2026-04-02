import datetime


class Task:
    def __init__(self, title, date_due, description=""):
        self.title = title
        self.completed = False
        self.date_created = datetime.datetime.now()
        self.date_due = date_due
        self.description = description

    def mark_completed(self):
        self.completed = True

    def change_title(self, new_title):
        self.title = new_title

    def change_date_due(self, date_due_str):
        self.date_due = datetime.datetime.strptime(date_due_str, "%Y-%m-%d")

    def change_description(self, description):
        self.description = description

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        overdue = " [OVERDUE]" if not self.completed and datetime.datetime.now() > self.date_due else ""
        result = f"{self.title} [{status}]{overdue}\n"
        result += f"   Created: {self.date_created.strftime('%Y-%m-%d')} | Due: {self.date_due.strftime('%Y-%m-%d')}"
        if self.description:
            result += f"\n   {self.description}"
        return result


class RecurringTask(Task):
    def __init__(self, title, date_due, interval, description=""):
        super().__init__(title, date_due, description)
        self.interval = interval
        self.completed_dates = []

    def _compute_next_due_date(self):
        return self.date_due + self.interval

    def mark_completed(self):
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()
        self.completed = False

    def __str__(self):
        dates = [d.strftime('%Y-%m-%d') for d in self.completed_dates]
        return (f"{self.title} - Recurring (created: {self.date_created.strftime('%Y-%m-%d')}, "
                f"due: {self.date_due.strftime('%Y-%m-%d')}, "
                f"completed: {dates}, interval: {self.interval.days} days)")
