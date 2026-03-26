# greet.py — A script that greets a user by name using sys.argv

import sys

if len(sys.argv) < 2:
    print("Usage: python greet.py <name>")
    print("Example: python greet.py Alice")
    sys.exit(1)

name = sys.argv[1]
print(f"Hello, {name}! Welcome to Python scripts.")
