"""
Exercise 2 - Solution: Simple Calculator
Run with: python calculator_solved.py
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"\n{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Cannot divide by zero!")
