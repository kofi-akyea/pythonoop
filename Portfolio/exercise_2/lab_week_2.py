# %%
# Exercise 1
is_true = True
print(is_true)

is_false = 5 < 4
# %%
# Exercise 2
age = 25

is_in_age_range = age > 20 and age < 30
print(is_in_age_range)
# %%
age = 19
age_group = "child"

if age > 18:
    age_group = "adult"

print(f"The age group is {age_group}")

# %%
wind_speed = 5

if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")
# %%
#Exercise 5: if-elif conditionals

grade = 55
if grade < 50:
    print("You failed")
elif grade < 60:
    print("You passed")
elif grade < 70:
    print("You got a good pass")
else:
    print("You got an excellent pass")
# %%
# Exercise 6

temperature1 = 45
temperature2 = 45

if temperature1 == temperature2:
    print(f"You entered {temperature2} degrees and {temperature2} degrees. They are equal")
else: 
    print(f"You entered {temperature2} degrees and {temperature2} degrees. They are not equal")
# %%
#Section 2: Python Lists
#Exercise 1: Creating a list

integer_list = [1,2,3,4,5]
string_list = ["apple", "banana", "orange", "grape"]
empty_list = []
list_with_different_types = [1, "two", 3.0, True]

person_1_age = 20
person_2_age = 24

age_list = [person_1_age, person_2_age]

list_within_a_list = [["red","yellow","green"], ["blue", "black", "white"]]


# %%
#Exercise 2: Accessing a list
city_list  = ["Glasgow", "London", "Edinburg"]
print(city_list[2])
print(city_list[1:3])

# %%
#Exercise 3: Modifying a list
city_list  = ["Glasgow", "London", "Edinburg"]
city_list.append("Manchester")
print(city_list)
city_list[1] = "Birmingham"
print(city_list)
# %%
#Exercise 4

colours = ["red", "yellow", "green"]
print(colours)
second_element = colours[1]
print(second_element)
colours[0] = "blue"
print(colours)
colours_length = len(colours)
print(colours_length)

if colours[0] == "blue":
    print("Blue is in the list")

selected_colours = colours[1:3]
print(selected_colours)

# %%
#Section 3: Python loops
#Exercise 1: While loops
i = 0
while i < 5:
    print(i)
    i+=1

# %%
#Exercise 2: For loops
city_list  = ["Glasgow", "London", "Edinburg"]
for city in city_list:
    print(city)
# %%
#Exercise 3: Loop keywords: range,break and continue
#The range() function is a built-in function in Python that allows you to generate a series of numbers within a given range.
range(0, 5) # will return [0, 1, 2, 3, 4]
range(5) # will return [0, 1, 2, 3, 4]
range(0, 5, 2) # will return [0, 2, 4] because the third parameter is the step size
range(5, 0, -1) # will return [5, 4, 3, 2, 1]

#break keyword stops a loop

for i in range(5):
    if i == 3:
        break
print(i)

#The continue keyword will stop the current iteration of the loop and continue to the next iteration, e.g. skipping the rest of the code in the loop for the current iteration.
for i in range(5):
    if i == 2:
        continue
print(i)


# %%
#Exercise 4

#Even numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    if i % 2 == 0:
        print(i)
        

#Sum of squares
sum_of_squares = 0
for i in range(1,6):
    sum_of_squares += i ** 2
print(sum_of_squares)

#Countdown
countdown = 10
while countdown > 1:
    countdown -=1
    print(countdown)
print("Lift off!!")
# %%
#Section 4: Obtaininf user input
user_input = input("Enter something: ")
print("You entered:", user_input)

# %%
#Exercise 1: User Input Task
#Task 1
user_age = input("How old are you? ")
user_age = int(user_age)

if user_age < 18:
    print("You're a minor")
elif user_age > 18 and user_age <= 65:
    print("You are an adult")
else:
    print("You are a senior citizen")    
# %%

# %%
#Temperature converter
print("Welcome to the Temperature Converter!")
celsius_input = int(input("Enter temperature value"))
# print(celsius_input)
degree_k = celsius_input + 273.15
degree_f = (celsius_input * 9/5) + 32
print("Converted Temperatures:")
print(f"{celsius_input} degree Celsius is equal to {degree_f} Fahrenheit.")
print(f"{celsius_input} degree Celsius is equal to {degree_k} Kelvin.")
# %%
