# Import ไลบรารีที่จำเป็น
import bisect  # สำหรับการเพิ่มข้อมูลลงใน list โดยยังคงลำดับ (sorted insert)
import math
from random import random  # สำหรับการสุ่มค่าเล็กน้อยเพื่อ break ties

# --- ส่วนของโครงสร้างข้อมูลพื้นฐาน (จากไฟล์ .ipynb) ---

infinity = 1.0e400  # ค่าคงที่แทน infinity

class FIFOQueue():
    """คลาสสำหรับคิวแบบเข้าก่อนออกก่อน (First-In-First-Out Queue)"""
    def __init__(self):
        self.A = []; self.start = 0
        
    def append(self, item):
        self.A.append(item)

    def __len__(self):
        return len(self.A) - self.start

    def extend(self, items):
        self.A.extend(items)     

    def pop(self):    
        e = self.A[self.start]
        self.start += 1
        return e

    def is_empty(self):
        return self.__len__() == 0


class PriorityQueue:
    """คลาสสำหรับคิวแบบมีลำดับความสำคัญ (Priority Queue)"""
    def __init__(self, order=min, f=lambda x: x):
        self.A = []  # เก็บข้อมูลเป็นลิสต์ของ (priority, item)
        self.order = order  # min หรือ max (ในที่นี้เราใช้ min)
        self.f = f  # ฟังก์ชันสำหรับคำนวณ priority (cost)

    def append(self, item):
        """เพิ่ม item เข้าคิว โดยเรียงลำดับตาม priority ที่คำนวณโดย self.f"""
        bisect.insort(self.A, (self.f(item), item))

    def __len__(self):
        return len(self.A)

    def pop(self):
        """นำ item ที่มี priority ดีที่สุด (น้อยสุดถ้า order=min) ออกจากคิว"""
        if self.order == min:
            return self.A.pop(0)[1]  # [1] คือตัว item (ส่วน [0] คือ priority)
        else:
            return self.A.pop()[1]
            
    def extend(self, items):
        """เพิ่ม list ของ items ลงในคิวทีละตัว"""
        for item in items: self.append(item)
            
    def is_empty(self):
        return self.__len__() == 0


class Node:
    """
    คลาสสำหรับเก็บโหนดสถานะในการค้นหา (เหมือนใน P4.py)
    """
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state  # สถานะปัจจุบัน (ในโจทย์นี้คือ (ref_idx, test_idx))
        self.parent = parent  # โหนดแม่
        self.action = action  # ท่าที่ใช้ (เช่น 'match', 'insert')
        self.path_cost = path_cost  # ต้นทุนสะสม (cost) ที่ใช้มาถึงโหนดนี้
        self.depth = 0
        if parent is not None: 
            self.depth = parent.depth + 1
                    
    def path(self):
        """ย้อนรอยเส้นทางกลับไปหาโหนดเริ่มต้น"""
        x, result = self, [self]
        while x.parent is not None:
            result.append(x.parent)
            x = x.parent
        return result

    def expand(self, problem):
        """ขยายโหนดเพื่อสร้างโหนดลูก (สถานะถัดไป)"""
        return [Node(child, self, act,
            problem.path_cost(self.path_cost, self.state, act, child))
                for (act, child) in problem.successor(self.state)]

# --- ส่วนของอัลกอริทึมการค้นหา (จากไฟล์ .ipynb) ---

