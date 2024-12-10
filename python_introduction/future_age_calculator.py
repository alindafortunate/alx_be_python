# A program to calculate age.

# Promot the user for his age.
years = int(input("How old are you? "))
current_year = 2023
birth_year = current_year - years
future_year = 2050
future_age = future_year - birth_year
print(f"In {future_year}, you will be {future_age} years old.")
