# A program that calculates finances.

# User Input for Financial Details:
monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings:
monthly_savings = monthly_income - total_monthly_expenses

# Project Annual Savings:
simple_annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (
    monthly_savings * 12 * simple_annual_interest_rate
)
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}")
# /tmp/correction/3120001615871916859719583418112290743355_5/100739/992906/
# python_introduction/finance_calculator.py
# doesn't contain monthly_savings\s*=\s*(monthly_income\s*-\s*monthly_expenses|
# float\s*\(\s*monthly_income\s*\)\s*-\s*float\s*\(\s*monthly_expenses\s*\))
