import bisect  # นำเข้าไลบรารีสำหรับ "การแทรกแบบเรียงลำดับ" (sorted insertion)
import math    # นำเข้าไลบรารีคณิตศาสตร์ (สำหรับฟังก์ชัน h)

# --- (อ้างอิงจากเซลล์ 11 หรือ 53 ใน Notebook) ---
# นี่คือคลาส "คิวจัดลำดับความสำคัญ"
# มันจะเก็บโหนด (Node) และจะส่งโหนดที่ "ดีที่สุด" (cost ต่ำสุด) ออกมาก่อนเสมอ
class PriorityQueue:
    def __init__(self, order=min, f=lambda x: x):
        self.A = [] # Queue
        self.order = order
        self.f = f

    def append(self, item):
        """
        It appends the item into a proper position in the sorted queue.
        """
        bisect.insort(self.A, (self.f(item), item))

    def __len__(self):
        return len(self.A)

    def pop(self):
        if self.order == min:
            return self.A.pop(0)[1]
        else:
            return self.A.pop()[1]
            
    def extend(self, items):
        for item in items: self.append(item)
            
    def is_empty(self):
        return self.__len__() == 0
    
# --- (อ้างอิงจากเซลล์ 37 ใน Notebook) ---
infinity = 1.0e400

# คลาส "นิยามปัญหา" เวอร์ชันอัปเกรดสำหรับ P3
class RoutingProblem:
    "The problem of searching a graph from one node to another."
    def __init__(self, local_map, initial, goal):
        self.map = local_map
        self.initial = initial
        self.goal = goal

    def successor(self, s):
        "Return a list of (action, result/linked town) pairs."
        options = []
        # (เพิ่มการตรวจสอบ) เพื่อความปลอดภัย ถ้าเมืองนั้นไม่มี transit
        if s in self.map['transit']:
            for town in self.map['transit'][s].keys():
                road = s + ' - ' + town # สร้าง "action" (ชื่อถนน)
                options.append( (road, town) )
        return options

    # นี่คือเมธอดที่ "สำคัญ" สำหรับ P3 (UCS)
    def path_cost(self, cost_to_s, s, action, snext):
        """คำนวณ "ระยะทางรวม" (cost) ที่ใช้ในการเดินทางมาถึง 'snext'
        cost_to_s = ระยะทางที่ใช้มาถึงเมืองปัจจุบัน (s)
        snext = เมืองถัดไป
        """
        transit_cost = infinity # ค่าเริ่มต้น (เผื่อหาไม่เจอ)
        if s in self.map["transit"]:
            if snext in self.map["transit"][s]:
                # ดึง "ระยะทาง" (cost) ของถนนเส้นนั้นจากแผนที่
                transit_cost = self.map["transit"][s][snext]
        # คืนค่า = ระยะทางที่ผ่านมา + ระยะทางของก้าวใหม่
        return cost_to_s + transit_cost

    def goal_test(self, state):
        return state == self.goal

    def h(self, state):
        # ฟังก์ชัน h (heuristic) สำหรับ A* Search
        # (เราไม่ได้ใช้ใน P3 แต่มีไว้ในคลาสเผื่ออนาคต)
        cx, cy = self.map["location"][state]
        gx, gy = self.map["location"][self.goal]
        return math.sqrt( (cx - gx)**2 + (cy - gy)**2 )

# --- (อ้างอิงจากเซลล์ 40 ใน Notebook) ---
# คลาส "โหนด" เวอร์ชันอัปเกรดสำหรับ P3
class Node:
    """นี่คือ "โหนด" หรือ "รอยเท้า" ที่ใช้ในการค้นหา
    มันจะเก็บว่ามาถึงเมืองไหน (state), มาจากใคร (parent),
    และที่สำคัญคือ "ใช้ระยะทางรวมมาเท่าไหร่" (path_cost)
    """
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state      # ชื่อเมืองปัจจุบัน (เช่น 'Sibiu')
        self.parent = parent    # "โหนดพ่อ" (Node object ของ 'Arad')
        self.action = action    # "action" ที่ใช้ (เช่น 'Arad - Sibiu')
        self.path_cost = path_cost # "ระยะทางรวม" (g) ที่ใช้จาก start มาถึงโหนดนี้
        
        self.depth = 0
        if parent is not None: 
            self.depth = parent.depth + 1
                    
    def path(self):
        "เมธอดสำหรับ 'ย้อนรอย' กลับไปหาจุดเริ่มต้น"
        x, result = self, [self] # เริ่มจากโหนดปัจจุบัน
        while x.parent is not None:
            result.append(x.parent) # ย้อนไปหาพ่อ
            x = x.parent            # อัปเดตตัวย้อนรอย
        return result

    def expand(self, problem):
        "สร้าง 'โหนดลูก' (เมืองถัดไป) ทั้งหมด"
        nexts = []
        # เรียก successor จาก 'problem' เพื่อหาว่าไปไหนได้บ้าง
        for (action, next_state) in problem.successor(self.state):
            # สร้าง "โหนดลูก" ใหม่
            nexts.append(Node(next_state,  # เมืองถัดไป
                         self,         # บอกว่า "ฉัน" (self) คือพ่อ
                         action,       # action ที่ใช้
                         # คำนวณ "ระยะทางรวม" ใหม่
                         problem.path_cost(self.path_cost, self.state, action, next_state)))
        return nexts

