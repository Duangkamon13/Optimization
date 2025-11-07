import itertools
import random

# --- 1. ข้อมูล (Dataset) ---
# ชุดข้อมูล "ตลาดโต้รุ่ง" ที่เราออกแบบไว้
market_data = [
    # อาหารจานหลัก
    {'name': 'ข้าวผัด', 'category': 'อาหารหลัก', 'price': 50, 'calories': 550},
    {'name': 'ผัดไทย', 'category': 'อาหารหลัก', 'price': 60, 'calories': 600},
    {'name': 'คอหมูย่าง', 'category': 'อาหารหลัก', 'price': 100, 'calories': 500},
    {'name': 'ส้มตำ', 'category': 'อาหารหลัก', 'price': 50, 'calories': 120},
    {'name': 'ข้าวเหนียว', 'category': 'อาหารหลัก', 'price': 10, 'calories': 150},
    # ของทานเล่น / เสียบไม้
    {'name': 'ไก่ทอด', 'category': 'ของทานเล่น', 'price': 25, 'calories': 280},
    {'name': 'ลูกชิ้นปิ้ง', 'category': 'ของทานเล่น', 'price': 20, 'calories': 200},
    {'name': 'ไส้กรอกอีสาน', 'category': 'ของทานเล่น', 'price': 15, 'calories': 180},
    {'name': 'หนังไก่ทอด', 'category': 'ของทานเล่น', 'price': 30, 'calories': 400},
    {'name': 'เครปญี่ปุ่น', 'category': 'ของทานเล่น', 'price': 40, 'calories': 350},
    # ของหวาน
    {'name': 'ขนมเบื้อง', 'category': 'ของหวาน', 'price': 30, 'calories': 250},
    {'name': 'ข้าวเหนียวมะม่วง', 'category': 'ของหวาน', 'price': 80, 'calories': 450},
    {'name': 'ไอศกรีมกะทิ', 'category': 'ของหวาน', 'price': 25, 'calories': 220},
    # เครื่องดื่ม
    {'name': 'ชาไทย', 'category': 'เครื่องดื่ม', 'price': 30, 'calories': 250},
    {'name': 'น้ำอัดลม', 'category': 'เครื่องดื่ม', 'price': 20, 'calories': 180},
    {'name': 'น้ำเปล่า', 'category': 'เครื่องดื่ม', 'price': 10, 'calories': 0},
]


# --- 2. อัลกอริทึมที่ 1: Greedy Algorithm (Heuristic Search) ---
def greedy_knapsack(items, budget):
    """เลือกของที่ 'คุ้มค่า' (แคลอรีต่อบาท) ที่สุดก่อนเสมอ"""
    # คำนวณความคุ้มค่าและเรียงลำดับจากมากไปน้อย
    items_with_ratio = []
    for item in items:
        # ป้องกันการหารด้วยศูนย์ถ้ามีของฟรี
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
            
    return knapsack, total_cost, total_calories

# --- 3. อัลกอริทึมที่ 2: Exhaustive Search (Brute-force) ---
def exhaustive_knapsack(items, budget):
    """ลองสร้างชุดอาหารที่เป็นไปได้ทุกรูปแบบ แล้วเลือกชุดที่ดีที่สุด"""
    best_combination = []
    max_calories = 0
    best_cost = 0

    # สร้างชุดค่าผสมตั้งแต่ 1 ชิ้น ไปจนถึงทุกชิ้น
    for i in range(1, len(items) + 1):
        for combo in itertools.combinations(items, i):
            current_cost = sum(item['price'] for item in combo)
            current_calories = sum(item['calories'] for item in combo)
            
            # ถ้าชุดนี้อยู่ในงบ และให้แคลอรีสูงกว่าที่เคยเจอ ให้บันทึกไว้
            if current_cost <= budget and current_calories > max_calories:
                max_calories = current_calories
                best_combination = list(combo)
                best_cost = current_cost
    
    return best_combination, best_cost, max_calories

