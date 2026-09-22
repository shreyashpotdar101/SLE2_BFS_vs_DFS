import time
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
# BFS - BREADTH FIRST SEARCH
# =========================================================

def bfs(graph, start, goal):

    queue = deque([(start, [start])])

    visited = set()

    nodes_expanded = 0

    while queue:

        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        for neighbor in graph[current]:

            if neighbor not in visited:

                queue.append(
                    (neighbor, path + [neighbor])
                )

    return None, nodes_expanded


# =========================================================
# DFS - DEPTH FIRST SEARCH
# =========================================================

def dfs(graph, start, goal):

    stack = [(start, [start])]

    visited = set()

    nodes_expanded = 0

    while stack:

        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        for neighbor in reversed(graph[current]):

            if neighbor not in visited:

                stack.append(
                    (neighbor, path + [neighbor])
                )

    return None, nodes_expanded


# =========================================================
# EXPERIMENT SETTINGS
# =========================================================

start_node = 'A'

goal_node = 'Z'

runs = 3

# Number of times each algorithm is executed
# during each timing run.
repeat_per_run = 100000


# =========================================================
# FIRST TEST - VERIFY BFS
# =========================================================

bfs_path, bfs_nodes = bfs(
    graph,
    start_node,
    goal_node
)


# =========================================================
# FIRST TEST - VERIFY DFS
# =========================================================

dfs_path, dfs_nodes = dfs(
    graph,
    start_node,
    goal_node
)


# =========================================================
# BFS TIMING EXPERIMENT
# =========================================================

bfs_times = []

for i in range(runs):

    start_time = time.perf_counter()

    for _ in range(repeat_per_run):

        bfs(
            graph,
            start_node,
            goal_node
        )

    end_time = time.perf_counter()

    total_time = (
        end_time - start_time
    ) * 1000

    bfs_times.append(total_time)


bfs_total_average = (
    sum(bfs_times) / runs
)

bfs_average_per_search = (
    bfs_total_average / repeat_per_run
)


# =========================================================
# DFS TIMING EXPERIMENT
# =========================================================

dfs_times = []

for i in range(runs):

    start_time = time.perf_counter()

    for _ in range(repeat_per_run):

        dfs(
            graph,
            start_node,
            goal_node
        )

    end_time = time.perf_counter()

    total_time = (
        end_time - start_time
    ) * 1000

    dfs_times.append(total_time)


dfs_total_average = (
    sum(dfs_times) / runs
)

dfs_average_per_search = (
    dfs_total_average / repeat_per_run
)


# =========================================================
# PATH LENGTH
# =========================================================

bfs_path_length = len(bfs_path) - 1

dfs_path_length = len(dfs_path) - 1


# =========================================================
# DISPLAY BFS RESULTS
# =========================================================

print()
print("========================================")
print("              BFS RESULTS")
print("========================================")

print("Start Node:", start_node)

print("Goal Node:", goal_node)

print(
    "Path:",
    " -> ".join(bfs_path)
)

print(
    "Path Length:",
    bfs_path_length
)

print(
    "Nodes Expanded:",
    bfs_nodes
)

print()

print(
    "Run 1 Total Time:",
    round(bfs_times[0], 3),
    "ms"
)

print(
    "Run 2 Total Time:",
    round(bfs_times[1], 3),
    "ms"
)

print(
    "Run 3 Total Time:",
    round(bfs_times[2], 3),
    "ms"
)

print(
    "Average Total Time:",
    round(bfs_total_average, 3),
    "ms"
)

print(
    "Average Time Per Search:",
    round(bfs_average_per_search, 6),
    "ms"
)

print(
    "Number of Searches Per Run:",
    repeat_per_run
)


# =========================================================
# DISPLAY DFS RESULTS
# =========================================================

print()
print("========================================")
print("              DFS RESULTS")
print("========================================")

print("Start Node:", start_node)

print("Goal Node:", goal_node)

print(
    "Path:",
    " -> ".join(dfs_path)
)

print(
    "Path Length:",
    dfs_path_length
)

print(
    "Nodes Expanded:",
    dfs_nodes
)

print()

print(
    "Run 1 Total Time:",
    round(dfs_times[0], 3),
    "ms"
)

print(
    "Run 2 Total Time:",
    round(dfs_times[1], 3),
    "ms"
)

print(
    "Run 3 Total Time:",
    round(dfs_times[2], 3),
    "ms"
)

print(
    "Average Total Time:",
    round(dfs_total_average, 3),
    "ms"
)

print(
    "Average Time Per Search:",
    round(dfs_average_per_search, 6),
    "ms"
)

print(
    "Number of Searches Per Run:",
    repeat_per_run
)


# =========================================================
# FINAL COMPARISON
# =========================================================

print()
print("========================================")
print("          BFS vs DFS COMPARISON")
print("========================================")

print()

print(
    f"{'Metric':<30}"
    f"{'BFS':<18}"
    f"{'DFS':<18}"
)

print("-" * 66)

print(
    f"{'Nodes Expanded':<30}"
    f"{bfs_nodes:<18}"
    f"{dfs_nodes:<18}"
)

print(
    f"{'Path Length':<30}"
    f"{bfs_path_length:<18}"
    f"{dfs_path_length:<18}"
)

print(
    f"{'Average Total Time (ms)':<30}"
    f"{bfs_total_average:<18.3f}"
    f"{dfs_total_average:<18.3f}"
)

print(
    f"{'Average Time/Search (ms)':<30}"
    f"{bfs_average_per_search:<18.6f}"
    f"{dfs_average_per_search:<18.6f}"
)

print(
    f"{'Searches Per Run':<30}"
    f"{repeat_per_run:<18}"
    f"{repeat_per_run:<18}"
)

print()

print("Experiment completed successfully.")