"""
Exercise 3 - Solution: Sales Report Script
Run with: python report_solved.py  (from the scripts/ folder)
"""

# Read the Q1 sales report
with open("../reports/q1_sales.txt") as f:
    q1_content = f.read()

# Read the Q2 sales report
with open("../reports/q2_sales.txt") as f:
    q2_content = f.read()

# Read the Q3 sales report
with open("../reports/q3_sales.txt") as f:
    q3_content = f.read()

print("=" * 40)
print("ANNUAL SALES SUMMARY")
print("=" * 40)

# Extract totals (the line that starts with "Total:")
for label, content in [("Q1", q1_content), ("Q2", q2_content), ("Q3", q3_content)]:
    for line in content.split("\n"):
        if line.startswith("Total:"):
            total = line.split("$")[1].strip()
            print(f"  {label}: ${total}")

print("=" * 40)
print("Report generated from practice/reports/")
