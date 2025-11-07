# --- นี่คือโค้ด "แบบดิบ" (Raw) ที่ยังไม่แก้ ---

# 1. ข้อมูลแผนที่ (Map Data)
towns ={'Arad': (91, 492), 'Bucharest': (400, 327), 'Craiova': (253, 288), \
    'Drobeta': (165, 299), 'Eforie': (562, 293), 'Fagaras': (305, 449), \
    'Giurgiu': (375, 270), 'Hirsova': (534, 350), 'Iasi': (473, 506), \
    'Lugoj': (165, 379), 'Mehadia': (168, 339), 'Neamt': (406, 537), \
    'Oradea': (131, 571), 'Pitesti': (320, 368), 'Rimnicu Vilcea': (233, 410), \
    'Sibiu': (207, 457), 'Timisoara': (94, 410), 'Urziceni': (456, 350), \
    'Vaslui': (509, 444), 'Zerind': (108, 531)}

roads = {'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
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
        'Zerind': {'Oradea': 71, 'Arad': 75} }

romania_map = {"location": towns, "transit": roads}

# 2. คลาสสำหรับ "นิยามปัญหา"
class SimpleRoutingProblem:
    def __init__(self, local_map, initial, goal):
        self.map = local_map
        self.initial = initial
        self.goal = goal

    def successor(self, current_town):
        options = []
        for town in self.map['transit'][current_town].keys():
            road = current_town + '-' + town
            options.append( (road, town) )
        return options

    def goal_test(self, town):
        return town == self.goal

# 3. คลาสสำหรับ "โหนด" หรือ "รอยเท้า"
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

# 4. ฟังก์ชันสำหรับหาเส้นทาง (BFS แบบดิบ - ไม่มี visited)
def P1_route(start, goal):
    
    problem = SimpleRoutingProblem(romania_map, start, goal)
    fringe = []
    fringe.append(Town(problem.initial))

    # *** ไม่มี visited set ***

    while len(fringe) > 0:
        
        candidate = fringe.pop(0) 

        # *** ไม่มีตัวเช็กว่าเคยมาแล้วหรือยัง ***

        if problem.goal_test(candidate.name):
            path = candidate.path()
            path.reverse()
            return " -> ".join(path) 

        # ขยายเส้นทางทันที
        fringe.extend(candidate.expand(problem))

    return "No route found."
if __name__ == '__main__':
    print(P1_route("Bucharest","Arad"))
    