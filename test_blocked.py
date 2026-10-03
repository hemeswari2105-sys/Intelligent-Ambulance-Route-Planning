from graph import get_graph, get_coordinates
from algorithms import bfs, ucs, astar


graph = get_graph()
coordinates = get_coordinates()


# ============================================================
# BLOCKED ROAD
# ============================================================

blocked_edges = {
    tuple(sorted(("E", "F")))
}


print("=" * 60)
print("🚑 AMBULANCE ROUTE PLANNING")
print("=" * 60)

print()
print("Start      : A")
print("Hospital   : H")
print("Blocked    : E -> F")
print()


# ============================================================
# BFS
# ============================================================

bfs_result = bfs(
    graph,
    "A",
    "H",
    blocked_edges
)

print("BFS")
print("-" * 30)
print("Path:", " -> ".join(bfs_result["path"]))
print("Cost:", bfs_result["cost"])
print("Nodes Explored:", bfs_result["nodes_explored"])


# ============================================================
# UCS
# ============================================================

ucs_result = ucs(
    graph,
    "A",
    "H",
    blocked_edges
)

print()
print("UCS")
print("-" * 30)
print("Path:", " -> ".join(ucs_result["path"]))
print("Cost:", ucs_result["cost"])
print("Nodes Explored:", ucs_result["nodes_explored"])


# ============================================================
# A*
# ============================================================

astar_result = astar(
    graph,
    coordinates,
    "A",
    "H",
    blocked_edges
)

print()
print("A*")
print("-" * 30)
print("Path:", " -> ".join(astar_result["path"]))
print("Cost:", astar_result["cost"])
print("Nodes Explored:", astar_result["nodes_explored"])


print()
print("=" * 60)
print("🚧 BLOCKED ROAD HANDLED")
print("=" * 60)









