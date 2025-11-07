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

def P1_route(start, goal):
    graph = romania_map["transit"]
    if start == goal:
        return start
    from collections import deque
    q = deque([start])
    visited = {start}
    parent = {}
    found = False

    while q and not found:
        u = q.popleft()
        for v in graph[u].keys():  
            if v not in visited:
                visited.add(v)
                parent[v] = u
                if v == goal:
                    found = True
                    break
                q.append(v)
    path = [goal]
    cur = goal
    while cur != start:
        cur = parent[cur]
        path.append(cur)
    path.reverse()

    route = " - ".join(path)
    return route


if __name__ == '__main__':

    # start = input("Current town: ")
    # goal = input("Destination: ")
    # print(P1_route(start, goal))
    print(P1_route("Arad", "Bucharest"))