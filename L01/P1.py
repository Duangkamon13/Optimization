
distance = float(input("Enter distance (m): "))
sprintConstant = float(input("Enter spring constant (N/m): "))

force = distance * sprintConstant

sheet = "The force is {:.3f} N"
print(sheet.format(force))