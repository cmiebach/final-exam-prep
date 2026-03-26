"""Statistical functions for mathkit."""

import math


def mean(numbers):
    """Calculate the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot compute mean of an empty list")
    return sum(numbers) / len(numbers)


def median(numbers):
    """Calculate the median of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot compute median of an empty list")
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]


def std_dev(numbers):
    """Calculate the population standard deviation of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot compute std_dev of an empty list")
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)
