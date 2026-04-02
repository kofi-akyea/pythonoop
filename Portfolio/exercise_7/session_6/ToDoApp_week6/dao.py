import csv
import datetime
import pickle
from tasks import Task, RecurringTask


class TaskTestDAO:
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def get_all_tasks(self):
        task_list = [
            Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)),
            Task("Do laundry",    datetime.datetime.now() + datetime.timedelta(days=2)),
            Task("Clean room",    datetime.datetime.now() - datetime.timedelta(days=1)),
            Task("Do homework",   datetime.datetime.now() + datetime.timedelta(days=3)),
            Task("Walk dog",      datetime.datetime.now() + datetime.timedelta(days=5)),
            Task("Do dishes",     datetime.datetime.now() + datetime.timedelta(days=6)),
        ]

        r_task = RecurringTask("Go to the gym", datetime.datetime.now(),
                               datetime.timedelta(days=7))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=22))
        r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28)
        task_list.append(r_task)

        return task_list

    def save_all_tasks(self, tasks):
        pass  # Test DAO does not persist


class TaskCsvDAO:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        self.fieldnames = ["title", "type", "date_due", "completed",
                           "interval", "completed_dates", "date_created"]

    def get_all_tasks(self):
        task_list = []
        with open(self.storage_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                task_type = row["type"]
                task_title = row["title"]
                task_date_due = datetime.datetime.strptime(row["date_due"], "%d/%m/%Y")
                task_completed = row["completed"].upper() == "TRUE"
                task_date_created = datetime.datetime.strptime(row["date_created"], "%d/%m/%Y")

                # Task A: create the correct object type
                if task_type == "RecurringTask":
                    # Parse interval — take only the leading number (days)
                    interval_days = int(row["interval"].split()[0])
                    interval = datetime.timedelta(days=interval_days)

                    task = RecurringTask(task_title, task_date_due, interval)
                    task.date_created = task_date_created
                    task.completed = task_completed

                    # Parse completed_dates list (comma-separated date strings)
                    if row["completed_dates"].strip():
                        for date_str in row["completed_dates"].split(","):
                            date_str = date_str.strip()
                            if date_str:
                                task.completed_dates.append(
                                    datetime.datetime.strptime(date_str, "%Y-%m-%d"))
                else:
                    task = Task(task_title, task_date_due)
                    task.date_created = task_date_created
                    task.completed = task_completed

                task_list.append(task)
        return task_list

    def save_all_tasks(self, tasks):
        with open(self.storage_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for task in tasks:
                row = {}

                # Task B: fill in the correct values
                row["title"] = task.title
                row["date_due"] = task.date_due.strftime("%d/%m/%Y")
                row["completed"] = str(task.completed).upper()
                row["date_created"] = task.date_created.strftime("%d/%m/%Y")

                if isinstance(task, RecurringTask):
                    row["type"] = "RecurringTask"
                    row["interval"] = str(task.interval)
                    row["completed_dates"] = ",".join(
                        d.strftime("%Y-%m-%d") for d in task.completed_dates)
                else:
                    row["type"] = "Task"
                    row["interval"] = ""
                    row["completed_dates"] = ""

                writer.writerow(row)


class TaskPickleDAO:
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def get_all_tasks(self):
        with open(self.storage_path, "rb") as file:
            return pickle.load(file)

    def save_all_tasks(self, tasks):
        with open(self.storage_path, "wb") as file:
            pickle.dump(tasks, file)
