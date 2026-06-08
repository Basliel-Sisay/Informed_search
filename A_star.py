import heapq
import time
from typing import Dict, List, Tuple, Optional
def a_star_search(
    graph: Dict[str, List[Tuple[str, float]]], 
    heuristics: Dict[str, float], 
    start: str, 
    goal: str
) -> Optional[Dict]:
    priority_queue = []
    start_f = 0 + heuristics[start]
    heapq.heappush(priority_queue, (start_f, 0, start, [start]))
    best_g_costs = {start: 0.0}
    expansion_order = []
    start_time = time.perf_counter()
    while priority_queue:
        f_cost, g_cost, current_node, path = heapq.heappop(priority_queue)
        expansion_order.append(current_node)
        if current_node == goal:
            end_time = time.perf_counter()
            return {
                "path": path,
                "expansion_order": expansion_order,
                "total_cost": g_cost,
                "execution_time": end_time - start_time
            }
        for neighbor, weight in graph.get(current_node, []):
            new_g_cost = g_cost + weight
            if neighbor not in best_g_costs or new_g_cost < best_g_costs[neighbor]:
                best_g_costs[neighbor] = new_g_cost
                new_f_cost = new_g_cost + heuristics[neighbor]
                new_path = path + [neighbor]
                heapq.heappush(priority_queue, (new_f_cost, new_g_cost, neighbor, new_path))
    return None
if __name__ == "__main__":
    from graph import ADJACENCY_LIST, GOOD_HEURISTIC
    res = a_star_search(ADJACENCY_LIST, GOOD_HEURISTIC, "Piyassa", "Bole Airport")
    print(f"Path: {res['path']}")
    print(f"Cost: {res['total_cost']}")
