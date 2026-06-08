import heapq
import time
from typing import Dict, List, Tuple, Optional
def greedy_best_first_search(
    graph: Dict[str, List[Tuple[str, float]]], 
    heuristics: Dict[str, float], 
    start: str, 
    goal: str
) -> Optional[Dict]:
    priority_queue = []
    heapq.heappush(priority_queue, (heuristics[start], start, [start]))
    visited = set()
    expansion_order = []
    start_time = time.perf_counter()
    while priority_queue:
        h_val, current_node, path = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        expansion_order.append(current_node)
        visited.add(current_node)
        if current_node == goal:
            end_time = time.perf_counter()
            total_cost = 0
            for i in range(len(path) - 1):
                for neighbor, cost in graph[path[i]]:
                    if neighbor == path[i+1]:
                        total_cost += cost
                        break
            return {
                "path": path,
                "expansion_order": expansion_order,
                "total_cost": total_cost,
                "execution_time": end_time - start_time
            }
        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor, new_path))  
    return None
if __name__ == "__main__":
    from graph import ADJACENCY_LIST, GOOD_HEURISTIC
    res = greedy_best_first_search(ADJACENCY_LIST, GOOD_HEURISTIC, "Piyassa", "Bole Airport")
    print(f"Path: {res['path']}")
    print(f"Cost: {res['total_cost']}")
