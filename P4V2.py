from collections import deque

class StateNode:
    """
    คลาสสำหรับจัดเก็บสถานะแต่ละโหนดในการค้นหา
    state: ทูเพิล (M1, C1, M2, C2, B)
    parent: โหนดแม่ (StateNode)
    action: ทูเพิล (m, c) ที่ทำให้เกิดสถานะนี้
    """
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

    def expand(self, problem):
        """
        ขยายโหนดเพื่อสร้างโหนดลูกที่เป็นไปได้ทั้งหมด
        """
        return [
            StateNode(next_state, self, action) 
            for (action, next_state) in problem.successor(self.state)
        ]

    def path_actions(self):
        """
        ย้อนรอยเส้นทางจากโหนดนี้กลับไปยังโหนดเริ่มต้น
        และคืนค่าเป็นลิสต์ของ actions
        """
        actions = []
        node = self
        while node.parent:
            actions.append(node.action)
            node = node.parent
        return actions[::-1]  # กลับลำดับเพื่อให้เป็นจากเริ่มต้นไปเป้าหมาย

class CrossRiverProblem:
    """
    คลาสสำหรับนิยามปัญหาส่งมิชชันนารีและคานนิบาลข้ามแม่น้ำ
    """
    def __init__(self, initial_state):
        self.initial_state = initial_state
        # คำนวณจำนวนมิชชันนารีและคานนิบาลทั้งหมดจากสถานะเริ่มต้น
        M_total = initial_state[0] + initial_state[2]
        C_total = initial_state[1] + initial_state[3]
        # นิยามสถานะเป้าหมาย
        self.goal_state = (0, 0, M_total, C_total, 0)
        # การกระทำ (action) ที่เป็นไปได้ทั้งหมด: (m, c)
        self.possible_actions = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

    def goal_test(self, state):
        """
        ตรวจสอบว่าสถานะที่กำหนดเป็นสถานะเป้าหมายหรือไม่
        """
        return state == self.goal_state

    def is_valid(self, state):
        """
        ตรวจสอบว่าสถานะที่กำหนดถูกต้องตามเงื่อนไขความปลอดภัยหรือไม่
        (มิชชันนารีต้องไม่น้อยกว่าคานนิบาลบนฝั่งใดฝั่งหนึ่ง หากมีมิชชันนารีอยู่)
        """
        M1, C1, M2, C2, B = state
        
        # ตรวจสอบว่าจำนวนคนไม่ติดลบ (อาจเกิดขึ้นระหว่างคำนวณ)
        if M1 < 0 or C1 < 0 or M2 < 0 or C2 < 0:
            return False
        
        # ตรวจสอบเงื่อนไขความปลอดภัยบนฝั่งรอ (M1, C1)
        if M1 > 0 and M1 < C1:
            return False
            
        # ตรวจสอบเงื่อนไขความปลอดภัยบนฝั่งที่ข้ามไปแล้ว (M2, C2)
        if M2 > 0 and M2 < C2:
            return False
            
        return True

    def successor(self, state):
        """
        สร้างลิสต์ของ (action, next_state) ที่เป็นไปได้จากสถานะปัจจุบัน
        """
        M1, C1, M2, C2, B = state
        successors = []

        for m, c in self.possible_actions:
            if B == 1:  # เรืออยู่ฝั่งรอ (ไปฝั่งข้าม)
                if M1 >= m and C1 >= c:  # มีคนพอให้ขึ้นเรือ
                    new_state = (M1 - m, C1 - c, M2 + m, C2 + c, 0)
                    if self.is_valid(new_state):
                        successors.append(((m, c), new_state))
            else:  # เรืออยู่ฝั่งข้าม (กลับฝั่งรอ)
                if M2 >= m and C2 >= c:  # มีคนพอให้ขึ้นเรือ
                    new_state = (M1 + m, C1 + c, M2 - m, C2 - c, 1)
                    if self.is_valid(new_state):
                        successors.append(((m, c), new_state))
                        
        return successors

def breadth_first_search(problem):
    """
    ฟังก์ชันค้นหาแบบ Breadth-First (BFS)
    """
    # ใช้ deque (Double-Ended Queue) เพื่อประสิทธิภาพที่ดีกว่า list.pop(0)
    fringe = deque()  
    
    # ใช้ set เพื่อเก็บสถานะที่เคยสำรวจแล้ว (explored) เพื่อป้องกันการวนลูป
    explored = set()

    # เพิ่มโหนดเริ่มต้นเข้าคิวและ set
    start_node = StateNode(problem.initial_state)
    fringe.append(start_node)
    explored.add(start_node.state)

    while fringe:
        # นำโหนดแรกออกจากคิว
        node = fringe.popleft()

        # ตรวจสอบว่าถึงเป้าหมายหรือไม่
        if problem.goal_test(node.state):
            return node.path_actions()  # คืนค่าลิสต์ของ actions

        # ขยายโหนด (สร้างโหนดลูก)
        for child in node.expand(problem):
            # ถ้ายังไม่เคยสำรวจสถานะนี้
            if child.state not in explored:
                # เพิ่มเข้า set และคิว
                explored.add(child.state)
                fringe.append(child)
                
    return None  # ไม่พบเส้นทาง

def P4_crossriver(initial):
    """
    ฟังก์ชันหลักในการแก้ปัญหาตามโจทย์
    """
    problem = CrossRiverProblem(initial)
    solution = breadth_first_search(problem)
    return solution

if __name__ == '__main__':
    print(P4_crossriver((2,2,1,1,1)))