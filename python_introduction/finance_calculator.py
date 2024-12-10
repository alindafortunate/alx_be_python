# A program that calculates finances.

# User Input for Financial Details:
monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings:
monthly_savings = monthly_income - total_monthly_expenses

# Project Annual Savings:
simple_annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (
    monthly_savings * 12 * simple_annual_interest_rate
)
print(f"Projected savings after one year, with interest, is: ${projected_savings}")