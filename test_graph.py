from graph import get_graph

graph = get_graph()

print("Road Network:")
print()

for node, connections in graph.items():
    print(node, "->", connections)