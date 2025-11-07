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


import random

def hill_climbing(items, budget):

    shuffled_items = random.sample(items, len(items))
    current_solution = []
    current_cost = 0
    for item in shuffled_items:
        if current_cost + item['price'] <= budget:
            current_solution.append(item)
            current_cost += item['price']
            
    current_calories = sum(item['calories'] for item in current_solution)
    
    
    while True:
        improved = False 
        neighbor_solution = list(current_solution)
        
        if neighbor_solution:
            item_to_remove = random.choice(neighbor_solution)
            neighbor_solution.remove(item_to_remove)
        
        unused_items = [item for item in items if item not in neighbor_solution]
        random.shuffle(unused_items)
        
        temp_cost = sum(item['price'] for item in neighbor_solution)
        for item_to_add in unused_items:
            if temp_cost + item_to_add['price'] <= budget:
                neighbor_solution.append(item_to_add)
                temp_cost += item_to_add['price']

        neighbor_calories = sum(item['calories'] for item in neighbor_solution)
        
      
        if neighbor_calories > current_calories:
            current_solution = neighbor_solution
            current_calories = neighbor_calories
            improved = True 

       
        if not improved:
            break
            
    # 3. สรุปผล
    final_cost = sum(item['price'] for item in current_solution)
    return current_solution, final_cost, current_calories

if __name__ == "__main__":
    BUDGET = 20
    print(f"Hill Climbing")
    hc_result, hc_cost, hc_calories = hill_climbing(market_data, BUDGET)

    print(f"งบประมาณ: {BUDGET} บาท ")
    print(f"แคลอรีรวม: {hc_calories} Kcal และใช้เงิน {hc_cost} บาท")
    print(f" ")
    
    sorted_result = sorted(hc_result, key=lambda x: x['price'], reverse=True)
    for item in sorted_result:
        print(f"    - {item['name']} ({item['price']} บาท, {item['calories']} Kcal)")
        
    print("\n------------------------------------------------------")