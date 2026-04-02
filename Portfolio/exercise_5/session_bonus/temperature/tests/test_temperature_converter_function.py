import pytest
from src.temperature_converter_function import convert

# Basic single conversion test
def test_temperature_converter_basic():
    celsius, fahrenheit, kelvin = convert("C", "0")
    assert celsius == pytest.approx(0, abs=0.01)
    assert fahrenheit == pytest.approx(32.0, abs=0.01)
    assert kelvin == pytest.approx(273.15, abs=0.01)


# Parametrize test for all three valid scales
@pytest.mark.parametrize(
    "scale, temp, expected_celsius, expected_fahrenheit, expected_kelvin",
    [
        ("C", "0", 0.0, 32.0, 273.15),
        ("F", "32", 0.0, 32.0, 273.15),
        ("K", "273.15", 0.0, 32.0, 273.15),
    ],
)
def test_temperature_converter_parametrize(scale, temp, expected_celsius, expected_fahrenheit, expected_kelvin):
    celsius, fahrenheit, kelvin = convert(scale, temp)
    assert celsius == pytest.approx(expected_celsius, abs=0.01)
    assert fahrenheit == pytest.approx(expected_fahrenheit, abs=0.01)
    assert kelvin == pytest.approx(expected_kelvin, abs=0.01)


# Task 1: invalid scale raises ValueError
def test_invalid_scale_raises_error():
    with pytest.raises(ValueError):
        convert("Z", "273.15")


# Task 2: temperatures below absolute zero raise ValueError
@pytest.mark.parametrize(
    "scale, below_minimum",
    [
        ("C", "-274"),     # below -273.15 C
        ("F", "-460"),     # below -459.67 F
        ("K", "-1"),       # below 0 K
    ],
)
def test_below_absolute_zero_raises_error(scale, below_minimum):
    with pytest.raises(ValueError):
        convert(scale, below_minimum)
