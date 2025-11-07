"""
A flying of an aircraft can be simply explained through 4 forces:
lift, weight, thrust, and drag. Lift is a force pushing an aircraft up
against weight. Write a program to estimate a power to fly a plane:
ask a user to input (1) drag coefficient CD, (2) lift coefficient CL,
(3) air density rho, (4)  plane cross-section area A, (5) wing area S,
and (6) plane weight m, then calculate speed v to sustain the flight altitude
and power required to fly in such a condition and report it.
Note: (1) power = thrust * v; (2) thrust ~= drag (at constant speed);
(3) drag = CD (0.5 rho v^2) A; (4) at constant flight altitude
lift = weight; (5) weight = m g and g = 9.8 m/s^2;
and (6) lift = CL (0.5 rho v^2) S.
"""

import math

CD = float(input('CD: '))
CL = float(input('CL: '))
rho = float(input('air density: '))
A = float(input('cross-section area: '))
S = float(input('wing area: '))
m = float(input('plane weight: '))

#(1) find v from lift = weight: CL (0.5 rho v^2) S = m g;
g = 9.8 # m/s^2

v = math.sqrt((2 * m * g) / (CL * rho * S))
#(2) find drag: drag = CD (0.5 rho v^2) A;
drag = CD * 0.5 * rho * v**2 * A
#(3) find thrust: thrush = drag;
thrust = drag
#(4) find power: power = thrust * v.
power = thrust * v

hp = power * 0.00136

report = "power = {:,.2f} W. = {:,.2f} hp."
print(report.format(power, hp))