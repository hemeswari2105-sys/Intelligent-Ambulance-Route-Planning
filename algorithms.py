from collections import deque
import heapq


# ============================================================
# BREADTH-FIRST SEARCH (BFS)
# ============================================================

def bfs(graph, start, goal, blocked_edges=None):

    if blocked_edges is None:
        blocked_edges = set()

    queue = deque()

    # Store:
    # (current node, path, total cost)
    queue.append((start, [start], 0))

    visited = set()

    nodes_explored = 0

    while queue:

        current, path, cost = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        # Goal reached
        if current == goal:
            return {
                "path": path,
                "cost": cost,
                "nodes_explored": nodes_explored
            }

        # Explore neighboring roads
        for neighbor, edge_cost in graph[current].items():

            # Represent road consistently
            edge = tuple(sorted((current, neighbor)))

            # Skip blocked road
            if edge in blocked_edges:
                continue

            if neighbor not in visited:

                queue.append(
                    (
                        neighbor,
                        path + [neighbor],
                        cost + edge_cost
                    )
                )

    # No route found
    return {
        "path": [],
        "cost": float("inf"),
        "nodes_explored": nodes_explored
    }


# ============================================================
# UNIFORM COST SEARCH (UCS)
# ============================================================

def ucs(graph, start, goal, blocked_edges=None):

    if blocked_edges is None:
        blocked_edges = set()

    # Priority queue:
    # (total_cost, current_node, path)

    priority_queue = []

    heapq.heappush(
        priority_queue,
        (0, start, [start])
    )

    # Lowest known cost to each node
    best_cost = {}

    nodes_explored = 0

    while priority_queue:

        current_cost, current, path = heapq.heappop(
            priority_queue
        )

        # Ignore a more expensive route
        if (
            current in best_cost
            and current_cost > best_cost[current]
        ):
            continue

        best_cost[current] = current_cost

        nodes_explored += 1

        # Goal reached
        if current == goal:
            return {
                "path": path,
                "cost": current_cost,
                "nodes_explored": nodes_explored
            }

        # Explore neighboring roads
        for neighbor, edge_cost in graph[current].items():

            # Represent road consistently
            edge = tuple(sorted((current, neighbor)))

            # Skip blocked road
            if edge in blocked_edges:
                continue

            new_cost = current_cost + edge_cost

            # Add route if it is cheaper
            if (
                neighbor not in best_cost
                or new_cost < best_cost[neighbor]
            ):

                heapq.heappush(
                    priority_queue,
                    (
                        new_cost,
                        neighbor,
                        path + [neighbor]
                    )
                )

    # No route found
    return {
        "path": [],
        "cost": float("inf"),
        "nodes_explored": nodes_explored
    }


# ============================================================
# A* SEARCH
# ============================================================

def heuristic(coordinates, node, goal):
    """
    Calculate the Euclidean distance between
    the current node and the goal.

    h(n) = estimated cost from node to goal
    """

    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]

    distance = (
        (x1 - x2) ** 2 +
        (y1 - y2) ** 2
    ) ** 0.5

    return distance


def astar(graph, coordinates, start, goal, blocked_edges=None):

    if blocked_edges is None:
        blocked_edges = set()

    # Priority queue:
    #
    # (f_score, g_score, current_node, path)
    #
    # f(n) = g(n) + h(n)

    priority_queue = []

    initial_h = heuristic(
        coordinates,
        start,
        goal
    )

    heapq.heappush(
        priority_queue,
        (
            initial_h,
            0,
            start,
            [start]
        )
    )

    # Lowest known g(n) cost
    best_cost = {}

    nodes_explored = 0

    while priority_queue:

        f_score, current_cost, current, path = heapq.heappop(
            priority_queue
        )

        # Ignore a more expensive route
        if (
            current in best_cost
            and current_cost > best_cost[current]
        ):
            continue

        best_cost[current] = current_cost

        nodes_explored += 1

        # Goal reached
        if current == goal:
            return {
                "path": path,
                "cost": current_cost,
                "nodes_explored": nodes_explored
            }

        # Explore neighboring roads
        for neighbor, edge_cost in graph[current].items():

            # Represent road consistently
            edge = tuple(sorted((current, neighbor)))

            # Skip blocked road
            if edge in blocked_edges:
                continue

            # g(n)
            new_cost = current_cost + edge_cost

            # h(n)
            h = heuristic(
                coordinates,
                neighbor,
                goal
            )

            # f(n) = g(n) + h(n)
            new_f_score = new_cost + h

            # Add route if it is cheaper
            if (
                neighbor not in best_cost
                or new_cost < best_cost[neighbor]
            ):

                heapq.heappush(
                    priority_queue,
                    (
                        new_f_score,
                        new_cost,
                        neighbor,
                        path + [neighbor]
                    )
                )

    # No route found
    return {
        "path": [],
        "cost": float("inf"),
        "nodes_explored": nodes_explored
    }


















