import math

def Hipparchus(do_km, theta_m_deg):
    # คำนวณระยะถึงดวงจันทร์
    Dm = do_km / (2 * math.tan(math.radians(90 - theta_m_deg)))
    
    # คำนวณเมื่อมุมผิดพลาด ± 0.01°
    Dm_low = do_km / (2 * math.tan(math.radians(90 - (theta_m_deg - 0.01))))
    Dm_high = do_km / (2 * math.tan(math.radians(90 - (theta_m_deg + 0.01))))
    
    # จัดลำดับจากน้อยไปมาก
    Dml, Dmu = sorted([Dm_low, Dm_high])
    
    return (Dm, Dml, Dmu)

def Aristarchus(dm_km, theta_s_deg):
    # คำนวณระยะถึงดวงอาทิตย์
    Ds = dm_km / math.tan(math.radians(theta_s_deg))
    
    # คำนวณเมื่อมุมผิดพลาด ± 0.01°
    Ds_low = dm_km / math.tan(math.radians(theta_s_deg - 0.01))
    Ds_high = dm_km / math.tan(math.radians(theta_s_deg + 0.01))
    
    # จัดลำดับจากน้อยไปมาก
    Dsl, Dsu = sorted([Ds_low, Ds_high])
    
    return (Ds, Dsl, Dsu)

# ทดสอบตามตัวอย่าง

if __name__ == '__main__':
    res = Hipparchus(400, 89.97)
    print('Hipparchus:{:,.2f} km; [{:.0f} , {:.0f}] if 0.01 deg off'.format(*res))
    
    res = Aristarchus(381972, 0.15)
    print('Aristarchus: {:,.2f} km; [{:.0f} , {:.0f}] if 0.01 deg off'.format(*res))
