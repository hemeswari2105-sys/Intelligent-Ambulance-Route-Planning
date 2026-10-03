from graph import get_graph, get_coordinates
from algorithms import bfs, ucs, astar
import time


# ============================================================
# LOAD GRAPH
# ============================================================

graph = get_graph()
coordinates = get_coordinates()


START = "A"
GOAL = "H"


# ============================================================
# TEST SCENARIOS
# ============================================================

scenarios = [
    {
        "name": "Normal Road Network",
        "blocked": set()
    },
    {
        "name": "A-B Blocked",
        "blocked": {
            tuple(sorted(("A", "B")))
        }
    },
    {
        "name": "E-F Blocked",
        "blocked": {
            tuple(sorted(("E", "F")))
        }
    },
    {
        "name": "A-B and B-E Blocked",
        "blocked": {
            tuple(sorted(("A", "B"))),
            tuple(sorted(("B", "E")))
        }
    },
    {
        "name": "A-B and E-F Blocked",
        "blocked": {
            tuple(sorted(("A", "B"))),
            tuple(sorted(("E", "F")))
        }
    },
    {
        "name": "D-E Blocked",
        "blocked": {
            tuple(sorted(("D", "E")))
        }
    }
]


# ============================================================
# HELPER FUNCTION
# ============================================================

def run_algorithm(name, blocked_edges):

    start_time = time.perf_counter()

    if name == "BFS":

        result = bfs(
            graph,
            START,
            GOAL,
            blocked_edges
        )

    elif name == "UCS":

        result = ucs(
            graph,
            START,
            GOAL,
            blocked_edges
        )

    else:

        result = astar(
            graph,
            coordinates,
            START,
            GOAL,
            blocked_edges
        )

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    if result["path"]:

        path = " -> ".join(result["path"])

    else:

        path = "NO ROUTE"

    return {
        "path": path,
        "cost": result["cost"],
        "nodes": result["nodes_explored"],
        "time": execution_time
    }


# ============================================================
# MAIN EXPERIMENT
# ============================================================

print()
print("=" * 100)
print("INTELLIGENT AMBULANCE ROUTE PLANNING")
print("ALGORITHM PERFORMANCE EXPERIMENT")
print("=" * 100)

print()
print(f"Start Location : {START}")
print(f"Hospital       : {GOAL}")
print()


# ============================================================
# RUN ALL SCENARIOS
# ============================================================

for scenario_number, scenario in enumerate(
    scenarios,
    start=1
):

    print()
    print("-" * 100)

    print(
        f"SCENARIO {scenario_number}: "
        f"{scenario['name']}"
    )

    print("-" * 100)

    blocked = scenario["blocked"]

    if blocked:

        blocked_display = ", ".join(
            f"{edge[0]}-{edge[1]}"
            for edge in sorted(blocked)
        )

        print(
            f"Blocked Roads : {blocked_display}"
        )

    else:

        print(
            "Blocked Roads : None"
        )

    print()

    print(
        f"{'Algorithm':<12}"
        f"{'Path':<35}"
        f"{'Cost':<10}"
        f"{'Nodes':<10}"
        f"{'Time (sec)':<15}"
    )

    print("-" * 100)


    # --------------------------------------------------------
    # BFS
    # --------------------------------------------------------

    bfs_result = run_algorithm(
        "BFS",
        blocked
    )

    print(
        f"{'BFS':<12}"
        f"{bfs_result['path']:<35}"
        f"{bfs_result['cost']:<10}"
        f"{bfs_result['nodes']:<10}"
        f"{bfs_result['time']:.8f}"
    )


    # --------------------------------------------------------
    # UCS
    # --------------------------------------------------------

    ucs_result = run_algorithm(
        "UCS",
        blocked
    )

    print(
        f"{'UCS':<12}"
        f"{ucs_result['path']:<35}"
        f"{ucs_result['cost']:<10}"
        f"{ucs_result['nodes']:<10}"
        f"{ucs_result['time']:.8f}"
    )


    # --------------------------------------------------------
    # A*
    # --------------------------------------------------------

    astar_result = run_algorithm(
        "A*",
        blocked
    )

    print(
        f"{'A*':<12}"
        f"{astar_result['path']:<35}"
        f"{astar_result['cost']:<10}"
        f"{astar_result['nodes']:<10}"
        f"{astar_result['time']:.8f}"
    )


print()
print("=" * 100)
print("EXPERIMENT COMPLETED")
print("=" * 100)
print()















