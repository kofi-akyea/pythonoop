# %%
#Section 1: Functions & Scope
##Exercise 1: Functions in Python

def greetUser():
    print("Hello!")

greetUser()
# %%
##Function parameters
def greetUser(name):
    print(f"Hello {name}!") #name is the parameter

greetUser("Kay") #"Kay" is the arguement
# %%
##Task 1

def greetFriends(names):
    for name in names:
        print(f"Hello {name}!")
        
greetFriends(["Kofi", "Ama"])
# %%
## Return Keyword
def addNumbers(num1, num2):
    result = num1 + num2
    return result
result = addNumbers(5,10)
print(result)

# %%
##Tax Calculation
def calculateTax(income, taxRate):
    taxAmount = income * taxRate
    return taxAmount

taxAmount = calculateTax(50000, 0.2)

print(taxAmount)
# %%
#Compound Interest Calculator
   
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
         
# %%
# Exercise 2: Variable Scope
def newFunction():
    myNewVariable = 5

newFunction()

#print(myNewVariable) # will cause an error
# %%
# Assertions
#Task 1

#assert condition, message
print("Enter marks out of 100:")
num = 175
assert num >= 0 and num <= 100, "Only numbers in the range 0 to 100 are acceptable"
print("Marks obtained:", num)
# %%
#Section 3: Your first larger-scale Python programme
##Exercise 4: Complete template program

#%%





