def tennis_service(ball_speed, court_length, ball_weight):
    '''
    param:
    ball_speed: top (or final) ball speed in km/h
    court_length: court length in m
    ball_weight: ball weight in g
    return:
    time: time to reach the other end of the court
    Ej:   energy in joules
    Ecal: energy in calories
    '''

    # (0) Convert speed and weight to SI units
    v_ms = ball_speed/ 3.6
    mass_kg = ball_weight / 1000

    # 1) time
    time =court_length*2/ v_ms

    # 2) acceleration
    a = v_ms / time  # assuming initial speed = 0

    # 3) force
    f = mass_kg * a

    # 4) energy
    EJ = f * court_length

    # 5) cal
    Ecal = EJ / 4.184

    return time, EJ, Ecal


# [!!! Mark 2 !!!]
# Do not edit below this line.
# ------------------------------------------------

if __name__ == '__main__':
    print('Time = %.4f s. Energy = %.2f J = %.2f cal'%tennis_service(
        int(input('Enter the ball speed (km/h):')),
        float(input('Enter the court length (m):')),
        float(input('Enter the ball weight (g):'))))