waste_per_person = float(input("Waste: "))
capacity = float(input("Cap: "))

population = 70000000
total_waste = waste_per_person * population
daily_land_m2 = total_waste / capacity
annual_land_m2 = daily_land_m2 * 365

daily_land_rai = daily_land_m2 / 1600
annual_land_rai = annual_land_m2 / 1600


print("Total waste= %.2f" % total_waste)
print("Landfill= %.2f" % daily_land_rai)
print("Annual land= %.2f" % annual_land_rai)
