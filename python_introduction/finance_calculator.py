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
# /tmp/correction/3120001615871916859719583418112290743355_5/100739/992906/
# python_introduction/finance_calculator.py
# doesn't contain monthly_savings\s*=\s*(monthly_income\s*-\s*monthly_expenses|
# float\s*\(\s*monthly_income\s*\)\s*-\s*float\s*\(\s*monthly_expenses\s*\))
