\
def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def convert_temperature(temperature, unit):
    """
    Converts temperature between Celsius and Fahrenheit.

    Args:
        temperature: The temperature value.
        unit: The unit of the temperature ('Celsius' or 'Fahrenheit').

    Returns:
        The converted temperature with the new unit, or an error message for invalid input.
    """
    if unit.lower() == "celsius":
        fahrenheit = celsius_to_fahrenheit(temperature)
        return f"{fahrenheit:.1f} Fahrenheit"
    elif unit.lower() == "fahrenheit":
        celsius = fahrenheit_to_celsius(temperature)
        return f"{celsius:.1f} Celsius"
    else:
        return "Error: Invalid unit. Please use 'Celsius' or 'Fahrenheit'."
