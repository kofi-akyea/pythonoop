# Temperature Converter
# This program converts temperature from Celsius to Fahrenheit and Kelvin.

scales = ["C", "F", "K"]

# Minimum physical temperatures (absolute zero) for each scale
MIN_TEMPS = {
    "C": -273.15,
    "F": -459.67,
    "K": 0.0,
}

def convert(temperature_scale: str = "C", temperature_input: str = "0"):
    # Task 1: handle invalid scale
    if temperature_scale not in scales:
        raise ValueError(f"Invalid temperature scale '{temperature_scale}'. Use 'C', 'F', or 'K'.")

    temp = float(temperature_input)

    # Task 2: reject temperatures below absolute zero for the given scale
    if temp < MIN_TEMPS[temperature_scale]:
        raise ValueError(
            f"{temp} {temperature_scale} is below absolute zero "
            f"(minimum: {MIN_TEMPS[temperature_scale]} {temperature_scale})."
        )

    if scales.index(temperature_scale) == 0:  # Celsius
        degree_celcius = temp
        degree_fahrenheit = (degree_celcius * 9 / 5) + 32
        degree_kelvin = degree_celcius + 273.15
    elif scales.index(temperature_scale) == 1:  # Fahrenheit
        degree_fahrenheit = temp
        degree_celcius = (degree_fahrenheit - 32) * 5 / 9
        degree_kelvin = (degree_fahrenheit + 459.67) * 5 / 9
    elif scales.index(temperature_scale) == 2:  # Kelvin
        degree_kelvin = temp
        degree_celcius = degree_kelvin - 273.15
        degree_fahrenheit = (degree_kelvin - 273.15) * 9 / 5 + 32

    return degree_celcius, degree_fahrenheit, degree_kelvin


# The next line prevents the code from being run if called by a test
if __name__ == "__main__":
    temperature_scale = input(
        "Enter the temperature scale you want to convert from: \n 'C' Celsius \n 'F' Fahrenheit \n 'K' Kelvin \n"
    ).strip().upper()

    if temperature_scale not in scales:
        print("Invalid scale. Please enter 'C', 'F', or 'K'.")
        exit()

    temperature_input = input(f"Enter the temperature in {temperature_scale}: ")

    try:
        degree_celcius, degree_fahrenheit, degree_kelvin = convert(temperature_scale, temperature_input)
        print("Temperature Conversion Results:")
        print(f"{degree_celcius} degree Celsius")
        print(f"{degree_fahrenheit} degree Fahrenheit")
        print(f"{degree_kelvin} degree Kelvin")
        print("Thank you for using the Temperature Converter!")
    except ValueError as e:
        print(f"Error: {e}")
