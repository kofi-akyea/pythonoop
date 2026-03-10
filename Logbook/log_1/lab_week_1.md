# Session 1 Section 2 Python Introduction

## Exercise 1 task: Variables and Types

```python
# Declaring variables in python and assigning their correct types.
#We declared 4 variables var_1, var_2,var_3 and var_4 an set their values to the 4 primary data types in python (boolean, integer, float and string) respectively
var_1 = True #Type = boolean
var_2 = 1 #Type = int
var_3 = 3.14159 #Type = float
var_4 = "Hello World" #Type = string
```

### Printing variables and their types

```python
## We then printed each variable's type using the print() function provided by python
var_1 = True #Type = boolean
var_2 = 1 #Type = int
var_3 = 3.14159 #Type = float
var_4 = "Hello World" #Type = string
print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

#Output for printing variables and their types

<class 'bool'>
<class 'int'>
<class 'float'>
<class 'str'>
```

## Exercise 1 task 2: Casting Variables

```python
my_int = 5
my_float = 5.5
my_bool = True
print(my_int)
print(my_bool)
print(my_float)

#Output

5
True
5.5
```

## Casting variables to different datatypes

```python
#Code
#We convert or cast the variables to different data types using the various inbult python functions: float() which converts a variables to a float and int() which converts a variable to an integer
my_int_float = float(my_int)
my_float_int = int(my_float)
my_bool_int = int(my_bool)
print(my_int_float)
print(my_bool_int)
print(my_float_int)

#Code output
5.0
1
5
```

## Exercise 2 Arithmetic Operators

```python
#Addition
#We performed basic mathematical addition using the addition operator (+)
result_addition = 10 + 5
print("Addition:", result_addition)

#Output
Addition: 15

#Subtraction
#We performed basic mathematical subtraction using the subtraction operator (-)
result_subtraction= 20 - 8
print("Subtraction:", result_subtraction)

#Output
Subtraction: 12

#Multiplication
#We performed basic mathematical multiplication using the multiplication operator (*)
result_multiplication= 6 * 4
print("Multiplication:", result_multiplication)

#Output
Multiplication: 24

#Division
#We performed basic mathematical division using the division operator (/)
result_division = 15 / 3
print("Division:", result_division)

#Division: 5.0

#Floor Division
#We performed  floor division using the floor division operator (//)
result_floor_division = 17 // 3
print("Floor Division:", result_floor_division)

#Output
Floor Division: 5

#Modulus
#We performed basic mathematical modulus using the modulus operator (%)
result_modulus = 17 % 3
print("Modulus:", result_modulus)

#Output
Modulus: 2

#Exponentiation
#We performed basic exponentiation using the exponentiation operator (**)
result_exponentiation = 2 ** 3
print("Exponentiation:", result_exponentiation)

#Output
Exponentiation: 8

#Average
#We found the average of two numbers 10 and 5, stored in variable names num1 and num2 and printed the output in a sentence using an f string
num1 = 10

num2 = 5

average = (num1 + num2) / 2
print(f"The average of {num1} and {num2} is {average}")

#Output
The average of 10 and 5 is 7.5

#Area of a rectangle
#We found the area of a rectangle by storing its length and with in two variables and using those variables in a new variable "area" which multiplies the length and width and finally printed the output using an fstring.
length = 50
width = 7
area = length * width

print(f"The area of a rectangle with length {length} and with {width} is {area}")

#Output
The area of a rectangle with length 50 and with 7 is 350

```

## Exercise 3: Strings and f-Strings#Exercise 3: Strings and f-Strings

### Strings and string methods

```python
#Task 1
#Task one focuses on strings and the various string methods: .upper() converts a string text to upper case, .lower() converts a string to lower case and .replace() accepts two arguments and replaces the first arguments value with the second arguments value in the string
my_string = "This class covers ISD."
print(my_string)

#Output
This class covers ISD.

my_uppercase_string = my_string.upper()
print(my_uppercase_string)

#Output
THIS CLASS COVERS ISD.

my_lowercase_string = my_string.lower()
print(my_lowercase_string)

#Output
this class covers isd.

my_new_string = my_string.replace("ISD", "Interactive Software Design")
print(my_new_string)

#Output
This class covers Interactive Software Design.

my_string_length = len(my_string)
print(my_string_length)

#Output
22
```

### fstrings

```python
#fstrings are used to insert variables into strings withe bractets "{}". In task 2 we set 3 variables and use them to construct the sentence in the my_text variable
#Task 2: f-Strings
my_name = "Kofi"
number_of_classes = 3
campus = "Paisley"

my_text = f"My name is {my_name} and I amd studying {number_of_classes} in {campus}"

print(my_text)

#Output
My name is Kofi and I amd studying 3 classes in Paisley
```
