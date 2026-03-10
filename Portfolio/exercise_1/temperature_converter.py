# %%
print("Welcome to the Temperature Converter!")
celsius_input = int(input("Enter temperature value"))
# print(celsius_input)
degree_k = celsius_input + 273.15
degree_f = (celsius_input * 9/5) + 32
print("Converted Temperatures:")
print(f"{celsius_input} degree Celsius is equal to {degree_f} Fahrenheit.")
print(f"{celsius_input} degree Celsius is equal to {degree_k} Kelvin.")
# %%