def best_first_search(problem, f, show=False):
    """
    ฟังก์ชันค้นหาแบบ Best-First Search
    f คือ cost function ที่ใช้ในการเรียง PriorityQueue
    """
    # Fringe คือ "ขอบเขต" ของการค้นหา หรือคิวของโหนดที่รอการสำรวจ
    fringe = PriorityQueue(min, f)  # ใช้ PriorityQueue โดยเรียงค่า f จากน้อยไปมาก
    fringe.append(Node(problem.initial))  # เริ่มต้นด้วยโหนดแรก
    search_cost = 0  # ใช้นับจำนวนโหนดที่ถูก 'expand' (ในโจทย์นี้ไม่ได้ใช้)

    # reached (หรือ explored set) ใช้เก็บสถานะที่เคยเจอแล้ว
    # พร้อมกับ cost ที่น้อยที่สุดที่เคยเจอสำหรับสถานะ_นั้น_
    reached = {}
    
    while not fringe.is_empty():
        # ดึงโหนดที่มี cost (ค่า f) น้อยที่สุดออกจากคิว
        node = fringe.pop()
        
        # 1. ตรวจสอบเป้าหมาย
        if problem.goal_test(node.state):
            return node, search_cost  # เจอเป้าหมาย! คืนโหนดและ cost
            
        # 2. ตรวจสอบ Optimality (หัวใจของ UCS/Dijkstra)
        # ถ้าสถานะนี้ยังไม่เคยเจอ หรือ ถ้าเคยเจอแต่ครั้งนี้มาด้วย cost ที่ "ถูกกว่า"
        if (node.state not in reached) or (node.path_cost < reached[node.state].path_cost):
            
            # อัปเดต/เพิ่ม สถานะนี้ใน 'reached' ว่านี่คือทางมาที่ถูกที่สุด
            reached[node.state] = node
            
            # ขยายโหนดลูก (สร้างสถานะถัดไป) และเพิ่มลงใน fringe
            fringe.extend(node.expand(problem))
            search_cost += 1

    return None, search_cost  # ไม่เจอเป้าหมาย


def uniform_cost_search(problem, show=False):
    """
    ฟังก์ชันค้นหาแบบ Uniform Cost Search (UCS)
    นี่คือ Best-First Search ประเภทหนึ่งที่ใช้ 'path_cost' เป็น cost function (f)
    """
    def fee(node):
        # f(n) = g(n) หรือ cost ที่ใช้เดินทางมาถึงโหนด n
        # เราบวก random() ค่าเล็กน้อยเพื่อ "break ties" 
        # (กรณีมีหลายโหนด cost เท่ากัน ให้สุ่มเลือก)
        return node.path_cost + 0.001*random()
    
    return best_first_search(problem, fee, show=show)

# --- ส่วนของปัญหา WER (นี่คือส่วนที่เราเขียนขึ้นมาใหม่) ---

