
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

class SimpleRoutingProblem: #กำหนดปัยหา
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
        for town in self.map['transit'][current_town].keys():
            # next_town = town
            road = current_town + '-' + town
            options.append( (road, town) )
        
        return options

    def goal_test(self, town):
        return town == self.goal

   
class town : 
    def __init__(self, name, parent=None, action=None):
        self.name = name       # Current town name
        self.parent = parent   # Previous town OBJECT!
        self.action = action   # Which road has been taken from previous town to the current town
                    
    def path(self):
        x = self
        result = [x.name]
        while x.parent is not None:
            result.append(x.parent.name)
            x = x.parent
        return result

    def expand(self, problem):
        nexts = []

        for road, next_town in problem.successor(self.name):
            nexts.append(town(next_town, self, road))
        
        return nexts

    def __str__(self):
        from_town = "nowhere"
        if self.parent is not None:
            from_town = self.parent.name
        thru = "nothing"
        if self.action is not None:
            thru = self.action
            
        return self.name + f" (from {from_town} thru {thru})"
    
def  P1_route(start, goal):
    problem = SimpleRoutingProblem(romania_map, start , goal)
    # Set up a queue
    fringe = []                             
    fringe.append(town(problem.initial))

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

if __name__ == '__main__':
    print(P1_route("Arad", "Bucharest"))