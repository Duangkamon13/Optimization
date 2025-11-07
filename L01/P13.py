"""
Given a mass of an object m kg,
write a program to calculate an energy E
spent to move the object from resting still to speed s m/s
within time t (second).
[Hint: 	acceleration = speed/time;
force = mass * acceleration;
displacement = initial speed + 0.5*acceleration*time**2;
energy = force * displacement.]

"""

import math

def calc_energy(mass, final_speed, time_interval):
    '''
    param:
    mass: an object mass in kg
    final_speed: a final speed of the object in m/s
    time_interval: time interval to move the object from 0 m/s to the final speed

    return:
    E: Energy to do the work in J.
    d: displacement from its starting position in m.
    '''
    initialSpeed = 0
    a = (final_speed - initialSpeed)/time_interval
    f = mass * a
    d = initialSpeed * time_interval + 0.5 *a * time_interval**2
    E = f*d
    # Fill in your code here.



    return E, d

## Do not change anything below this line.
## [!!Marker!!]
## ----------------------------------------

if __name__ == '__main__':

    g = lambda f: f(float(input('object mass:')),
                    float(input('target speed:')),
                    float(input('time spent:')))
    print("Energy = %.2f J. Distance = %.2f m."%g(calc_energy))




