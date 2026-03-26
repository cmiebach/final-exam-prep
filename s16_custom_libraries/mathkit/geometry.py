"""Geometry classes for mathkit."""

import math


class Circle:
    """A circle defined by its radius."""

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __str__(self):
        return f"Circle with radius {self.radius} (area={self.area():.2f})"


class Rectangle:
    """A rectangle defined by width and height."""

    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative")
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    @property
    def is_square(self):
        """Check if the rectangle is a square."""
        return self.width == self.height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __str__(self):
        shape = "Square" if self.is_square else "Rectangle"
        return f"{shape} ({self.width} x {self.height}, area={self.area():.2f})"
