# 1. --- Import ไลบรารีที่จำเป็น ---
from collections import deque

# 2. --- ข้อมูลแผนที่ (จากไฟล์ .ipynb) ---
# เรากำหนดข้อมูลแผนที่ไว้ในระดับ Global เพื่อให้ P1_route เรียกใช้ได้เลย
towns = {
    'Arad': (91, 492), 'Bucharest': (400, 327), 'Craiova': (253, 288),
    'Drobeta': (165, 299), 'Eforie': (562, 293), 'Fagaras': (305, 449),
    'Giurgiu': (375, 270), 'Hirsova': (534, 350), 'Iasi': (473, 506),
    'Lugoj': (165, 379), 'Mehadia': (168, 339), 'Neamt': (406, 537),
    'Oradea': (131, 571), 'Pitesti': (320, 368), 'Rimnicu Vilcea': (233, 410),
    'Sibiu': (207, 457), 'Timisoara': (94, 410), 'Urziceni': (456, 350),
    'Vaslui': (509, 444), 'Zerind': (108, 531)
}

roads = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu': {'Bucharest': 90},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Sibiu': {'Rimnicu Vilcea': 80, 'Arad': 140, 'Oradea': 151, 'Fagaras': 99},
    'Timisoara': {'Lugoj': 111, 'Arad': 118},
    'Urziceni': {'Vaslui': 142, 'Bucharest': 85, 'Hirsova': 98},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Oradea': 71, 'Arad': 75}
}

romania_map = {"location": towns, "transit": roads}

# 3. --- คลาสสำหรับนิยามสถานะ (Node) ---
# (ดัดแปลงจาก StateNode ใน P4.py หรือ Node/Town ใน .ipynb)
class Node:
    """
    คลาสสำหรับจัดเก็บสถานะ (เมือง)
    state: ชื่อเมือง (str)
    parent: โหนดแม่ (Node)
    action: ชื่อถนนที่ใช้มา (str)
    """
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

    def expand(self, problem):
        """ขยายโหนดเพื่อสร้างโหนดลูก (เมืองถัดไป)"""
        return [
            Node(next_state, self, action) 
            for (action, next_state) in problem.successor(self.state)
        ]

    def path(self):
        """
        ย้อนรอยเส้นทางจากโหนดนี้ (เป้าหมาย) กลับไปยังโหนดเริ่มต้น
        คืนค่าเป็นลิสต์ของโหนด [goal, ..., parent, ..., start]
        """
        nodes = []
        node = self
        while node:
            nodes.append(node)
            node = node.parent
        return nodes

# 4. --- คลาสสำหรับนิยาม "กฎของเกม" (Problem) ---
# (นี่คือ SimpleRoutingProblem จาก .ipynb)
class RoutingProblem:
    """
    คลาสสำหรับนิยามปัญหาการค้นหาเส้นทาง
    """
    def __init__(self, local_map, initial, goal):
        self.map = local_map
        self.initial = initial
        self.goal = goal

    def successor(self, current_town):
        """
        สร้างลิสต์ของ (action, next_state) ที่เป็นไปได้
        action คือชื่อถนน, next_state คือเมืองถัดไป
        """
        options = []
        # .get(current_town, {}) เพื่อป้องกัน error ถ้าเมืองนั้นไม่มีถนนเชื่อมต่อ
        for town in self.map['transit'].get(current_town, {}).keys():
            road_name = f"{current_town}-{town}"
            options.append((road_name, town))
        return options

    def goal_test(self, town):
        """ตรวจสอบว่าถึงเป้าหมายหรือยัง"""
        return town == self.goal

# 5. --- "เครื่องมือค้นหา" (Algorithm) ---
# (นี่คือ BFS จาก P4.py)
def breadth_first_search(problem):
    """
    ฟังก์ชันค้นหาแบบ Breadth-First (BFS)
    """
    fringe = deque()  
    explored = set()  # set สำหรับเก็บสถานะ (ชื่อเมือง) ที่เคยสำรวจแล้ว

    # สร้างโหนดเริ่มต้น
    start_node = Node(problem.initial)
    fringe.append(start_node)
    explored.add(start_node.state)

    while fringe:
        # นำโหนดแรกออกจากคิว
        node = fringe.popleft()

        # ตรวจสอบว่าถึงเป้าหมายหรือไม่
        if problem.goal_test(node.state):
            return node  # คืนค่า "โหนด" ที่เป็นเป้าหมาย

        # ขยายโหนด (สร้างโหนดลูก)
        for child in node.expand(problem):
            # ถ้ายังไม่เคยสำรวจเมืองนี้
            if child.state not in explored:
                # เพิ่มเข้า set และคิว
                explored.add(child.state)
                fringe.append(child)
                
    return None  # ไม่พบเส้นทาง

# 6. --- ฟังก์ชันหลักตามโจทย์ (P1_route) ---
def P1_route(start, goal):
    """
    ค้นหาเส้นทางจาก start ไปยัง goal โดยใช้ BFS
    """
    # 1. สร้าง "ปัญหา"
    problem = RoutingProblem(romania_map, start, goal)
    
    # 2. เรียก "เครื่องมือค้นหา"
    solution_node = breadth_first_search(problem)
    
    # 3. แปลงผลลัพธ์เป็น String
    if solution_node:
        # ย้อนรอยเส้นทาง [goal, ..., start]
        path_nodes = solution_node.path()
        
        # กลับด้านเป็น [start, ..., goal]
        path_nodes.reverse()
        
        # ดึงเฉพาะชื่อเมือง (state) ออกมา
        path_states = [node.state for node in path_nodes]
        
        # เชื่อมด้วย " - "
        return " - ".join(path_states)
    else:
        return f"No route found from {start} to {goal}"

# 7. --- ส่วนสำหรับทดสอบ (ตามโจทย์) ---
if __name__ == '__main__':
    print("Test P1")
    
    # ทดสอบเคส Arad -> Bucharest
    route1 = P1_route("Arad", "Bucharest")
    print(route1)
    
    # ทดสอบเคสอื่นๆ
    route2 = P1_route("Pitesti", "Timisoara")
    print(route2)
    
    route3 = P1_route("Neamt", "Drobeta")
    print(route3)
    
    route4 = P1_route("Arad", "Arad")
    print(route4)
  