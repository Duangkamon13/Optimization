# P2: Rice quantity conversion
rice_kwian = int(input("Enter rice quantity (kwian): "))
rice_tang = rice_kwian * 100
rice_kg = rice_tang * 10
sheet = "{} kw = {} tg = {} kg"
print(sheet.format(rice_kwian,rice_tang,rice_kg))
