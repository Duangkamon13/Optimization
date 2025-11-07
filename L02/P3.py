
def survive_mars(area , depth):
    soil_volume = area * depth 
    total_water = soil_volume *40 /100
    return total_water

w = survive_mars(126, 30)
print('water', w, 'L')
w = survive_mars(150, 40)
print('water', w, 'L')
w = survive_mars(100, 35)
print('water', w, 'L')