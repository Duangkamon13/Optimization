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

def greedy(items, budget):

    items_with_ratio = []
    for item in items:
        ratio = item['calories'] / item['price'] if item['price'] > 0 else float('inf')
        items_with_ratio.append({**item, 'ratio': ratio})


    sorted_items = sorted(items_with_ratio, key=lambda x: x['ratio'], reverse=True)
    


    knapsack = []
    total_cost = 0
    total_calories = 0

    for item in sorted_items:
        if total_cost + item['price'] <= budget:
            knapsack.append(item)
            total_cost += item['price']
            total_calories += item['calories']
            
    # 4. คืนค่าตะกร้าที่จัดได้
    return knapsack, total_cost, total_calories


# --- 3. ส่วนเรียกใช้งานและแสดงผล ---
if __name__ == "__main__":
    BUDGET = 20
 
    print(f"Greedy Algorithm")
    hc_result, hc_cost, hc_calories = greedy(market_data, BUDGET)

    print(f"งบประมาณ: {BUDGET} บาท ")
    print(f"แคลอรีรวม: {hc_calories} Kcal และใช้เงิน {hc_cost} บาท")
    print(f" ")
    
    sorted_result = sorted(hc_result, key=lambda x: x['price'], reverse=True)
    for item in sorted_result:
        print(f"    - {item['name']} ({item['price']} บาท, {item['calories']} Kcal)")
        
    print("\n------------------------------------------------------")