import random

market_data = [
    {'name': 'หม่าล่า', 'category': 'อาหารหลัก', 'price': 100, 'calories': 500},
    {'name': 'ข้าวผัด', 'category': 'อาหารหลัก', 'price': 50, 'calories': 550},
    {'name': 'ผัดไทย', 'category': 'อาหารหลัก', 'price': 60, 'calories': 600},
    {'name': 'คอหมูย่าง', 'category': 'อาหารหลัก', 'price': 100, 'calories': 500},
    {'name': 'ส้มตำ', 'category': 'อาหารหลัก', 'price': 50, 'calories': 120},
    {'name': 'ข้าวเหนียว', 'category': 'อาหารหลัก', 'price': 10, 'calories': 150},
    {'name': 'ไก่ทอด', 'category': 'ของทานเล่น', 'price': 25, 'calories': 280},
    {'name': 'ลูกชิ้นปิ้ง', 'category': 'ของทานเล่น', 'price': 20, 'calories': 200},
    {'name': 'ไส้กรอกอีสาน', 'category': 'ของทานเล่น', 'price': 15, 'calories': 180},
    {'name': 'หนังไก่ทอด', 'category': 'ของทานเล่น', 'price': 30, 'calories': 400},
    {'name': 'เครปญี่ปุ่น', 'category': 'ของทานเล่น', 'price': 45, 'calories': 350},
    {'name': 'ขนมเบื้อง', 'category': 'ของหวาน', 'price': 30, 'calories': 250},
    {'name': 'ข้าวเหนียวมะม่วง', 'category': 'ของหวาน', 'price': 80, 'calories': 450},
    {'name': 'ไอศกรีมกะทิ', 'category': 'ของหวาน', 'price': 25, 'calories': 220},
    {'name': 'ชาไทย', 'category': 'เครื่องดื่ม', 'price': 30, 'calories': 250},
    {'name': 'น้ำอัดลม', 'category': 'เครื่องดื่ม', 'price': 20, 'calories': 180},
    {'name': 'น้ำเปล่า', 'category': 'เครื่องดื่ม', 'price': 10, 'calories': 0},
]

def greedy_select(items, budget, key_func):
    selected = []
    cost = 0
    calories = 0
    for it in sorted(items, key=key_func, reverse=True):
        if cost + it['price'] <= budget:
            selected.append(it)
            cost += it['price']
            calories += it['calories']
    return selected, cost, calories

def greedy_meal_plan(items, budget):
    ratio_key = lambda x: (x['calories'] / (x['price'] + 1e-9))
    sel1, cost1, cal1 = greedy_select(items, budget, ratio_key)
    cal_key = lambda x: x['calories']
    sel2, cost2, cal2 = greedy_select(items, budget, cal_key)

    # เลือกผลที่ให้แคลอรีรวมสูงกว่า (ถ้าเท่ากัน เลือกที่ราคาต่ำกว่า)
    if (cal1, -cost1) >= (cal2, -cost2):
        return "Greedy (cal/baht)", sel1, cost1, cal1
    else:
        return "Greedy (max calories first)", sel2, cost2, cal2

if __name__ == "__main__":
    BUDGET = 50
    algo_name, result, total_cost, total_cal = greedy_meal_plan(market_data, BUDGET)

    print(f"{algo_name}")
    print(f"งบประมาณ: {BUDGET} บาท")
    print(f"แคลอรีรวม: {total_cal} Kcal และใช้เงิน {total_cost} บาท\n")

    for item in sorted(result, key=lambda x: x['price'], reverse=True):
        print(f"  - {item['name']} ({item['price']} บาท, {item['calories']} Kcal)")

    print("\n------------------------------------------------------")
