from collections import deque


# =========================================================
# GRAPH
# =========================================================

graph = {
    'A': ['B', 'C'],

    'B': ['D', 'E'],
    'C': ['F', 'G'],

    'D': ['H'],
    'E': ['I'],

    'F': ['J'],
    'G': ['K'],

    'H': ['L'],
    'I': ['M'],

    'J': ['N'],
    'K': ['O'],

    'L': ['P'],
    'M': ['Q'],

    'N': ['R'],
    'O': ['S'],

    'P': ['T'],
    'Q': ['U'],

    'R': ['V'],
    'S': ['W'],

    'T': [],
    'U': [],

    'V': ['X'],
    'W': [],

    'X': ['Z'],

    'Z': []
}


# =========================================================
# BFS
# =========================================================

def bfs(graph, start, goal):

    queue = deque([(start, [start])])

    visited = set()

    while queue:

        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        for neighbor in graph[current]:

            if neighbor not in visited:

                queue.append(
                    (neighbor, path + [neighbor])
                )

    return None


# =========================================================
# PROFILING LOOP
# =========================================================

start_node = 'A'
goal_node = 'Z'

repeat = 1000000

for _ in range(repeat):

    bfs(
        graph,
        start_node,
        goal_node
    )


print("BFS profiling completed.")