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
# DFS
# =========================================================

def dfs(graph, start, goal):

    stack = [(start, [start])]

    visited = set()

    while stack:

        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        for neighbor in reversed(graph[current]):

            if neighbor not in visited:

                stack.append(
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

    dfs(
        graph,
        start_node,
        goal_node
    )


print("DFS profiling completed.")