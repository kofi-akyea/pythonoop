import datetime
from tasks import Task, RecurringTask
from task_list import TaskList
from users import Owner


def propagate_task_list(task_list):
    task_list.add_task(Task("Buy groceries",
                            datetime.datetime.now() + datetime.timedelta(days=1)))
    task_list.add_task(Task("Submit assignment",
                            datetime.datetime.now() - datetime.timedelta(days=2),
                            "Upload to Aula before midnight"))
    task_list.add_task(Task("Call dentist",
                            datetime.datetime.now() + datetime.timedelta(days=5)))

    # Sample recurring task
    r_task = RecurringTask("Go to the gym", datetime.datetime.now(),
                           datetime.timedelta(days=7))
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=22))
    r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28)
    task_list.add_task(r_task)

    return task_list


def main():
    default_owner = Owner("Student", "student@uws.ac.uk")
    task_list = TaskList(default_owner)
    task_list = propagate_task_list(task_list)

    print(f"Logged in as: {default_owner}")

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
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
