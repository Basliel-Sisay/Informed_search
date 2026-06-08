from runner import run_experiments
if __name__ == "__main__":
    print("-" * 123)
    print("Informed Search AI Group Project: Addis Ababa")
    print("-" * 123)
    results = run_experiments()
    print("-" * 123)
    print("Detailed Expansion Order for each scenario: ")
    for alg, h_type, res in results:
        print(f"\n[{alg} - {h_type} Heuristic]")
        print(f"Location Checked: {' -> '.join(res['expansion_order'])}")
        print(f"Selected Route: {' -> '.join(res['path'])}")
        print(f"Total Path Cost: {res['total_cost']}")
