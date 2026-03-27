import sys
import numpy as np
import pandas as pd


def generate_dataset(n_rows, seed):
    """Generate a synthetic dataset with weather and visitor data."""
    np.random.seed(seed)
    df = pd.DataFrame({
        "date": pd.date_range("2025-01-01", periods=n_rows, freq="D"),
        "temperature": np.random.normal(22, 4, n_rows),
        "humidity": np.random.uniform(30, 90, n_rows),
        "visitors": np.random.randint(50, 500, n_rows),
    })
    return df


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_data.py <n_rows> <seed>")
        print("Example: python generate_data.py 100 42")
        sys.exit(1)

    n_rows = int(sys.argv[1])
    seed = int(sys.argv[2])

    df = generate_dataset(n_rows, seed)
    df.to_csv("output.csv", index=False)

    print(f"Generated dataset with shape: {df.shape}")
    print(f"Saved to output.csv")
    print()
    print(df.describe())
