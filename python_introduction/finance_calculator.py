# A program that calculates finances.

# User Input for Financial Details:
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings:
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings:
simple_annual_interest_rate = 0.05
projected_savings = float(monthly_savings) * 12 + (
    float(monthly_savings) * 12 * simple_annual_interest_rate
)
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
