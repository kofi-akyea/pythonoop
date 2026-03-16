#%%
class TaskList: # to define a class in python you use the Class keyword followed by the classname
    def __init__(self, owner): # to add attributes to classes we define them using the __init__ method. this method is always called whenw e create an object instance of a class. the self word is used to represent the instance of the class, it allows you to access the attributes and methods of the class
        self.owner = owner
        self.tasks = []
    
my_task_list = TaskList("Kofi")
print(my_task_list.owner)

# %%
#Exercise 2: Adding Methods
class TaskList:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            removedTask = self.tasks.pop(index - 1)
            print(f"Task {removedTask} removed successfully!")
        else:
            print("Invalid task number. Try again")
    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet. Add one!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f" {i}. {task}")
        print()
        
        
my_task_list = TaskList("Kofi")
my_task_list.tasks = ["Do Homework", "Do Laundry", "Go Shopping"]
my_task_list.view_tasks()

# %%
#Exercise 4
if choice == "1":
    title = input("Enter a task: ")
    task = Task(title)
    self.add_task(task)
    
    
    
    
#%%
class TaskList:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

my_task_list = TaskList("Kofi")
print(my_task_list.owner)
# %%
my_task_list = TaskList("Kofi")
my_task_list.tasks = ["Do Homework", "Do Laundry", "Go Shopping"]
my_task_list.view_tasks()
my_task_list.remove_task(1)
my_task_list.view_tasks()
# %%
