import numpy as np
import pandas as pd


def z_score(arr):
    """Standardize a NumPy array to z-scores."""
    return (arr - arr.mean()) / arr.std()


def weekly_summary(df, date_col, value_col):
    """Resample a DataFrame to weekly mean for a given column.

    Args:
        df: DataFrame with a date column and a value column.
        date_col: Name of the date column.
        value_col: Name of the column to aggregate.

    Returns:
        Series with weekly mean values, indexed by week start date.
    """
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.set_index(date_col)
    return df[[value_col]].resample("W").mean()


def detect_anomalies(arr, threshold=2.0):
    """Return a boolean mask where |z_score| > threshold."""
    scores = z_score(arr)
    return np.abs(scores) > threshold


if __name__ == "__main__":
    sample = np.array([10, 12, 11, 13, 50, 9, 11, 10, 12, 8])
    print("Sample array:", sample)
    print("Z-scores:    ", z_score(sample).round(2))
    print("Anomalies:   ", detect_anomalies(sample, threshold=2.0))
    print(f"Anomaly values: {sample[detect_anomalies(sample, threshold=2.0)]}")
