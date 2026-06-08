# Informed Search AI Project Report: Addis Ababa Pathfinding

## 1. Graph Design
The project utilizes an adjacency list representation of a 10 node weighted graph representing key locations in Addis Ababa 

### Nodes and Connections
- **Nodes**: Piyassa, Arat Kilo, 6 Kilo, Kazanchis, Meskel Square, Mexico Square, Bole Edna Mall, Bole Airport, Gotera, Megenagna
- **Coordinates**: Each node is assigned a 2D coordinate $(x, y)$ to facilitate Euclidean distance calculations
- **Weights**: Edge weights represent real world distances between locations

### Search Algorithms
- **Greedy Best First Search (GBFS)**: Implemented using $f(n) = h(n)$ and It prioritizes nodes that appear closest to the goal, ignoring the cost already traveled
- **A* Search**: Implemented using $f(n) = g(n) + h(n)$ and It balances the path cost ($g$) and the heuristic estimate ($h$) to ensure optimality

---

## 2. Heuristic Funciton
Two heuristic scenarios were designed to test the robustness and behavior of the algorithms

### Scenario A: Good Heuristic 
This heuristic is admissible because the straight line distance is always the shortest possible path between two points and it makes sure that it never overestimates the actual cost

### Scenario B: Misleading Heuristic
This heuristic was designed to trick the algorithms by:
1. Underestimating suboptimal paths 
2. Overestimating nodes on the optimal path 
This causes algorithms to avoid the truly shorter path in favor of one that looks better according to the biased heuristic

---

## 3. Experimental Results 
The following data was collected from 4 execution scenarios starting from **Piyassa** to **Bole Airport**

| Algorithm | Heuristic | Nodes Expanded | Final Cost | Path Sequence |
| :--- | :--- | :--- | :--- | :--- |
| **GBFS** | Good | 5 | 9.3 | Piyassa -> Mexico -> Meskel -> Edna Mall -> Airport |
| **GBFS** | Misleading | 6 | 11.0 | Piyassa -> Mexico -> Meskel -> Gotera -> Airport |
| **A\*** | Good | 6 | 9.3 | Piyassa -> Mexico -> Meskel -> Edna Mall -> Airport |
| **A\*** | Misleading | 6 | 11.0 | Piyassa -> Mexico -> Meskel -> Gotera -> Airport |

---

## 4. Visual Analysis 

### Graph Visualization 
```
(6 Kilo)---(Megenagna)
   |           |
(Arat Kilo)--(Kazanchis)---(Edna Mall)
   |           |             |
(Piyassa)---(Meskel Sq)---(Airport)
   |           |             |
(Mexico Sq)----(Gotera)-------
```
*(Note: Edges are weighted; see graph.py for exact values)*

### Behavioral Shift Observation
- **Good Heuristic**: Both algorithms identified the optimal path via Bole Edna Mall (Cost 9.3) and GBFS was slightly faster in terms of nodes expanded in some configurations but matched A* here due to the small graph size
- **Misleading Heuristic**: The heuristic value for `Bole Edna Mall` was inflated to 9.0, while `Gotera` was deflated to 0.5 and This "tricked" both algorithms into taking the path through Gotera (Cost 11.0), demonstrating how poor heuristic design leads to suboptimality

---

## 5. Comparative Analysis 

### Why A* Guarantees Optimality
A* balances the cost already incurred ($g(n)$) with the estimated cost to the goal ($h(n)$). When $h(n)$ is admissible, A* will never "settle" for a suboptimal path if a better one could exist and If it finds a path to the goal, it is guaranteed to be the shortest because any other potential path would have an $f(n)$ value greater than or equal to the optimal path's cost

### GBFS vs. A*
GBFS is "short-sighted." It only cares about the remaining distance. In larger, more complex graphs, GBFS can often be faster but frequently finds suboptimal paths. A* is "methodical," ensuring it explores all promising directions until it confirms the best one

### The Impact of Misleading Heuristics
When the heuristic is inadmissible (like our Misleading one), A* loses its optimality guarantee and It trusts the "lie" told by the heuristic and skips the optimal path because it *thinks* that path is more expensive than it actually is

---

## 6. Conclusion 
This project successfully demonstrates the fundamental principles of informed search. By contrasting Euclidean-based admissible heuristics with biased inadmissible ones, we empirically proved that while A* is a powerful tool for optimization, its success is fundamentally dependent on the quality of the heuristic function provided.
