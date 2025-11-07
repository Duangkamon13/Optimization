import bisect
import math
from random import random

# Constant
infinity = 1.0e400


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
        

########################################### code from writeup #######
def showq(q, name=""):
    qtxt = ""
    for f, i in q.A:
        qtxt += "({:.3f},{}) ".format(f,i.state)
    print("* {}:[{}]".format(name, qtxt.strip()))

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

    return None, search_cost                    


def fee(node):
    return node.depth + 0.01*random() 

def uniform_cost_search(problem, show=False):
    def fee(node):
        return node.path_cost + 0.001*random() # The random part is to break tie, otherwise bisect.insort will have a hard time working

    return best_first_search(problem, fee, show=show)


############################################# My code ################

def P3_route(romania_map, start, goal):
    roads = {}  
    with open(romania_map) as f:
        for line in f:
            town_part, neighbors_part = line.strip().split(';')
            town_name = town_part.split(':')[0].strip()
            neighbors = {}
            for nbr in neighbors_part.split(','):
                if ':' in nbr:
                    n_name, dist = nbr.split(':')
                    neighbors[n_name.strip()] = int(dist.strip())
            roads[town_name] = neighbors

    romania_map = {"transit": roads}

    prob = RoutingProblem(romania_map, start, goal)
    rst, scost = uniform_cost_search(prob, show=False)

    soln = rst.path()

    route = ""
    for s in soln:
        route = s.state + ' - ' + route

    route = route[:-3].strip()
    return route

if __name__ == '_main_':
    r = P3_route('P2romania.txt', 'Arad', 'Bucharest')
    print(r)