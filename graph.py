

# graph.py

# Road network represented as a weighted graph
# Each node represents an intersection/location.
# Each edge represents a road.
# Edge weight represents the road cost/distance.

GRAPH = {
    "A": {
        "B": 2,
        "D": 4
    },

    "B": {
        "A": 2,
        "C": 3,
        "E": 2
    },

    "C": {
        "B": 3,
        "F": 1
    },

    "D": {
        "A": 4,
        "E": 1
    },

    "E": {
        "B": 2,
        "D": 1,
        "F": 2
    },

    "F": {
        "C": 1,
        "E": 2,
        "H": 3
    },

    "H": {
        "F": 3
    }
}


# Coordinates for A* heuristic
# These are simulated coordinates for our road network.

COORDINATES = {
    "A": (0, 0),
    "B": (2, 0),
    "C": (5, 0),
    "D": (0, -3),
    "E": (2, -3),
    "F": (5, -3),
    "H": (5, -6)
}


def get_graph():
    return GRAPH


def get_coordinates():
    return COORDINATES