# Session 3 – Functions, Scope and a Larger Programme

## Section 1: Functions & Scope

### Exercise 1 – Functions in Python

A **function** is a reusable block of code that runs when it is called. Functions are defined using the `def` keyword.

```python
def greetUser():
    print("Hello!")

greetUser()
```

#### Output

```console
Hello!
```

#### Function Parameters

A **parameter** is a variable listed inside the parentheses in the function definition. An **argument** is the actual value passed in when the function is called.

```python
def greetUser(name):
    print(f"Hello {name}!")

greetUser("Kay")
```

#### Output

```console
Hello Kay!
```

#### Task 1 – Function with a List Parameter

We extended `greetUser` to accept a list of names and greet each one using a `for` loop:

```python
def greetFriends(names):
    for name in names:
        print(f"Hello {name}!")

greetFriends(["Kofi", "Ama"])
```

#### Output

```console
Hello Kofi!
Hello Ama!
```

---

### The `return` Keyword

The `return` keyword sends a value back to the caller. Without it a function returns `None` by default.

```python
def addNumbers(num1, num2):
    result = num1 + num2
    return result

result = addNumbers(5, 10)
print(result)
```

#### Output

```console
15
```

---

### Tax Calculation

We applied the `return` keyword to a realistic example — calculating an income tax amount:

```python
def calculateTax(income, taxRate):
    taxAmount = income * taxRate
    return taxAmount

taxAmount = calculateTax(50000, 0.2)
print(taxAmount)
```

#### Output

```console
10000.0
```

---

### Compound Interest Calculator

We wrote a more complex function that calculates compound interest year by year. It uses input validation with `if` statements and a `for` loop with `range()`, then returns the final total as an integer:

```python
def compoundInterest(principal, duration, interestRate):
    if interestRate < 0 or interestRate > 1:
        print("Please enter a decimal number between 0 and 1 for the interest rate")
        return None
    if duration < 0:
        print("Please enter a positive number of years")
        return None
    for year in range(duration + 1):
        totalForTheYear = principal * (1 + interestRate) ** year
        print(f"The total amount of money earned by the investment in year {year} is {totalForTheYear}")
    return int(totalForTheYear)

result = compoundInterest(1000, 5, 0.03)
print(f"Returned value: £{result}")
```

#### Output

```console
The total amount of money earned by the investment in year 0 is 1000.0
The total amount of money earned by the investment in year 1 is 1030.0
The total amount of money earned by the investment in year 2 is 1060.9
The total amount of money earned by the investment in year 3 is 1092.727
The total amount of money earned by the investment in year 4 is 1125.5088...
The total amount of money earned by the investment in year 5 is 1159.2740...
Returned value: £1159
```

The `**` operator is used for exponentiation. `int()` truncates the float result, removing the decimal part.

---

## Exercise 2 – Variable Scope

**Scope** controls where a variable can be accessed. A variable defined inside a function is **local** to that function and cannot be used outside it.

```python
def newFunction():
    myNewVariable = 5

newFunction()
# print(myNewVariable)  # This would cause a NameError
```

`myNewVariable` only exists inside `newFunction`. Trying to print it outside causes a `NameError` because the variable is out of scope.

---

## Exercise 3 – Assertions

An **assertion** is a sanity check built into the code using the `assert` keyword. If the condition is `False`, Python raises an `AssertionError` with the provided message.

```python
# assert condition, message
print("Enter marks out of 100:")
num = 175
assert num >= 0 and num <= 100, "Only numbers in the range 0 to 100 are acceptable"
print("Marks obtained:", num)
```

#### Output

```console
AssertionError: Only numbers in the range 0 to 100 are acceptable
```

Because `num = 175` is outside the valid range, the assertion fails immediately and stops the programme. Assertions are useful for catching incorrect values early during development.

---

## Section 3: First Larger-Scale Python Programme

### Exercise 4 – To-Do List Manager

We built a functional To-Do list application that combines functions, a global list, a `while` loop, and user input. The programme has three core functions and a menu loop that runs until the user chooses to quit.

#### `add_task(task)`

Appends a new task string to the global `tasks` list and confirms the addition to the user:

```python
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task {task} added successfully!")
```

#### `view_tasks()`

Checks whether the list is empty and either prompts the user to add a task or prints all tasks numbered using `enumerate`:

```python
def view_tasks():
    if not tasks:
        print("No tasks yet. Add one!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f" {i}. {task}")
    print()
```

`enumerate(tasks, start=1)` gives both the position and the value in one step, avoiding the need for a manual counter.

#### `remove_task(index)`

Removes a task by its 1-based position. Bounds checking prevents an invalid index from crashing the programme:

```python
def remove_task(index):
    if 1 <= index <= len(tasks):
        removedTask = tasks.pop(index - 1)
        print(f"Task {removedTask} removed successfully!")
    else:
        print("Invalid task number. Try again")
```

`pop(index - 1)` converts the user's 1-based number to a 0-based list index before removing the element.

#### Main Menu Loop

A `while True` loop keeps the menu running. `break` exits when the user enters `"4"`:

```python
while True:
    print("To-Do List Manager")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        index = int(input("Enter the task number to remove: "))
        remove_task(index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again")
```

#### Example Session Output

```console
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Quit
Enter your choice: 1
Enter the task: Do Homework
Task Do Homework added successfully!

Enter your choice: 1
Enter the task: Do Laundry
Task Do Laundry added successfully!

Enter your choice: 2

Your tasks:
 1. Do Homework
 2. Do Laundry

Enter your choice: 3

Your tasks:
 1. Do Homework
 2. Do Laundry

Enter the task number to remove: 1
Task Do Homework removed successfully!

Enter your choice: 4
Goodbye!
```
