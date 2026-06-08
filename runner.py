import time
from graph import ADJACENCY_LIST, GOOD_HEURISTIC, MISLEADING_HEURISTIC
from GBFS import greedy_best_first_search
from A_star import a_star_search  
def run_experiments():
    scenarios = [
        ("GBFS", GOOD_HEURISTIC, "Good"),
        ("GBFS", MISLEADING_HEURISTIC, "Misleading"),
        ("A*", GOOD_HEURISTIC, "Good"),
        ("A*", MISLEADING_HEURISTIC, "Misleading")
    ]
    start_node = "Piyassa"
    goal_node = "Bole Airport"
    print(f"{'Algorithm':<10} | {'Heuristic':<10} | {'Traversed ':<10} | {'Cost ':<6} | {'Paths'}")
    print("-" * 123)
    results = []
    for alg_name, heuristic, h_type in scenarios:
        if alg_name == "GBFS":
            res = greedy_best_first_search(ADJACENCY_LIST, heuristic, start_node, goal_node)
        else:
            res = a_star_search(ADJACENCY_LIST, heuristic, start_node, goal_node)

        if res:
            nodes_expanded = len(res['expansion_order'])
            path_str = " -> ".join(res['path'])
            print(f"{alg_name:<10} | {h_type:<10} | {nodes_expanded:<10} | {res['total_cost']:<6.1f} | {path_str}")
            results.append((alg_name, h_type, res))
        else:
            print(f"{alg_name:<10} | {h_type:<10} | {'NULL':<10} | {'NULL':<6} | {'NULL'}")

    return results
if __name__ == "__main__":
    run_experiments()
