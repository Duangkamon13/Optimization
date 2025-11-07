"""
Template

Write a program to ask a user for an investment in rice production (baht/rai), an average rice production (kg/rai) and the wholesale price (baht/kwian), calculate the balance sheet, and report it.
"""
# Ask user
investment = float(input("Investment (baht/rai): "))
production = float(input("Rice production (kg/rai): "))
wholesale = float(input("Wholesale price (baht/kwian): "))

# Calculate income
income = production / 1000 * wholesale  # unit conversion: kg -> kwian

# Calculate balance
balance = income - investment


sheet = "Balance = income ({:,.2f}) - investment ({:,.2f}) = {:,.2f} baht/rai"

print(sheet.format(income, investment, balance))