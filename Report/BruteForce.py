import itertools

# --- 1. ข้อมูล (Dataset) ---
market_data = [
    {'name': 'ข้าวผัด', 'category': 'อาหารหลัก', 'price': 50, 'calories': 550},
    {'name': 'ผัดไทย', 'category': 'อาหารหลัก', 'price': 60, 'calories': 600},
    {'name': 'คอหมูย่าง', 'category': 'อาหารหลัก', 'price': 100, 'calories': 500},
    {'name': 'ส้มตำ', 'category': 'อาหารหลัก', 'price': 50, 'calories': 120},
    {'name': 'ข้าวเหนียว', 'category': 'อาหารหลัก', 'price': 10, 'calories': 150},
    {'name': 'ไก่ทอด', 'category': 'ของทานเล่น', 'price': 25, 'calories': 280},
    {'name': 'ลูกชิ้นปิ้ง', 'category': 'ของทานเล่น', 'price': 20, 'calories': 200},
    {'name': 'ไส้กรอกอีสาน', 'category': 'ของทานเล่น', 'price': 15, 'calories': 180},
    {'name': 'หนังไก่ทอด', 'category': 'ของทานเล่น', 'price': 30, 'calories': 400},
    {'name': 'เครปญี่ปุ่น', 'category': 'ของทานเล่น', 'price': 40, 'calories': 350},
    {'name': 'ขนมเบื้อง', 'category': 'ของหวาน', 'price': 30, 'calories': 250},
    {'name': 'ข้าวเหนียวมะม่วง', 'category': 'ของหวาน', 'price': 80, 'calories': 450},
    {'name': 'ไอศกรีมกะทิ', 'category': 'ของหวาน', 'price': 25, 'calories': 220},
    {'name': 'ชาไทย', 'category': 'เครื่องดื่ม', 'price': 30, 'calories': 250},
    {'name': 'น้ำอัดลม', 'category': 'เครื่องดื่ม', 'price': 20, 'calories': 180},
    {'name': 'น้ำเปล่า', 'category': 'เครื่องดื่ม', 'price': 10, 'calories': 0},
]


def exhaustive(items, budget):
    best_combination = []
    max_calories = 0
    best_cost = 0

    for i in range(1, len(items) + 1):
        for combo in itertools.combinations(items, i):


            current_cost = sum(item['price'] for item in combo)
            current_calories = sum(item['calories'] for item in combo)
            if current_cost <= budget and current_calories > max_calories:
                max_calories = current_calories
                best_combination = list(combo)
                best_cost = current_cost
    
    return best_combination, best_cost, max_calories

if __name__ == "__main__":
    BUDGET = 234
    print(f"Exhaustive Search")
    hc_result, hc_cost, hc_calories = exhaustive(market_data, BUDGET)

    print(f"งบประมาณ: {BUDGET} บาท ")
    print(f"แคลอรีรวม: {hc_calories} Kcal และใช้เงิน {hc_cost} บาท")
    print(f" ")
    
    sorted_result = sorted(hc_result, key=lambda x: x['price'], reverse=True)
    for item in sorted_result:
        print(f"    - {item['name']} ({item['price']} บาท, {item['calories']} Kcal)")
        
    print("\n------------------------------------------------------")