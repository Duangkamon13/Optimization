"""
Write a program to take in an angle of the stick shadow in Alexandria and a distance between Alexandria and Aswan (in km) and print out the calculated earth circumference.
The program takes the shadow angle in degree and the distance in km, respectively. It reports the estimated earth circumference in km (rounded to 1 decimal point).
Hint: circumference = 360 * distance / angle.
"""

angle = float(input("Angle (degree): "))
distance = float(input("Distance (km): "))

circumference =360 * distance / angle

report = 'Eratosthenes: "the earth circumference is about {:,.1f} km."'
print(report.format(circumference))