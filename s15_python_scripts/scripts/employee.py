# employee.py — Employee class module (no __name__ guard)

from datetime import datetime


class Employee:
    """Represents an employee with name, role, and start date."""

    def __init__(self, name, role, start_date):
        self.name = name
        self.role = role
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")

    def years_employed(self):
        """Calculate years since start date."""
        delta = datetime.now() - self.start_date
        return round(delta.days / 365.25, 1)

    def __repr__(self):
        return f"Employee('{self.name}', '{self.role}')"

    def __str__(self):
        return f"{self.name} — {self.role} ({self.years_employed()} years)"


# Demo code — runs every time this file is executed OR imported
print("--- Employee Demo ---")
emp = Employee("Alice", "Data Analyst", "2022-03-15")
print(emp)
print(f"Years employed: {emp.years_employed()}")
