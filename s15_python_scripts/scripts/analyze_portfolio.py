# analyze_portfolio.py — Analyze stock transactions from a CSV file
#
# Usage:
#   python analyze_portfolio.py <csv_file> [currency]
#
# Examples:
#   python analyze_portfolio.py transactions.csv
#   python analyze_portfolio.py transactions.csv USD

import sys
import csv
from datetime import datetime


class Transaction:
    """Represents a single stock transaction."""

    def __init__(self, date, ticker, action, shares, price, currency="USD"):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.ticker = ticker
        self.action = action  # "BUY" or "SELL"
        self.shares = int(shares)
        self.price = float(price)
        self.currency = currency

    @property
    def total(self):
        """Total value of the transaction."""
        return self.shares * self.price

    def __repr__(self):
        return f"Transaction('{self.ticker}', '{self.action}', {self.shares} @ {self.price})"

    def __str__(self):
        return f"{self.date:%Y-%m-%d} | {self.action:4s} | {self.ticker:5s} | {self.shares:4d} shares @ ${self.price:,.2f} = ${self.total:,.2f}"


def load_transactions(filepath):
    """Load transactions from a CSV file."""
    transactions = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            t = Transaction(
                date=row["date"],
                ticker=row["ticker"],
                action=row["action"],
                shares=row["shares"],
                price=row["price"],
                currency=row.get("currency", "USD"),
            )
            transactions.append(t)
    return transactions


def summarize(transactions, currency_filter=None):
    """Print a summary of the transactions."""
    if currency_filter:
        transactions = [t for t in transactions if t.currency == currency_filter]

    if not transactions:
        print("No transactions found.")
        return

    total_bought = sum(t.total for t in transactions if t.action == "BUY")
    total_sold = sum(t.total for t in transactions if t.action == "SELL")
    tickers = sorted(set(t.ticker for t in transactions))

    print(f"Portfolio Summary ({len(transactions)} transactions)")
    print("=" * 40)
    print(f"  Tickers: {', '.join(tickers)}")
    print(f"  Total bought: ${total_bought:,.2f}")
    print(f"  Total sold:   ${total_sold:,.2f}")
    print(f"  Net invested: ${total_bought - total_sold:,.2f}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_portfolio.py <csv_file> [currency]")
        sys.exit(1)

    filepath = sys.argv[1]
    currency_filter = sys.argv[2] if len(sys.argv) > 2 else None

    transactions = load_transactions(filepath)
    summarize(transactions, currency_filter)
