import sys
import pandas as pd


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python weekly_report.py <csv_path> <metric>")
        print("Example: python weekly_report.py fitness_data.csv steps")
        sys.exit(1)

    csv_path = sys.argv[1]
    metric = sys.argv[2]

    df = pd.read_csv(csv_path, parse_dates=["date"])
    df = df.set_index("date")

    if metric not in df.columns:
        print(f"Error: column '{metric}' not found in {csv_path}")
        print(f"Available columns: {list(df.columns)}")
        sys.exit(1)

    weekly = df[[metric]].resample("W").agg(["mean", "min", "max"])
    weekly.columns = ["mean", "min", "max"]

    print(f"Weekly Report: {metric}")
    print("=" * 45)
    print(f"{'Week of':<14} | {'Mean':>8} | {'Min':>8} | {'Max':>8}")
    print("-" * 45)
    for date, row in weekly.iterrows():
        print(f"{date.strftime('%Y-%m-%d'):<14} | {row['mean']:>8.1f} | {row['min']:>8.1f} | {row['max']:>8.1f}")
