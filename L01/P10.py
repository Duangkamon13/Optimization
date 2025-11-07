"""
Write a program to calculate an annual water requirement for crop production.
The program takes 4 inputs: (1) a name of the crop,
(2) an average water usage per rai of the given crop in litre,
(3) an area planting the crop in rai,
(4) annual crop yield in kg/rai,
and (5) crop price in baht/kg.
Then, calculate the following figures and print out:
* total water usage (in L)
* total crop yield (in kg)
* total earning (in baht)
* average crop yield per water usage (in kg/L)
* average earning per water usage (in baht/L)
* average earning per area (in baht/rai)

Crop: water usage L/rai;   annual crop yield kg/rai;   crop wholesale price baht/kg; total area
Rice:
    Raw: water: 3000L/kg; water height 0.2 m = 0.2 x 1600 sq. m = 800 cu. m/rai =  800 kL/rai
    yield: 500-800 kg per rai; price: 10,500 baht/ton; total growing area: 56 M rai
    (1ha = 10000 sq. m. = 6 rai 1 ngan; 1 ton = 1000kg)
    
    * water: 800 kL/rai; yield: 700 kg/rai; price: 10.5 baht/kg; total area: 56 M rai

Corn:
    Raw: water: 60 Gallon/1 pound; water: 594,000 gallons of water/acre;
    annual yield: 174.6 bushels per acre; 2150 kg/rai
    wholesale w/o husking 12 baht/kg
    total area: 230000 rai
    (1 Gallon = 3.7854L; 2.2 pound = 1 kg; 1 bushel = 35.2 L; 1 acre = 2.53 rai)

    * water: 891 kL/rai; yield: 2150 kg/rai; price: 12 baht/kg; total area: 230 k rai

Sugarcane:
    water consumption ~ 2400 kL/rai
    nation-wide growing area: ~11 M rai
    total production ~ 92,950,098 ton
     --> yield: production/area = 8450 kg/rai
    wholesale price: ~ 1000 baht/ton = ~ 1000 baht/1000kg @ 10 c.c.s.

    * water: 2400 kL/rai; yield: 8450 kg/rai; price: 1 baht/kg; total area: 11 M rai

Para Rubber:

"""

def crop_econ(water, area, annual_yield, price):
    '''
    param:
    water: water usage in L/rai
    area: total growing area in rai
    annual_yield: annual crop yield in kg/rai
    price: average crop price in baht/kg

    return:
    total_water: total water usage in L
    total_yield: total crop yield in kg
    total_earning: total earning in baht
    ypw: average crop yield per water usage in kg/L
    epw: average earning per water usage in baht/L
    epa: average earning per area in baht/rai 
    '''

    ## Do not change anything above this line.
    ## ----------------------------------------

    total_water = water_usage * growing_area
    total_yield = growing_area * ypa
    total_earning = total_yield * wholesale_price
    ypw = total_yield / total_water
    epw = total_earning / total_water
    epa = total_earning / growing_area

    # Fill in your code to have total_water, total_yield, total_earning, ypw, epw, epa the correct values.




    ## Do not change anything below this line.
    ## ----------------------------------------

    return total_water, total_yield, total_earning, ypw, epw, epa



if __name__ == '__main__':

    # Name of the crop
    crop_name = input('Crop:')

    water_usage = float(input('Estimated annual water consumption (L/rai):'))
    growing_area = float(input('Nation-wide growing area (rai):'))
    ypa = float(input('Average crop yield per growing area (kg/rai):'))
    wholesale_price = float(input('Estimated wholesale price (baht/kg):'))

    W, Y, E, YPW, EPW, EPA = crop_econ(water_usage, growing_area,
                                       ypa, wholesale_price)

    print()
    print(crop_name.upper(), 'over {:,.0f} rai'.format(growing_area))
    print('Total water usage: {:,.2f} ML'.format(W/1e6))
    print('Total crop yield: {:,.2f} kg or {:,.2f} ton'.format(Y, Y/1000))
    print('Total earning: {:,.2f} mil. baht'.format(E/1e6))
    print('Average crop yield per water usage: {:,.6f} kg/L'.format(YPW))
    print('Average earning per water usage: {:,.6f} baht/L'.format(EPW))
    print('Average earning per area: {:,.2f} baht/rai'.format(EPA))

    


