from graph import get_graph, get_coordinates
from algorithms import astar


graph = get_graph()
coordinates = get_coordinates()

result = astar(
    graph,
    coordinates,
    "A",
    "H"
)

print("A* RESULT")
print("----------")

print("Path:", " -> ".join(result["path"]))
print("Cost:", result["cost"])
print("Nodes Explored:", result["nodes_explored"])








