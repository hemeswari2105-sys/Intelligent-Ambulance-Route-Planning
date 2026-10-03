from graph import get_graph
from algorithms import bfs

graph = get_graph()

result = bfs(
    graph,
    "A",
    "H"
)

print("BFS RESULT")
print("-----------")

print("Path:", " -> ".join(result["path"]))
print("Cost:", result["cost"])
print("Nodes Explored:", result["nodes_explored"])

