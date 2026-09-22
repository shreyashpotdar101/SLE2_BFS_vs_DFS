# SLE-2: Empirical Performance Analysis of BFS vs DFS

## Course

02AML204 – Introduction to Artificial Intelligence

## Experiment Title

Empirical Performance Analysis of Breadth-First Search (BFS) and Depth-First Search (DFS)

## Objective

To empirically compare BFS and DFS on the same graph-search problem using execution-time profiling, node-expansion counting, and py-spy flame graphs.

## Problem Description

A small directed graph was selected as the common problem for both algorithms.

The objective is to find the goal node `Z` starting from node `A`.

Both BFS and DFS use the same graph, start node, and goal node.

### Graph

A
├── B
│   ├── D → H → L → P → T
│   └── E → I → M → Q → U
│
└── C
    ├── F → J → N → R → V → X → Z
    └── G → K → O → S → W

## Algorithms

BFS:
Breadth-First Search explores nodes level by level using a queue.

Implementation file:
bfs_vs_dfs.py

DFS:
Depth-First Search explores a branch before backtracking and uses a stack.

Implementation file:
bfs_vs_dfs.py

## Experimental Setup
- Start node: A
- Goal node: Z
- Searches per run: 100000
- Number of runs: 3
- Same graph used for BFS and DFS
- Execution time measured using Python's high-resolution performance timer
- Number of expanded nodes counted manually
- py-spy used for visual profiling

## Results
| Metric | BFS | DFS |
|---|---:|---:|
| Path Length | 8 | 8 |
| Nodes Expanded | 25 | 20 |
| Average Total Time (ms) | 1070.167 | 1164.746 |
| Average Time/Search (ms) | 0.010702 | 0.011647 |
| Searches Per Run | 100000 | 100000 |

## Files
| File | Purpose |
|---|---|
| `bfs_vs_dfs.py` | Main BFS vs DFS implementation and numerical profiling |
| `pyspy_bfs.py` | BFS workload used for py-spy |
| `pyspy_dfs.py` | DFS workload used for py-spy |
| `bfs_flamegraph.svg` | BFS py-spy flame graph |
| `dfs_flamegraph.svg` | DFS py-spy flame graph |
| `README.md` | Project documentation |
| `AI_ContributionLog.md` | AI assistance and contribution record |

```text