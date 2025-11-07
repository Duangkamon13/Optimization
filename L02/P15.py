
import math
def earthquake(events):
    result = []
    for event in events:
        text = event[0]
        magnitude = event[1]

        # คำนวณค่าล็อก
        log_energy = 4.8 + 1.5 * magnitude

        # แปลงกลับ
        energy = 10 ** log_energy

        # เพิ่มรายการ
        result.append([text, magnitude, energy])

    return result

events = [['2019 02 22 Ecuador', 7.5],
['2018 08 19 Fiji', 8.2],
['2017 09 08 Mexico', 8.2]]
res = earthquake(events)
print(res)