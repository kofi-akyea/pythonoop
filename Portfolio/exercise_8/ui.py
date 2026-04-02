import datetime
from dao import TaskTestDAO, TaskCsvDAO, TaskPickleDAO


class CommandLineUI:
    def __init__(self, controller):
        self.controller = controller

    def _print_menu(self):
        print(f"\n--- To-Do List ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. View overdue tasks")
        print("5. Mark task completed")
        print("6. Load tasks from file")
        print("7. Save tasks to file")
        print("8. Quit")

    def _view_tasks(self):
        tasks = self.controller.get_uncompleted_tasks()
        if not tasks:
            print("No tasks to do!")
            return
        print("The following tasks are still to be done:")
        all_tasks = self.controller.get_all_tasks()
        for task in tasks:
            ix = all_tasks.index(task) + 1
            print(f"{ix}: {task}")

    def run(self):
        while True:
            self._print_menu()
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
                    self.controller.add_task(title, date_due, interval=interval)
                else:
                    self.controller.add_task(title, date_due)
                print("Task added.")

            elif choice == "2":
                self._view_tasks()

            elif choice == "3":
                self._view_tasks()
                try:
                    ix = int(input("Task number to remove: "))
                    self.controller.remove_task(ix)
                    print("Task removed.")
                except ValueError:
                    print("Invalid input.")

            elif choice == "4":
                overdue = self.controller.get_overdue_tasks()
                if not overdue:
                    print("No overdue tasks.")
                else:
                    print("Overdue tasks:")
                    all_tasks = self.controller.get_all_tasks()
                    for task in overdue:
                        ix = all_tasks.index(task) + 1
                        print(f"{ix}: {task}")

            elif choice == "5":
                self._view_tasks()
                try:
                    ix = int(input("Task number to mark completed: "))
                    task = self.controller.complete_task(ix)
                    if task:
                        print(f"'{task.title}' marked as completed.")
                    else:
                        print("Invalid task number.")
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
                    count = self.controller.load_tasks(dao)
                    print(f"Loaded {count} tasks.")
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
                    self.controller.save_tasks(dao)
                    print("Tasks saved.")
                except Exception as e:
                    print(f"Error saving: {e}")

            elif choice == "8":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
