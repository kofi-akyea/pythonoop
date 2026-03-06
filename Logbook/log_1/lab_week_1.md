# Session 1 Section 2 Python Introduction

## Exercise 1 task: Variables and Types

```python
# Declaring variables in python and assigning their correct types
var_1 = True #Type = boolean
var_2 = 1 #Type = int
var_3 = 3.14159 #Type = float
var_4 = "Hello World" #Type = string
```

### Printing variables and their types

```python
var_1 = True #Type = boolean
var_2 = 1 #Type = int
var_3 = 3.14159 #Type = float
var_4 = "Hello World" #Type = string
print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))
```

#### Output for printing variables and their types

```python
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
```

### Output for printing variables data

```python
5
True
5.5
```

## Casting variables to different datatypes

```python
#Code
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
result_addition = 10 + 5
print("Addition:", result_addition)

#Output
Addition: 15

#Subtraction
result_subtraction= 20 - 8
print("Subtraction:", result_subtraction)

#Output
Subtraction: 12

#Multiplication
result_multiplication= 6 * 4
print("Multiplication:", result_multiplication)

#Output
Multiplication: 24

#Division
result_division = 15 / 3
print("Division:", result_division)

#Division: 5.0

#Floor Division
result_floor_division = 17 // 3
print("Floor Division:", result_floor_division)

#Output
Floor Division: 5

#Modulus
result_modulus = 17 % 3
print("Modulus:", result_modulus)

#Output
Modulus: 2

#Exponentiation
result_exponentiation = 2 ** 3
print("Exponentiation:", result_exponentiation)

#Output
Exponentiation: 8

#Average
num1 = 10

num2 = 5

average = (num1 + num2) / 2
print(f"The average of {num1} and {num2} is {average}")

#Output
The average of 10 and 5 is 7.5

#Area of a rectangle
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
#Task 2: f-Strings
my_name = "Kofi"
number_of_classes = 3
campus = "Paisley"

my_text = f"My name is {my_name} and I amd studying {number_of_classes} in {campus}"

print(my_text)

#Output
My name is Kofi and I amd studying 3 classes in Paisley
```
