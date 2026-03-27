import numpy as np


def min_max_scale(arr):
    """Apply min-max scaling to a NumPy array. Returns values in [0, 1]."""
    return (arr - arr.min()) / (arr.max() - arr.min())


if __name__ == "__main__":
    sample = np.array([10, 20, 30, 40, 50])
    scaled = min_max_scale(sample)
    print(f"Original: {sample}")
    print(f"Scaled:   {scaled}")
