# Initialize an empty list to store tasks
class TaskList:
    def __init__(self,owner):
        self.owner = owner
        self.task = []

    def add_task(self,task):
        self.tasks.append(task)
        print(f"Task {task} added successfully!")

    def view_tasks(self, task):
        if not tasks:
            print("No tasks yet. Add one!")
        else:
            print("\nYour tasks:")
            for i, task in self.enumerate(tasks, start=1):
                print(f" {i}. {task}")
        print()

    def remove_task(self, index):
        if 1 <= index <= len(tasks):
            removedTask = tasks.pop(index - 1)
            print(f"Task {removedTask} removed successfully!")
        else:
            print("Invalid task number. Try again")


# tasks =  [] 

def Todo(self):    
    while True:
        print("To-Do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Quit")  
        choice = input("Enter your choice: ")  

        if choice == "1":
            task = input("Enter the task: ")
            self.add_task(task)
        elif choice == "2":
            self.view_tasks()
        elif choice == "3":
            self.view_tasks()
            index = int(input("Enter the task number to remove: "))
            self.remove_task(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")
            