class WERProblem:
    """
    คลาสสำหรับนิยามปัญหา Word Error Rate (WER) 
    โดยมองให้เป็นปัญหาการค้นหา (Search Problem)
    เราจะใช้เพื่อหา "Minimum Edit Distance" (จำนวน S, D, I ที่น้อยที่สุด)
    """
    
    def __init__(self, reference, test):
        """
        ref: สตริงอ้างอิง (คำตอบที่ถูก)
        test: สตริงที่ทดสอบ (คำตอบที่ได้)
        """
        self.reference = reference
        self.test = test
        # สถานะ (State) คือ (index ของ ref, index ของ test)
        # ที่เรากำลังเปรียบเทียบอยู่
        self.initial = (0, 0)  # สถานะเริ่มต้น: (index 0, index 0)
        # สถานะเป้าหมาย: (index สุดท้าย+1, index สุดท้าย+1)
        self.goal = (len(reference), len(test))
        
    def successor(self, state):
        """
        สร้าง "ท่าเดิน" (actions) และ "สถานะถัดไป" (next_states) ที่เป็นไปได้
        นี่คือการแปลง Edit Distance (S, D, I) ให้เป็นการเดินในกราฟ
        """
        ref_idx, test_idx = state
        successors = []
        
        # --- กรณี Base Cases (สุดขอบสตริง) ---
        
        # 1. ถ้าเปรียบเทียบ ref หมดแล้ว (แต่ test ยังเหลือ)
        if ref_idx >= len(self.reference):
            # ทำได้แค่ 'insert' (ข้ามตัวอักษร test ที่เหลือ)
            if test_idx < len(self.test):
                new_state = (ref_idx, test_idx + 1)
                successors.append(('insert', new_state))
            return successors  # ไม่มีท่าอื่นให้ทำแล้ว
        
        # 2. ถ้าเปรียบเทียบ test หมดแล้ว (แต่ ref ยังเหลือ)
        if test_idx >= len(self.test):
            # ทำได้แค่ 'delete' (ข้ามตัวอักษร ref ที่เหลือ)
            if ref_idx < len(self.reference):
                new_state = (ref_idx + 1, test_idx)
                successors.append(('delete', new_state))
            return successors  # ไม่มีท่าอื่นให้ทำแล้ว
        
        # --- กรณีทั่วไป (ยังเหลือทั้ง 2 สตริง) ---
        
        ref_char = self.reference[ref_idx]
        test_char = self.test[test_idx]
        
        # 3. ถ้าตัวอักษรตรงกัน (Match)
        if ref_char == test_char:
            # ท่า 'match': ขยับไปเปรียบเทียบตัวถัดไปของทั้งคู่
            new_state = (ref_idx + 1, test_idx + 1)
            successors.append(('match', new_state))
        else:
            # 4. ถ้าตัวอักษรไม่ตรงกัน -> 'substitute'
            # ท่า 'substitute': ขยับไปเปรียบเทียบตัวถัดไปของทั้งคู่
            new_state = (ref_idx + 1, test_idx + 1)
            successors.append(('substitute', new_state))
        
        # นอกจากท่า match/substitute แล้ว เรายังมีทางเลือกอื่นเสมอ:
        
        # 5. ท่า 'delete' (ลบจาก ref)
        # คือการข้ามตัวอักษรใน ref ไป 1 ตัว (ref+1) แต่ยังใช้ test ตัวเดิม (test)
        new_state_del = (ref_idx + 1, test_idx)
        successors.append(('delete', new_state_del))
        
        # 6. ท่า 'insert' (เพิ่มเข้า ref)
        # คือการข้ามตัวอักษรใน test ไป 1 ตัว (test+1) แต่ยังใช้ ref ตัวเดิม (ref)
        new_state_ins = (ref_idx, test_idx + 1)
        successors.append(('insert', new_state_ins))
        
        return successors
    
    def goal_test(self, state):
        """ตรวจสอบว่าถึงสถานะเป้าหมาย (เปรียบเทียบจบ) หรือยัง"""
        return state == self.goal
    
    def path_cost(self, cost_to_s, s, action, snext):
        """
        กำหนด "ต้นทุน" (cost) ของแต่ละท่าเดิน
        cost_to_s คือ cost สะสมที่ใช้มาถึงสถานะ s
        """
        if action == 'match':
            return cost_to_s + 0  # 'match' ไม่นับ cost
        else:
            # 'substitute', 'delete', 'insert' นับเป็น 1 operation
            return cost_to_s + 1

def P5_wer(ref, test):
    """
    ฟังก์ชันหลักสำหรับคำนวณ WER
    """
    
    # 1. สร้าง "ปัญหา" จาก ref และ test
    problem = WERProblem(ref, test)
    
    # 2. แก้ปัญหาด้วย Uniform Cost Search
    # UCS จะหา "เส้นทาง" (ลำดับของ S, D, I, M) ที่มี "ต้นทุน" (path_cost)
    # สะสมน้อยที่สุด จาก (0,0) ไปยัง (len(ref), len(test))
    solution_node, search_cost = uniform_cost_search(problem, show=False)
    
    if solution_node is None:
        # กรณีไม่เจอ (เช่น ref และ test ว่างทั้งคู่)
        return 0.0, 0
    
    # 3. ต้นทุนสะสมที่น้อยที่สุด = จำนวน S, D, I ที่น้อยที่สุด
    min_operations = int(solution_node.path_cost)

    # 4. คำนวณ WER
    N = len(ref)  # N คือจำนวนคำ (หรือตัวอักษร) ใน reference
    if N == 0:
        # จัดการกรณีหารด้วยศูนย์ (ถ้า ref ว่าง)
        # ถ้า test ก็ว่าง -> 0.0
        # ถ้า test ไม่ว่าง -> ถือว่า 'insert' ทั้งหมด (แต่ WER มักไม่นิยามกรณีนี้)
        wer = float(len(test)) if len(test) > 0 else 0.0
    else:
        # WER = (S + D + I) / N
        wer = float(min_operations) / float(N)
    
    return wer, min_operations

if __name__ == '__main__':
    wer, n = P5_wer("grit", "greet")
    print("wer = {}, n = {}".format(wer, n))