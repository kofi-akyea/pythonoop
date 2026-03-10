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