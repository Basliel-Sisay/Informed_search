import math
COORDINATES ={
    "Piyassa": (0, 5),
    "Arat Kilo": (2, 6),
    "6 Kilo": (3, 8),
    "Kazanchis": (4, 5),
    "Meskel Square": (4, 2),
    "Mexico Square": (1, 2),
    "Bole Edna Mall": (8, 3),
    "Bole Airport": (10, 0),
    "Gotera": (6, 0),
    "Megenagna": (9, 7)
}
ADJACENCY_LIST ={
    "Piyassa": [("Arat Kilo", 1.5), ("Mexico Square", 2.2)],
    "Arat Kilo": [("Piyassa", 1.5), ("6 Kilo", 1.2), ("Kazanchis", 1.8)],
    "6 Kilo": [("Arat Kilo", 1.2), ("Megenagna", 4.5)],
    "Kazanchis": [("Arat Kilo", 1.8), ("Meskel Square", 1.4), ("Megenagna", 3.8)],
    "Meskel Square": [("Kazanchis", 1.4), ("Mexico Square", 1.8), ("Gotera", 2.8), ("Bole Edna Mall", 3.2)],
    "Mexico Square": [("Piyassa", 2.2), ("Meskel Square", 1.8)],
    "Bole Edna Mall": [("Meskel Square", 3.2), ("Bole Airport", 2.1), ("Megenagna", 2.9)],
    "Bole Airport": [("Bole Edna Mall", 2.1), ("Gotera", 4.2)],
    "Gotera": [("Meskel Square", 2.8), ("Bole Airport", 4.2)],
    "Megenagna": [("6 Kilo", 4.5), ("Kazanchis", 3.8), ("Bole Edna Mall", 2.9)]
}
def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
GOAL = "Bole Airport"
GOOD_HEURISTIC = {node: round(calculate_euclidean_distance(coords, COORDINATES[GOAL]), 2) 
                  for node, coords in COORDINATES.items()}
MISLEADING_HEURISTIC = {
    "Piyassa": 1.0,      
    "Arat Kilo": 2.0,    
    "6 Kilo": 12.0,     
    "Kazanchis": 10.0,    
    "Mexico Square": 1.5,
    "Meskel Square": 8.0, 
    "Gotera": 0.5,      
    "Megenagna": 1.2,    
    "Bole Edna Mall": 9.0, 
    "Bole Airport": 0.0
}
if __name__ == "__main__":
    print("Coordinates:", COORDINATES)
    print("\nCalculated Good Heuristic (Euclidean): ")
    for node, h in GOOD_HEURISTIC.items():
        print(f"{node}: {h}")
