from graph import get_graph
from algorithms import ucs


graph = get_graph()

result = ucs(
    graph,
    "A",
    "H"
)

print("UCS RESULT")
print("-----------")

print("Path:", " -> ".join(result["path"]))
print("Cost:", result["cost"])
print("Nodes Explored:", result["nodes_explored"])