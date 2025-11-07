def star_lagtime(light_speed, name, distance_km):
    """
    :param light_speed: m/s
    :param name: string, name of celestial object
    :param distance_km: km
    :return: time in seconds (float)
    """
    distance_m = distance_km * 1000
    t = distance_m / light_speed

    print(name)
    return t

if __name__ == '__main__':
    t = star_lagtime(299792458, "sun", 149.6e6)
    print(t)
    print("{:,.2f} s = {:,.2f} min.".format(t, t/60))