# --- ฟังก์ชันหลักสำหรับ P3 ---
def P3_route(map_fname, start, goal):
    
    # --- ส่วนที่ 1: การอ่านและแปลข้อมูลไฟล์ (File Parsing) ---
    # (ส่วนนี้เหมือนกับ P2 ครับ)
    locations = {}
    transits = {}
    
    try:
        with open(map_fname, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or ':' not in line:
                    continue
                
                parts = line.split(';')
                main_part = parts[0].strip()
                
                town_name, coords_str = main_part.split(':')
                town_name = town_name.strip()
                x_str, y_str = coords_str.split(',')
                locations[town_name] = (int(x_str.strip()), int(y_str.strip()))
                
                transits[town_name] = {} 
                if len(parts) > 1 and parts[1].strip():
                    neighbors_list = parts[1].strip().split(',')
                    for neighbor_data in neighbors_list:
                        if ':' in neighbor_data:
                            neighbor_name, dist_str = neighbor_data.split(':')
                            transits[town_name][neighbor_name.strip()] = int(dist_str.strip())

    except FileNotFoundError:
        return f"Error: Map file '{map_fname}' not found."
    except Exception as e:
        return f"Error parsing map file: {e}"

    romania_map = {"location": locations, "transit": transits}
    # --- (จบส่วน File Parsing) ---

    
    # --- ส่วนที่ 2: Uniform-Cost Search (UCS) ---
    # (ตรรกะนี้อ้างอิงจาก 'best_first_search' (เซลล์ 55)
    #  และ 'uniform_cost_search' (เซลล์ 63) ใน Notebook)
    
    # สร้าง "โจทย์" (ใช้คลาส RoutingProblem)
    problem = RoutingProblem(romania_map, start, goal)
    
    # "ฟังก์ชันให้คะแนน" (fee) สำหรับ UCS
    # เราบอกว่า "คะแนน" ที่จะใช้จัดลำดับในคิว คือ "ระยะทางรวม" (path_cost)
    def fee(node):
        return node.path_cost

    # สร้าง "คิวจัดลำดับความสำคัญ" (PriorityQueue)
    # โดยใช้ 'min' (ค่าน้อยสุดก่อน) และ 'fee' (ฟังก์ชันคะแนน)
    fringe = PriorityQueue(min, fee)
    fringe.append(Node(problem.initial)) # ใส่โหนดเริ่มต้น (cost=0)
    
    # 'reached' (หรือ 'visited')
    # ใน UCS, มันทำ 2 หน้าที่:
    # 1. ป้องกันการวนลูป (Cycle)
    # 2. เก็บ "ระยะทางที่ดีที่สุด" (Shortest path) ที่เราเคยเจอสำหรับเมืองนั้นๆ
    reached = {} 

    while len(fringe) > 0:
        
        # .pop() จะดึงโหนดที่ "ระยะทาง (cost) น้อยที่สุด" ออกมาเสมอ
        node = fringe.pop()

        # ตรวจสอบว่าถึงเป้าหมายหรือยัง
        if problem.goal_test(node.state):
            # ถ้าใช่, สร้างเส้นทาง
            path_nodes = node.path()
            path_nodes.reverse()
            path_names = [n.state for n in path_nodes]
            # คืนค่าเส้นทางที่สั้นที่สุดที่เจอ
            return " - ".join(path_names) 

        # --- นี่คือหัวใจของ UCS ---
        # "ถ้าเมืองนี้ (node.state) ยังไม่เคยเจอ (not in reached)"
        # "หรือ (OR) ถ้าเส้นทางใหม่ที่มาเมืองนี้ 'สั้นกว่า' (cost น้อยกว่า) เส้นทางเก่าที่เคยบันทึกไว้"
        if (node.state not in reached) or (node.path_cost < reached[node.state].path_cost):
            
            # "ให้อัปเดต 'reached' ว่านี่คือเส้นทางที่ดีที่สุดที่เราเจอสำหรับเมืองนี้"
            reached[node.state] = node
            # "แล้วค่อยขยายเส้นทาง (หาลูกๆ) และเพิ่มลูกๆ เข้าไปในคิว"
            # (คิวจะจัดเรียงลูกๆ เหล่านี้ตาม cost ให้อัตโนมัติ)
            fringe.extend(node.expand(problem))

    # ถ้าคิวว่าง (while loop จบ) แต่ยังไม่เจอเป้าหมาย
    return "No route found."

# 5. ส่วนสำหรับรัน (ถ้าไฟล์นี้ถูกรันโดยตรง)
if __name__ == '__main__':
    # เราจะใช้ 'P2romania.txt' ตามที่โจทย์ P3 กำหนด
    r = P3_route('P2romania.txt', 'Arad', 'Bucharest')
    print(r)