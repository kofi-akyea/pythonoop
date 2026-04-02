import datetime
from tasks import Task, RecurringTask
from task_list import TaskList
from dao import TaskTestDAO, TaskCsvDAO, TaskPickleDAO


def main():
    task_list = TaskList("Student")

    while True:
        task_list.list_options()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            date_str = input("Due date (YYYY-MM-DD): ").strip()
            try:
                date_due = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                print("Invalid date. Using today + 7 days.")
                date_due = datetime.datetime.now() + datetime.timedelta(days=7)

            is_recurring = input("Recurring task? (y/n): ").strip().lower()
            if is_recurring == "y":
                try:
                    days = int(input("Repeat every how many days? "))
                    interval = datetime.timedelta(days=days)
                except ValueError:
                    print("Invalid. Defaulting to 7 days.")
                    interval = datetime.timedelta(days=7)
                task = RecurringTask(title, date_due, interval)
            else:
                task = Task(title, date_due)

            task_list.add_task(task)
            print("Task added.")

        elif choice == "2":
            task_list.view_tasks()

        elif choice == "3":
            task_list.view_tasks()
            try:
                ix = int(input("Task number to remove: "))
                task_list.remove_task(ix)
                print("Task removed.")
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            task_list.view_overdue_tasks()

        elif choice == "5":
            task_list.view_tasks()
            try:
                ix = int(input("Task number to mark completed: "))
                task = task_list.get_task(ix)
                task.mark_completed()
                print(f"'{task.title}' marked as completed.")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == "6":
            print("Load from: (1) Test data  (2) CSV file  (3) Pickle file")
            src = input("Choice: ").strip()
            if src == "1":
                dao = TaskTestDAO("")
            elif src == "2":
                path = input("CSV file path: ").strip()
                dao = TaskCsvDAO(path)
            elif src == "3":
                path = input("Pickle file path: ").strip()
                dao = TaskPickleDAO(path)
            else:
                print("Invalid choice.")
                continue
            try:
                loaded = dao.get_all_tasks()
                for t in loaded:
                    task_list.add_task(t)
                print(f"Loaded {len(loaded)} tasks.")
            except Exception as e:
                print(f"Error loading: {e}")

        elif choice == "7":
            print("Save to: (1) CSV file  (2) Pickle file")
            dst = input("Choice: ").strip()
            if dst == "1":
                path = input("CSV file path: ").strip()
                dao = TaskCsvDAO(path)
            elif dst == "2":
                path = input("Pickle file path: ").strip()
                dao = TaskPickleDAO(path)
            else:
                print("Invalid choice.")
                continue
            try:
                dao.save_all_tasks(task_list.tasks)
                print("Tasks saved.")
            except Exception as e:
                print(f"Error saving: {e}")

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
