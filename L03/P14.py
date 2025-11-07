

def calculate_fuel_energy():
    
   
    LITERS_PER_BARREL = 158.987

   
    try:
        fuel_density = float(input("Fuel density (in kg/L): "))
        calorific_value = float(input("Calorific value (in MJ/kg): "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

   
    energy_per_liter = fuel_density * calorific_value
    print("This fuel has energy per volume of {:.2f} MJ/L.".format(energy_per_liter))
 
    energy_per_barrel = energy_per_liter * LITERS_PER_BARREL
    print("That is {:.2f} MJ/bbl.".format(energy_per_barrel))


if __name__ == "__main__":
    calculate_fuel_energy()

