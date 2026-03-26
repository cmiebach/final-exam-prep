# utils.py — Temperature conversion utilities (no __name__ guard)


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def format_temperature(value, unit="C"):
    """Format a temperature value with its unit symbol."""
    return f"{value:.1f} °{unit}"


# Demo code — runs every time this file is executed OR imported
print("=== Temperature Converter ===")
temp_c = 100
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{format_temperature(temp_c, 'C')} = {format_temperature(temp_f, 'F')}")

temp_f = 72
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{format_temperature(temp_f, 'F')} = {format_temperature(temp_c, 'C')}")