# --- 4. อัลกอริทึมที่ 3: Hill Climbing (Local Search) ---
def hill_climbing_knapsack(items, budget, max_iterations=1000):
    """เริ่มต้นจากคำตอบสุ่ม แล้วค่อยๆ ปรับปรุงให้ดีขึ้น"""
    
    # 1. สร้างคำตอบเริ่มต้นแบบสุ่ม (แต่ค่อนข้างดี)
    shuffled_items = random.sample(items, len(items))
    current_solution = []
    current_cost = 0
    current_calories = 0
    for item in shuffled_items:
        if current_cost + item['price'] <= budget:
            current_solution.append(item)
            current_cost += item['price']
            current_calories += item['calories']
            
    # 2. เริ่มการวนลูปเพื่อปรับปรุง
    for _ in range(max_iterations):
        # สร้าง "เพื่อนบ้าน" โดยการลองสลับของ 1 ชิ้น
        neighbor_solution = list(current_solution)
        
        # ถ้าตะกร้าไม่ว่าง ให้ลองเอาของออก 1 ชิ้น
        if neighbor_solution:
            item_to_remove = random.choice(neighbor_solution)
            neighbor_solution.remove(item_to_remove)
        
        # หาของที่ยังไม่ได้เลือก
        unused_items = [item for item in items if item not in neighbor_solution]
        random.shuffle(unused_items)
        
        # ลองเอาของชิ้นใหม่ใส่เข้าไปแทน
        temp_cost = sum(item['price'] for item in neighbor_solution)
        for item_to_add in unused_items:
            if temp_cost + item_to_add['price'] <= budget:
                neighbor_solution.append(item_to_add)
                temp_cost += item_to_add['price']

        # 3. เปรียบเทียบ
        neighbor_calories = sum(item['calories'] for item in neighbor_solution)
        if neighbor_calories > current_calories:
            current_solution = neighbor_solution
            current_calories = neighbor_calories
    
    final_cost = sum(item['price'] for item in current_solution)
    return current_solution, final_cost, current_calories


# --- 5. ส่วนเรียกใช้งานและแสดงผล ---
if __name__ == "__main__":
    BUDGET = 200  # ใช้งบ 100 บาท

    print(f"--- 🛒 ตลาดโต้รุ่ง (งบประมาณ: {BUDGET} บาท) ---")
    
    # --- Greedy Search ---
    print("\n--- 💡 1. Greedy Algorithm (เลือกของคุ้มค่าที่สุดก่อน) ---")
    greedy_result, greedy_cost, greedy_calories = greedy_knapsack(market_data, BUDGET)
    print(f"  > ได้แคลอรีรวม: {greedy_calories} Kcal (ใช้เงิน {greedy_cost} บาท)")
    for item in greedy_result:
        print(f"    - {item['name']}")

    # --- Exhaustive Search ---
    print("\n--- 🧠 2. Exhaustive Search (หาทุกทางที่เป็นไปได้) ---")
    # หมายเหตุ: ถ้า market_data มีมากกว่า 20 รายการ อาจจะทำงานช้ามาก
    ex_result, ex_cost, ex_calories = exhaustive_knapsack(market_data, BUDGET)
    print(f"  > ได้แคลอรีรวม: {ex_calories} Kcal (ใช้เงิน {ex_cost} บาท) ✨ นี่คือคำตอบที่ดีที่สุด! ✨")
    for item in ex_result:
        print(f"    - {item['name']}")

    # --- Hill Climbing ---
    print("\n--- ⛰️ 3. Hill Climbing (เริ่มจากสุ่มแล้วปรับปรุง) ---")
    # เนื่องจากมีการสุ่ม ผลลัพธ์อาจเปลี่ยนแปลงเล็กน้อยในแต่ละครั้งที่รัน
    hc_result, hc_cost, hc_calories = hill_climbing_knapsack(market_data, BUDGET)
    print(f"  > ได้แคลอรีรวม: {hc_calories} Kcal (ใช้เงิน {hc_cost} บาท)")
    for item in hc_result:
        print(f"    - {item['name']}")
        
    print("\n------------------------------------------------------")