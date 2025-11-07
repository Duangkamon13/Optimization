"""
Given a rain density in mm/h and an area in rai,
write a program to calculate the amount of rain water in L.
The program, named rain_water, takes 3 arguments:
an area of the field (in rai, as a number either in integer or float),
a rain density (in mm/h, as a floating-point number),
and a number of raining hours.
Then, calculate the amount of water and return it.
"""

# Do not edit above this line.
# ------------------------------------------------


# ... Your function will be here

def rain_water(area_rai, rain_density_mm_per_h, raining_hours):
    """
    :param:
    * area_rai: float or int, area in rai
    * rain_density_mm_per_h: float, mm/h
    * raining_hours: float, duration in hours
    :return:
    * total rain water in L
    """
    # (1) rai to m²
    area_m2 = area_rai * 1600

    # (2) total rainfall (mm)
    rainfall_mm = rain_density_mm_per_h * raining_hours

    # (3) total rain water in L
    total_water_L = rainfall_mm * area_m2

    return total_water_L


# [!!! Mark 2 !!!]
# Do not edit below this line.
# ------------------------------------------------

if __name__ == '__main__':
    area = input('Area name:')
    print('{}: rain water = {:,.2f} L'.format(area, rain_water(
        float(input('Size of the area (in rai):')),
        float(input('The area rain density (in mm/h):')),
        float(input('The number of raining hours:'))
    )))