import sys
import numpy as np
import pandas as pd


def generate_fitness_data(n_days, seed):
    """Generate a synthetic fitness dataset.

    Args:
        n_days: Number of days to generate.
        seed: Random seed for reproducibility.

    Returns:
        DataFrame with columns: date, steps, heart_rate, sleep_hours, calories.
    """
    np.random.seed(seed)
    df = pd.DataFrame({
        "date": pd.date_range("2025-01-01", periods=n_days, freq="D"),
        "steps": np.random.randint(3000, 15000, n_days),
        "heart_rate": np.clip(np.random.normal(72, 8, n_days), 45, 120).round(1),
        "sleep_hours": np.random.uniform(4.5, 9.5, n_days).round(1),
        "calories": (np.random.randint(3000, 15000, n_days) * 0.04
                     + np.random.uniform(150, 300, n_days)).round(1),
    })
    return df


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_fitness_data.py <n_days> <seed>")
        print("Example: python generate_fitness_data.py 365 42")
        sys.exit(1)

    n_days = int(sys.argv[1])
    seed = int(sys.argv[2])

    df = generate_fitness_data(n_days, seed)
    df.to_csv("fitness_data.csv", index=False)

    print(f"Generated dataset with shape: {df.shape}")
    print("Saved to fitness_data.csv")
    print()
    print(df.describe())
