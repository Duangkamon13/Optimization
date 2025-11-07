import math
if __name__ == '__main__':
    """
Taewondo Tornado Kick is one of the most exciting move
to watch in martial arts. It takes 360-degree body rotation
and hip thrust to deliver a very powerful kick.
Write a program to calculate force at impact:
ask a user for impact duration t (s),
an effective kicking leg weight m (kg),
an effective kicking leg length r (m),
kick execution time T (s) for full 360 rotation,
calculate impact velocity v (in km/h and mph)
and impact force f (in N and lb f)
and report the calculations.
Note: (1) impact force can be estimated from f = m * v / t;
(2) impact velocity can be estimated from v = omega * r,
where is an angular velocity (rad/s);
(3) kick execution time T = (2 pi)/omega;
(4) 1 mph = 1.61 km/h and 1 lb f = 4.45 N.
"""

t = float(input('Impact duration (s): '))
m = float(input('Effective weight (kg): '))
r = float(input('Effective length (m): '))
T = float(input('Blow execution time (s): '))

# (1) Find angular velocity
omega = 2*math.pi/T

# (2) Find impact velocity
v = omega*r
# (3) Find impact force
f = m*v/t # Dummy
# (4) Convert units
kmh = v*3.6
mph = kmh/ 1.61
lbf = f / 4.45


velocity_report = "v = {:,.2f} km/h = {:,.2f} mph"
force_report = "f = {:,.2f} N = {:,.2f} lbf"

print(velocity_report.format(kmh, mph))
print(force_report.format(f, lbf))