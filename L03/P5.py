"""
Write a function named mighty_river to take in an argument:
a dictionary of river information (having a key being a river name
and a value being a list of cross-section area, water density,
and flow rate), calculate the estimated power,
and return the result in another dictionary using
a river name as key and calculated power as a value.
Note:
    P = 0.5 * rho * Q^3 / A^2
    argument = {'river name': [A, rho, Q],...}
"""

def mighty_river(rivers):

    P_kinetic = {}
    # Write your code here
    for river_name, info in rivers.items():
        A = info[0]  
        rho = info[1]  
        Q = info[2]  
        power = 0.5 * rho * Q * (Q / A)**2
        P_kinetic[river_name] = power
    return P_kinetic

if __name__ == '__main__':
                # name  : [A (m^2), rho (kg/m^3),  Q (m^3/s)]
    mighties = {'Amazon': [1.2e6, 1100, 210000],
                'Congo':  [2e6, 1150, 41200],
                'Yangtze': [800e3, 1200, 30000]}

    river_power = mighty_river(mighties)
    print(river_power)
