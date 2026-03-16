from datetime import datetime, timedelta

class TaskList:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

    def add_task(self, task_name, days_to_complete):
        # 1. Get the current time
        now = datetime.now()
        added_on = now.strftime("%Y-%m-%d %H:%M")

        # 2. Calculate the due date using timedelta
        due_date_obj = now + timedelta(days=days_to_complete)
        due_on = due_date_obj.strftime("%Y-%m-%d")

        # 3. Store task
        task_entry = {
            "name": task_name,
            "added": added_on,
            "due": due_on,
            "due_obj": due_date_obj # Stored for "Overdue" comparisons later
        }

        self.tasks.append(task_entry)
        print(f"\n Task '{task_name}' added successfully!")
        print(f"   Deadline: {due_on}")

    def view_tasks(self):
        if not self.tasks:
            print("\n Your list is empty. Add a task!")
        else:
            print(f"\n--- {self.owner.upper()}'S TODO LIST ---")
            now = datetime.now()
            
            for i, task in enumerate(self.tasks, start=1):
                # Check if task is overdue
                status = " [!] OVERDUE" if now > task["due_obj"] else ""
                
                print(f"{i}. {task['name']}{status}")
                print(f"   Added: {task['added']} | Due: {task['due']}")
        print("-" * 30)

    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"\n Removed: {removed['name']}")
        else:
            print("\n Invalid task number!")

    def run(self):
        while True:
            print("\n--- MAIN MENU ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Quit")
            
            choice = input("Enter choice (1-4): ")

            if choice == "1":
                name = input("What is the task? ")
                try:
                    days = int(input("How many days do you have to finish it? "))
                    self.add_task(name, days)
                except ValueError:
                    print("Please enter a valid number for days!")
            
            elif choice == "2":
                self.view_tasks()
            
            elif choice == "3":
                self.view_tasks()
                if self.tasks:
                    try:
                        idx = int(input("Enter task number to remove: "))
                        self.remove_task(idx)
                    except ValueError:
                        print("Please enter a valid number!")
            
            elif choice == "4":
                print(f"Goodbye, {self.owner}!")
                break
            else:
                print("Invalid choice. Try again.")

# Start the application
if __name__ == "__main__":
    app = TaskList("Kofi")
    app.run()