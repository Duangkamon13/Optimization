"""
Write a function named sweet to take 2 filenames:
one is for a sweetness table and
another one is for sweeteners in a drink.
The function calculates estimated sweetness of the drink
comparable to 10% sucrose solution,
and appends its calculate to the end of the second file
---the drink-sweetener file.
"""

def sweet(fsweet, fdrink):

    # Retrieve sweetness dict
    sweetness = {}

    # อ่านไฟล์ sweetness table
    with open(fsweet, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:  # ข้าม header
            parts = line.strip().split()
            if len(parts) >= 2:
                substance = parts[0]
                sweet_val = float(parts[1])
                sweetness[substance] = sweet_val

    # อ่านไฟล์เครื่องดื่ม
    drink_items = []
    with open(fdrink, 'r') as f:
        for line in f:
            if line.strip() == '':
                continue
            parts = line.strip().split()
            if len(parts) == 2:
                substance = parts[0]
                weight = float(parts[1])
                drink_items.append((substance, weight))

    # คำนวณ weighted sweetness
    sweet_sum = 0
    for substance, weight in drink_items:
        s = sweetness.get(substance, 0)  # ถ้าไม่เจอ substance ให้ใช้ 0
        sweet_sum += weight * s

    # ข้อความที่จะ append
    msg = "\nSweet as {:.1f}% sucrose solution".format(sweet_sum)

  
    with open(fdrink, 'a') as f:
        f.write(msg)

if __name__ == '__main__':
    sweet('sweetness1.txt', 'CocaPanda.txt')