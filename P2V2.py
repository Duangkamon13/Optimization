# P2.py
# เป็น Breath first Search เพราะมันสามารถที่จะ
# 1. คลาสสำหรับ "นิยามปัญหา" (จากเซลล์ที่ 8 ใน Notebook)
class SimpleRoutingProblem:
    "The problem of searching a graph from one node to another."
    def __init__(self, local_map, initial, goal):
        self.map = local_map
        self.initial = initial
        self.goal = goal

    def successor(self, current_town):
        """
        Take:   Current town/state
        Return: A list of (road/action, next town/next state) pairs.
        """
        options = []
        # (แก้ไข) เพิ่มการตรวจสอบว่ามี key นี้จริงหรือไม่
        if current_town in self.map['transit']:
            for town in self.map['transit'][current_town].keys():
                # (แก้ไข) ใช้ " - " ตามโจทย์ P2
                road = current_town + ' - ' + town
                options.append( (road, town) )
        return options

    def goal_test(self, town):
        return town == self.goal

# 3. คลาสสำหรับ "โหนด" หรือ "รอยเท้า" (จากเซลล์ที่ 14)
class Town:
    def __init__(self, name, parent=None, action=None):
        self.name = name
        self.parent = parent
        self.action = action
                    
    def path(self):
        x = self
        result = [x.name]
        while x.parent is not None:
            result.append(x.parent.name)
            x = x.parent
        return result

    def expand(self, problem):
        nexts = []
        for (road, next_town) in problem.successor(self.name):
            nexts.append(Town(next_town, self, road))
        return nexts

# 4. ฟังก์ชันสำหรับหาเส้นทาง (BFS)
# (แก้ไข) - เพิ่ม 'map_fname' เป็น argument แรก
def P2_route(map_fname, start, goal):
    
    # --- ส่วนที่ 1: การอ่านและแปลข้อมูลไฟล์ (File Parsing) ---
    locations = {}
    transits = {}
    
    try:
        with open(map_fname, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
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
                        neighbor_name, dist_str = neighbor_data.split(':')
                        transits[town_name][neighbor_name.strip()] = int(dist_str.strip())

    except FileNotFoundError:
        return f"Error: Map file '{map_fname}' not found."
    except Exception as e:
        return f"Error parsing map file: {e}"

    romania_map = {"location": locations, "transit": transits}
    
    # --- (Debug) พิมพ์แผนที่ที่อ่านได้ออกมาดู ---
    # print("DEBUG: Map data loaded:", romania_map)
    # --- (End Debug) ---

    # --- (จบส่วน File Parsing) ---
    
    problem = SimpleRoutingProblem(romania_map, start , goal)
    # Set up a queue
    fringe = []                             
    fringe.append(Town(problem.initial))

    # Search
    while len(fringe) > 0:   
        # Pop the first in queue
        candidate = fringe[0] 
        fringe = fringe[1:]

        # Check it out
        if problem.goal_test(candidate.name): 
            path = candidate.path()
            path.reverse()
            # return " -> ".join(path) 
            return "->".join(path)
        # Nah, not yet
        # Have its successors in the queue
        fringe.extend(candidate.expand(problem))   # Expand the fringe 

# 5. ส่วนสำหรับรัน
if __name__ == '__main__':
    # ตอนนี้การเรียกใช้ (3 args) จะตรงกับนิยาม (3 args) แล้ว
    r = P2_route('P2romania.txt', 'Arad', 'Bucharest')
    print(r)
