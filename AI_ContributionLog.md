# AI Contribution Log

## SLE-2: BFS vs DFS Empirical Performance Analysis

### Project Information

| Field | Details |
|---|---|
| Project | SLE-2 Profiling Report |
| Comparison | BFS vs DFS |
| Programming Language | Python |
| AI Tool Used | ChatGPT |
| Profiling Tool | py-spy |
| Development Environment | Visual Studio Code |
| Version Control | Git / GitHub |

## AI Assistance

AI assistance was used during the development and documentation of this experiment.

### 1. Problem and Algorithm Setup

ChatGPT assisted with:

- Structuring the BFS and DFS comparison.
- Selecting a small graph-search problem.
- Ensuring that BFS and DFS use the same graph, start node, and goal node.
- Explaining the difference between BFS and DFS.

### 2. Python Implementation

ChatGPT assisted with:

- Writing and improving BFS implementation.
- Writing and improving DFS implementation.
- Adding node-expansion counting.
- Adding execution-time measurement.
- Repeating searches to obtain measurable execution times.

### 3. Debugging

AI assistance was used to identify and correct problems in the graph and profiling setup.

The final experiment was executed and verified locally by the student.

### 4. py-spy Profiling

ChatGPT assisted with:

- Preparing separate BFS and DFS profiling scripts.
- Providing the py-spy command required to generate flame graphs.
- Explaining how to verify the generated SVG files.

The py-spy executed locally and generated:

5. Results and Analysis
ChatGPT assisted with organizing and explaining the measured results.
The final numerical values were obtained by executing the Python program locally.

Final measured results:

| Metric | BFS | DFS |
|---|---:|---:|
| Nodes Expanded | 25 | 20 |
| Path Length | 8 | 8 |
| Average Total Time (ms) | 1070.167 | 1164.746 |
| Average Time/Search (ms) | 0.010702 | 0.011647 |
| Searches Per Run | 100000 | 100000 |


```text
bfs_flamegraph.svg
dfs_flamegraph.svg