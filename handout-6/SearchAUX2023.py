import bisect
import math
from random import random

# Constant
infinity = 1.0e400

############
# Classes
############


class FIFOQueue():
    """A First-In-First-Out Queue."""
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
        # if self.start > 5 and self.start > len(self.A)/2:
        #     self.A = self.A[self.start:]
        #     self.start = 0
        return e

    def is_empty(self):
        return self.__len__() == 0


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

############
# Problem
############

class RoutingProblem:
    "The problem of searching a graph from one node to another."
    def __init__(self, local_map, initial, goal):
        self.map = local_map
        self.initial = initial
        self.goal = goal

    def successor(self, s):
        """
        Take s: current state/current town
        Return a list of (action, result/linked town) pairs.
        """
        return [(snext, snext) for snext in self.map['transit'][s].keys()]

    def path_cost(self, cost_to_s, s, action, snext):

        transit_cost = infinity
        if s in self.map["transit"]:
            if snext in self.map["transit"][s]:
                transit_cost = self.map["transit"][s][snext]

        return cost_to_s + transit_cost

    def goal_test(self, state):
        return state == self.goal

    def h(self, state):
        cx, cy = self.map["location"][state]
        gx, gy = self.map["location"][self.goal]

        # Squared Euclidean distance
        return math.sqrt( (cx - gx)**2 + (cy - gy)**2 )

###########################
# Node (Tree Structure)
###########################

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent is not None: 
            self.depth = parent.depth + 1
                    
    def path(self):
        x, result = self, [self]
        while x.parent is not None:
            result.append(x.parent)
            x = x.parent
        return result

    def expand(self, problem):
        return [Node(child, self, act,
            problem.path_cost(self.path_cost, self.state, act, child))
                for (act, child) in problem.successor(self.state)]


############
# Data
############

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

############
# Functions
############

def showq(q, name=""):
    qtxt = ""
    for f, i in q.A:
        qtxt += "({:.3f},{}) ".format(f,i.state)
    print("* {}:[{}]".format(name, qtxt.strip()))

def best_first_search(problem, f, show=False):
    fringe = PriorityQueue(min, f)                              # Set up a queue by f of node
    fringe.append(Node(problem.initial))                        # Add the initial state
    search_cost = 0
    if show:
        showq(fringe, "queue")

    reached = {}                                                # A record of states reached
    while not fringe.is_empty():                                # Traverse a queue
        node = fringe.pop()                                     # Pop the first in queue
        if problem.goal_test(node.state):                       # Check if goal is reach
            return node, search_cost                            # Yes, return the found
        if (node.state not in reached) or (node.path_cost < reached[node.state].path_cost):    
                                                                # Check if it's a new node or an old one with a better path     
            reached[node.state] = node                          # Track new reached (or better reached)
            fringe.extend(node.expand(problem))                 # Expand the fringe 
            search_cost += 1
            if show:
                showq(fringe, "queue")

    return None, search_cost                                     # There is no solution

def test_bfs(start='Arad', goal='Bucharest', disp=False):

    # Test it

    from random import seed
    from random import random

    # First, choose fee function
    def fee(node):
        return node.depth + 0.01*random() # The random part is to break tie, otherwise bisect.insort will have a hard time working


    prob = RoutingProblem(romania_map, initial=start, goal=goal)
    rst, scost = best_first_search(prob, fee, show=disp)

    soln = rst.path()

    route = ""
    for s in soln:
        route = s.state + ' - ' + route

    route = route[:-3].strip()
    print(route)  
    print('search cost =', scost)

def showfifo(q, name=""):
    qtxt = ""
    for i, n in enumerate(q.A):
        if i < q.start:
            qtxt += "{}, ".format(str(n.state[0]).lower())
        elif i == q.start:
            qtxt += "{}, ".format(str(n.state).upper())
        else:
            qtxt += "{}, ".format(n.state)
    print("* {}:[{}]".format(name, qtxt[:-2].strip()))

def breadth_first_search(problem, show=False):
    fringe = FIFOQueue()                    # Set up a FIFO queue
    fringe.append(Node(problem.initial))    # Add the initial state
    search_cost = 0
    if show:
        showfifo(fringe, "queue")

    reached = {}
    while not fringe.is_empty():            # Traverse a queue
        node = fringe.pop()                 # Pop the first in queue
        if problem.goal_test(node.state):   # Check if goal is reach
            return node, search_cost        # Yes, return the found
        if node.state not in reached:
            reached[node.state] = node
            fringe.extend(node.expand(problem)) # Expand the fringe 
            search_cost += 1  
            if show:
                showfifo(fringe, "queue")        
    return None, search_cost                # There is no solution

def breadth_first_search_nomem(problem, show=False):
    fringe = FIFOQueue()                    # Set up a FIFO queue
    fringe.append(Node(problem.initial))    # Add the initial state
    search_cost = 0
    if show:
        showfifo(fringe, "queue")

    while not fringe.is_empty():            # Traverse a queue
        node = fringe.pop()                 # Pop the first in queue
        if problem.goal_test(node.state):   # Check if goal is reach
            return node, search_cost        # Yes, return the found
        fringe.extend(node.expand(problem)) # Expand the fringe 
        search_cost += 1  
        if show:
            showfifo(fringe, "queue")        
    return None, search_cost                # There is no solution


def depth_first_search(problem, show=False):

    def fee(node):
        return -node.depth + 0.01*random() # The random part is to break tie, otherwise bisect.insort will have a hard time working

    return best_first_search(problem, fee, show=show)


def uniform_cost_search(problem, show=False):

    def fee(node):
        return node.path_cost + 0.001*random() # The random part is to break tie, otherwise bisect.insort will have a hard time working

    return best_first_search(problem, fee, show=show)


if __name__ == '__main__':
    test_bfs(start='Sibiu', disp=False)
    print()
    test_bfs(disp=True)
