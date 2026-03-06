# Session 1 Section 2 Python Introduction

#%%
#Exercise 1 task: Variables and Types

var_1 = True #Type = boolean
var_2 = 1 #Type = int
var_3 = 3.14159 #Type = float
var_4 = "Hello World" #Type = string
# %%
print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))
# %%
# Exercise 1 task 2: Casting Variables
my_int = 5
my_float = 5.5
my_bool = True
print(my_int)
print(my_bool)
print(my_float)

my_int_float = float(my_int)
my_float_int = int(my_float)
my_bool_int = int(my_bool)
print(my_int_float)
print(my_bool_int)
print(my_float_int)
# %%
# Exercise 2 Arithmetic Operators
#Addition
result_addition = 10 + 5
print("Addition:", result_addition)

#Subtraction
result_subtraction= 20 - 8
print("Subtraction:", result_subtraction)

#Multiplication
result_multiplication= 6 * 4
print("Multiplication:", result_multiplication)

#Division
result_division = 15 / 3
print("Division:", result_division)

#Floor Division
result_floor_division = 17 // 3
print("Floor Division:", result_floor_division)

#Modulus
result_modulus = 17 % 3
print("Modulus:", result_modulus)

#Exponentiation
result_exponentiation = 2 ** 3
print("Exponentiation:", result_exponentiation)
# %%
#Average
num1 = 10

num2 = 5

average = (num1 + num2) / 2
print(f"The average of {num1} and {num2} is {average}")
# %%
#Area of a rectangle
length = 50
width = 7
area = length * width

print(f"The area of a rectangle with length {length} and with {width} is {area}")


# %%
#Exercise 3: Strings and f-Strings

#Task 1
my_string = "This class covers ISD."
print(my_string)

my_uppercase_string = my_string.upper()
print(my_uppercase_string)
my_lowercase_string = my_string.lower()
print(my_lowercase_string)

my_new_string = my_string.replace("ISD", "Interactive Software Design")
print(my_new_string)

my_string_length = len(my_string)
# %%
#Task 2: f-Strings
my_name = "Kofi"
number_of_classes = 3
campus = "Paisley"

my_text = f"My name is {my_name} and I amd studying {number_of_classes} in {campus}"

print(my_text)
# %%
