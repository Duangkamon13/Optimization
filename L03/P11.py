from mama_turtle import road, find_pol
import math

def brunelleschi_lamp(vx, vy, x, y, height, d, logfile='log.txt'):
    '''
    :param vx, vy: vanishing point coordinate
    :param x, y: reference lamp coordinate
    :param height: reference lamp height
    :param d: distance from ref to the lamp under question
                in direction toward the vanishing point
    '''

    # 1. หา L และ alpha ระหว่าง reference lamp กับ vanishing point
    L, alpha = find_pol(x, y, vx, vy)

    # 2. beta = π - alpha
    beta = math.pi - alpha

    # 3. H และ tau
    H = (L - d) * math.sin(beta)
    tau = (L - d) * math.cos(beta)

    # 4. หา phi จาก top ของ reference lamp
    _, theta = find_pol(x, y + height, vx, vy)
    phi = math.pi - theta

    # 5. คำนวณ h'
    hprime = H - tau * math.tan(phi)

    # Log ข้อมูล
    inp_msg = "Input: vx={:.2f}, vy={:.2f}, x={:.2f}, y={:.2f}, " + \
              "height={:.2f}, d={:.2f}.\n"
    inp_msg = inp_msg.format(vx, vy, x, y, height, d)

    calc_msg = "Calc: L = {:.2f}, beta = {:.2f}, " + \
        "H = {:.2f}, tau = {:.2f}, phi = {:.2f}, " + \
        "h' = {:.2f}.\n"
    calc_msg = calc_msg.format(L, beta, H, tau, phi, hprime)

    with open(logfile, 'a') as f:
        f.write(inp_msg)
        f.write(calc_msg)

    return hprime

if __name__ == '__main__':
    r = road()
    r.draw_road()
    r.draw_lamp_posts(brunelleschi_lamp)
    input('enter to exit')
