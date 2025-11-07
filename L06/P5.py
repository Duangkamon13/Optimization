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

def best_first_search(problem, f, show=False):
    fringe = PriorityQueue(min, f)
    fringe.append(Node(problem.initial))
    search_cost = 0

    reached = {}
    while not fringe.is_empty():
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node, search_cost
        if (node.state not in reached) or (node.path_cost < reached[node.state].path_cost):
            reached[node.state] = node
            fringe.extend(node.expand(problem))
            search_cost += 1

    return None, search_cost


def uniform_cost_search(problem, show=False):
    def fee(node):
        return node.path_cost + 0.001*random()
    
    return best_first_search(problem, fee, show=show)

class WERProblem:
    """Word Error Rate problem using edit distance (minimum operations)."""
    
    def __init__(self, reference, test):
        self.reference = reference
        self.test = test
        self.initial = (0, 0)  # (ref_index, test_index)
        self.goal = (len(reference), len(test))
        
    def successor(self, state):
        """Generate all possible next states from current state."""
        ref_idx, test_idx = state
        successors = []
        
        # If we've processed all reference characters
        if ref_idx >= len(self.reference):
            # Can only insert remaining test characters
            if test_idx < len(self.test):
                # Insert operation
                new_state = (ref_idx, test_idx + 1)
                successors.append(('insert', new_state))
            return successors
        
        # If we've processed all test characters
        if test_idx >= len(self.test):
            # Can only delete remaining reference characters
            if ref_idx < len(self.reference):
                # Delete operation
                new_state = (ref_idx + 1, test_idx)
                successors.append(('delete', new_state))
            return successors
        
        # Both strings have remaining characters
        ref_char = self.reference[ref_idx]
        test_char = self.test[test_idx]
        
        # Match (no operation needed)
        if ref_char == test_char:
            new_state = (ref_idx + 1, test_idx + 1)
            successors.append(('match', new_state))
        else:
            # Substitution
            new_state = (ref_idx + 1, test_idx + 1)
            successors.append(('substitute', new_state))
        
        # Deletion (skip reference character)
        new_state = (ref_idx + 1, test_idx)
        successors.append(('delete', new_state))
        
        # Insertion (skip test character)
        new_state = (ref_idx, test_idx + 1)
        successors.append(('insert', new_state))
        
        return successors
    
    def goal_test(self, state):
        """Check if we've processed both strings completely."""
        return state == self.goal
    
    def path_cost(self, cost_to_s, s, action, snext):
        """Cost is 0 for match, 1 for all other operations."""
        if action == 'match':
            return cost_to_s + 0
        else:
            return cost_to_s + 1

def P5_wer(ref, test):
   
    problem = WERProblem(ref, test)
    
    # Solve using uniform cost search to find minimum operations
    solution_node, search_cost = uniform_cost_search(problem, show=False)
    
    if solution_node is None:
        return 0.0, 0  # No operations needed for empty string
    min_operations = int(solution_node.path_cost)

    N = len(ref)
    if N == 0:

        wer = float(len(test)) if len(test) > 0 else 0.0
    else:
        wer = float(min_operations) / float(N)
    
    return wer, min_operations