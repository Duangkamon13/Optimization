def carbon_14_dating():
    HALF_LIFE = 5730
    current_ratio = float(input("ratio: "))
    sensitivity = float(input("sensitivity: "))
   
    year = 0

    while current_ratio >= sensitivity:
        print("Year", str(year) + ":", "ratio =", current_ratio)
        current_ratio /= 2
        year += HALF_LIFE
if __name__ == "__main__":
    carbon_14_dating()
