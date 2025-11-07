import bisect
import math
from random import random

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
        return e

    def is_empty(self):
        return self.__len__() == 0


class PriorityQueue:
    def __init__(self, order=min, f=lambda x: x):
        self.A = []
        self.order = order
        self.f = f

    def append(self, item):
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

def breadth_first_search(problem, show=False):
    fringe = FIFOQueue()
    fringe.append(Node(problem.initial))
    search_cost = 0

    reached = {}
    while not fringe.is_empty():
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node, search_cost
        if node.state not in reached:
            reached[node.state] = node
            fringe.extend(node.expand(problem))
            search_cost += 1
    return None, search_cost
class MissionaryProblem:
    """The missionary-cannibal river crossing problem using SearchAUX2023 framework."""
    
    def __init__(self, initial):
        self.initial = initial  # (m_wait, c_wait, m_cross, c_cross, boat_side)
        # Goal: everyone crossed, boat on crossed side
        m_total = initial[0] + initial[2]
        c_total = initial[1] + initial[3]
        self.goal = (0, 0, m_total, c_total, 0)
        
    def is_valid_state(self, state):
        """Check if a state is valid (missionaries not outnumbered)."""
        m_wait, c_wait, m_cross, c_cross, boat_side = state

        if m_wait < 0 or c_wait < 0 or m_cross < 0 or c_cross < 0:
            return False

        if m_wait > 0 and c_wait > m_wait:
            return False

        if m_cross > 0 and c_cross > m_cross:
            return False
            
        return True
    
    def successor(self, state):
        """Generate all possible next states from current state."""
        m_wait, c_wait, m_cross, c_cross, boat_side = state
        successors = []
        
        possible_actions = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
        
        for action in possible_actions:
            m_boat, c_boat = action
            
            if boat_side == 1:  # Boat on waiting side, going to crossed side
                new_m_wait = m_wait - m_boat
                new_c_wait = c_wait - c_boat
                new_m_cross = m_cross + m_boat
                new_c_cross = c_cross + c_boat
                new_boat_side = 0
                
                # Check if we have enough people on waiting side
                if new_m_wait >= 0 and new_c_wait >= 0:
                    new_state = (new_m_wait, new_c_wait, new_m_cross, new_c_cross, new_boat_side)
                    if self.is_valid_state(new_state):
                        successors.append((action, new_state))
                        
            else:  # Boat on crossed side, going to waiting side
                new_m_wait = m_wait + m_boat
                new_c_wait = c_wait + c_boat
                new_m_cross = m_cross - m_boat
                new_c_cross = c_cross - c_boat
                new_boat_side = 1
                
                # Check if we have enough people on crossed side
                if new_m_cross >= 0 and new_c_cross >= 0:
                    new_state = (new_m_wait, new_c_wait, new_m_cross, new_c_cross, new_boat_side)
                    if self.is_valid_state(new_state):
                        successors.append((action, new_state))
        
        return successors
    
    def goal_test(self, state):
        """Check if current state is the goal state."""
        return state == self.goal
    
    def path_cost(self, cost_to_s, s, action, snext):
        """Each action has cost 1."""
        return cost_to_s + 1
def P4_crossriver(initial):

    problem = MissionaryProblem(initial)

    solution_node, search_cost = breadth_first_search(problem, show=False)
    
    if solution_node is None:
        return []  
    
    path = solution_node.path()
    path.reverse() 
    
    actions = []
    for node in path[1:]: 
        actions.append(node.action)
    
    return actions