from task_list import TaskManager

def run_app():
    manager = TaskManager("Kofi")
    
    while True:
        print(f"\n--- {manager.owner.upper()}'S TODO MANAGER ---")
        print("1. Add Task | 2. View Tasks | 3. Remove Task | 4. Quit")
        
        choice = input("Choice: ")

        if choice == "1":
            desc = input("Task description: ")
            try:
                days = int(input("Days until due: "))
                manager.add_new_task(desc, days)
                print("Added!")
            except ValueError:
                print("Please enter a number for days.")

        elif choice == "2":
            tasks = manager.get_all_tasks()
            if not tasks:
                print("\nList is empty!")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

        elif choice == "3":
            try:
                idx = int(input("Task number to remove: ")) - 1
                removed = manager.remove_task_at(idx)
                if removed:
                    print(f"Removed: {removed.description}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    run_app()