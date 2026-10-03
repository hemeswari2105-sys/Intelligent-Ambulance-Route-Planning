import streamlit as st
import time

from graph import get_graph, get_coordinates
from algorithms import bfs, ucs, astar


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Intelligent Ambulance Route Planning",
    page_icon="🚑",
    layout="wide"
)


# ============================================================
# LOAD GRAPH
# ============================================================

graph = get_graph()
coordinates = get_coordinates()

nodes = list(graph.keys())


# ============================================================
# HELPER FUNCTION - CREATE ROAD NETWORK VISUALIZATION
# ============================================================

def create_graphviz(
    graph,
    start,
    goal,
    blocked_edges,
    route
):
    """
    Creates a Graphviz representation of the road network.

    - Green = selected route
    - Red dashed = blocked road
    - Ambulance = start node
    - Hospital = goal node
    """

    dot = """
    graph RoadNetwork {

        layout=neato;
        overlap=false;
        splines=true;

        node [
            shape=circle,
            style=filled,
            fontname="Arial",
            fontsize=14
        ];

        edge [
            fontname="Arial",
            fontsize=11
        ];
    """

    # --------------------------------------------------------
    # Create nodes
    # --------------------------------------------------------

    for node in nodes:

        if node == start:

            dot += f'''
            "{node}" [
                label="🚑 {node}",
                shape=doublecircle,
                fillcolor="#90EE90",
                color="#008000",
                penwidth=3
            ];
            '''

        elif node == goal:

            dot += f'''
            "{node}" [
                label="🏥 {node}",
                shape=doublecircle,
                fillcolor="#FFB6B6",
                color="#B00000",
                penwidth=3
            ];
            '''

        else:

            dot += f'''
            "{node}" [
                label="{node}",
                fillcolor="#E8F1FA",
                color="#4A6FA5"
            ];
            '''

    # --------------------------------------------------------
    # Track roads so we don't draw duplicate edges
    # --------------------------------------------------------

    processed_edges = set()

    # --------------------------------------------------------
    # Create edges
    # --------------------------------------------------------

    for node, neighbors in graph.items():

        for neighbor, cost in neighbors.items():

            edge = tuple(sorted((node, neighbor)))

            if edge in processed_edges:
                continue

            processed_edges.add(edge)

            # Is this road blocked?
            if edge in blocked_edges:

                dot += f'''
                "{node}" -- "{neighbor}" [
                    label=" {cost} ",
                    color="#D00000",
                    style="dashed",
                    penwidth=3
                ];
                '''

            # Is this road part of selected route?
            elif (
                len(route) > 1
                and node in route
                and neighbor in route
            ):

                # Make sure the two nodes are consecutive
                node_index = route.index(node)
                neighbor_index = route.index(neighbor)

                if abs(node_index - neighbor_index) == 1:

                    dot += f'''
                    "{node}" -- "{neighbor}" [
                        label=" {cost} ",
                        color="#008000",
                        penwidth=5
                    ];
                    '''

                else:

                    dot += f'''
                    "{node}" -- "{neighbor}" [
                        label=" {cost} ",
                        color="#777777",
                        penwidth=2
                    ];
                    '''

            else:

                dot += f'''
                "{node}" -- "{neighbor}" [
                    label=" {cost} ",
                    color="#888888",
                    penwidth=1.5
                ];
                '''

    dot += "}"

    return dot


# ============================================================
# TITLE
# ============================================================

st.title("🚑 Intelligent Ambulance Route Planning Agent")

st.write(
    "Classical AI Search Algorithms for Emergency Route Planning"
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("🚑 Ambulance Configuration")


start = st.sidebar.selectbox(
    "Ambulance Starting Location",
    nodes,
    index=0
)


goal = st.sidebar.selectbox(
    "Hospital Location",
    nodes,
    index=len(nodes) - 1
)


algorithm = st.sidebar.selectbox(
    "Search Algorithm",
    [
        "BFS",
        "UCS",
        "A*"
    ]
)


# ============================================================
# BLOCKED ROADS
# ============================================================

st.sidebar.subheader("🚧 Blocked Roads")


roads = [
    "A-B",
    "A-D",
    "B-C",
    "B-E",
    "C-F",
    "D-E",
    "E-F",
    "F-H"
]


blocked_road_names = st.sidebar.multiselect(
    "Select blocked roads",
    roads
)


blocked_edges = set()


for road in blocked_road_names:

    first, second = road.split("-")

    blocked_edges.add(
        tuple(sorted((first, second)))
    )


# ============================================================
# FIND ROUTE BUTTON
# ============================================================

find_route = st.sidebar.button(
    "🚨 FIND BEST ROUTE",
    use_container_width=True
)


# ============================================================
# MAIN AREA
# ============================================================

st.subheader("🗺️ Road Network")


# Show initial network before route calculation

if not find_route:

    initial_graph = create_graphviz(
        graph,
        start,
        goal,
        blocked_edges,
        []
    )

    st.graphviz_chart(
        initial_graph,
        use_container_width=True
    )

    st.info(
        "Configure the ambulance and click "
        "**FIND BEST ROUTE** to calculate the route."
    )


# ============================================================
# FIND ROUTE
# ============================================================

if find_route:

    # --------------------------------------------------------
    # Validate locations
    # --------------------------------------------------------

    if start == goal:

        st.warning(
            "⚠️ Ambulance and hospital cannot be "
            "at the same location."
        )

    else:

        # ----------------------------------------------------
        # Start timer
        # ----------------------------------------------------

        start_time = time.perf_counter()


        # ----------------------------------------------------
        # Run selected algorithm
        # ----------------------------------------------------

        if algorithm == "BFS":

            result = bfs(
                graph,
                start,
                goal,
                blocked_edges
            )

        elif algorithm == "UCS":

            result = ucs(
                graph,
                start,
                goal,
                blocked_edges
            )

        else:

            result = astar(
                graph,
                coordinates,
                start,
                goal,
                blocked_edges
            )


        # ----------------------------------------------------
        # End timer
        # ----------------------------------------------------

        end_time = time.perf_counter()

        execution_time = end_time - start_time


        # ----------------------------------------------------
        # Check route
        # ----------------------------------------------------

        if not result["path"]:

            st.error(
                "❌ No valid route is available "
                "with the selected blocked roads."
            )

            # Show network even if no route exists

            graph_visual = create_graphviz(
                graph,
                start,
                goal,
                blocked_edges,
                []
            )

            st.graphviz_chart(
                graph_visual,
                use_container_width=True
            )

        else:

            route = result["path"]


            # ------------------------------------------------
            # Success message
            # ------------------------------------------------

            st.success(
                "✅ Route successfully calculated!"
            )


            # ------------------------------------------------
            # Visual Network
            # ------------------------------------------------

            st.subheader("🗺️ Calculated Route")


            graph_visual = create_graphviz(
                graph,
                start,
                goal,
                blocked_edges,
                route
            )


            st.graphviz_chart(
                graph_visual,
                use_container_width=True
            )


            # ------------------------------------------------
            # Recommended Route
            # ------------------------------------------------

            st.subheader("🚑 Recommended Route")


            route_text = " → ".join(route)


            st.info(route_text)


            # ------------------------------------------------
            # Metrics
            # ------------------------------------------------

            col1, col2, col3 = st.columns(3)


            with col1:

                st.metric(
                    "Total Road Cost",
                    result["cost"]
                )


            with col2:

                st.metric(
                    "Nodes Explored",
                    result["nodes_explored"]
                )


            with col3:

                st.metric(
                    "Execution Time",
                    f"{execution_time:.6f} sec"
                )


            # ------------------------------------------------
            # Route Details
            # ------------------------------------------------

            st.subheader("📊 Route Details")


            col1, col2 = st.columns(2)


            with col1:

                st.write(
                    f"**Algorithm:** {algorithm}"
                )

                st.write(
                    f"**Ambulance:** {start}"
                )

                st.write(
                    f"**Hospital:** {goal}"
                )


            with col2:

                if blocked_road_names:

                    st.write(
                        "**🚧 Blocked Roads:** "
                        + ", ".join(blocked_road_names)
                    )

                else:

                    st.write(
                        "**🚧 Blocked Roads:** None"
                    )

                st.write(
                    f"**Number of Stops:** {len(route) - 1}"
                )


            # ------------------------------------------------
            # Route Status
            # ------------------------------------------------

            st.subheader("🚨 Emergency Route Status")

            st.success(
                f"🚑 Ambulance can reach Hospital {goal} "
                f"through the calculated route."
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()
# ============================================================
# ALGORITHM COMPARISON
# ============================================================

st.divider()

st.subheader("📊 Algorithm Comparison")

st.write(
    "Compare BFS, UCS, and A* for the same ambulance "
    "route-planning scenario."
)


compare_algorithms = st.button(
    "🔬 COMPARE ALL ALGORITHMS",
    use_container_width=True
)


if compare_algorithms:

    # --------------------------------------------------------
    # Validate locations
    # --------------------------------------------------------

    if start == goal:

        st.warning(
            "⚠️ Ambulance and hospital cannot be "
            "at the same location."
        )

    else:

        comparison_results = []


        # ====================================================
        # BFS
        # ====================================================

        bfs_start = time.perf_counter()

        bfs_result = bfs(
            graph,
            start,
            goal,
            blocked_edges
        )

        bfs_end = time.perf_counter()

        bfs_time = bfs_end - bfs_start


        comparison_results.append({
            "Algorithm": "BFS",
            "Path": (
                " → ".join(bfs_result["path"])
                if bfs_result["path"]
                else "No route"
            ),
            "Cost": bfs_result["cost"],
            "Nodes Explored": bfs_result["nodes_explored"],
            "Execution Time (sec)": bfs_time
        })


        # ====================================================
        # UCS
        # ====================================================

        ucs_start = time.perf_counter()

        ucs_result = ucs(
            graph,
            start,
            goal,
            blocked_edges
        )

        ucs_end = time.perf_counter()

        ucs_time = ucs_end - ucs_start


        comparison_results.append({
            "Algorithm": "UCS",
            "Path": (
                " → ".join(ucs_result["path"])
                if ucs_result["path"]
                else "No route"
            ),
            "Cost": ucs_result["cost"],
            "Nodes Explored": ucs_result["nodes_explored"],
            "Execution Time (sec)": ucs_time
        })


        # ====================================================
        # A*
        # ====================================================

        astar_start = time.perf_counter()

        astar_result = astar(
            graph,
            coordinates,
            start,
            goal,
            blocked_edges
        )

        astar_end = time.perf_counter()

        astar_time = astar_end - astar_start


        comparison_results.append({
            "Algorithm": "A*",
            "Path": (
                " → ".join(astar_result["path"])
                if astar_result["path"]
                else "No route"
            ),
            "Cost": astar_result["cost"],
            "Nodes Explored": astar_result["nodes_explored"],
            "Execution Time (sec)": astar_time
        })


        # ====================================================
        # DISPLAY TABLE
        # ====================================================

        st.write(
            f"**Scenario:** {start} → {goal}"
        )


        if blocked_road_names:

            st.write(
                "**Blocked Roads:** "
                + ", ".join(blocked_road_names)
            )

        else:

            st.write(
                "**Blocked Roads:** None"
            )


        st.dataframe(
            comparison_results,
            use_container_width=True,
            hide_index=True
        )


        # ====================================================
        # PERFORMANCE CHART
        # ====================================================

        st.subheader("📈 Nodes Explored Comparison")


        chart_data = {
            "Algorithm": [
                item["Algorithm"]
                for item in comparison_results
            ],

            "Nodes Explored": [
                item["Nodes Explored"]
                for item in comparison_results
            ]
        }


        st.bar_chart(
            chart_data,
            x="Algorithm",
            y="Nodes Explored"
        )


        # ====================================================
        # COST COMPARISON
        # ====================================================

        st.subheader("💰 Route Cost Comparison")


        cost_data = {
            "Algorithm": [
                item["Algorithm"]
                for item in comparison_results
            ],

            "Route Cost": [
                item["Cost"]
                for item in comparison_results
            ]
        }


        st.bar_chart(
            cost_data,
            x="Algorithm",
            y="Route Cost"
        )


        # ====================================================
        # EXECUTION TIME
        # ====================================================

        st.subheader("⏱️ Execution Time Comparison")


        time_data = {
            "Algorithm": [
                item["Algorithm"]
                for item in comparison_results
            ],

            "Execution Time": [
                item["Execution Time (sec)"]
                for item in comparison_results
            ]
        }


        st.bar_chart(
            time_data,
            x="Algorithm",
            y="Execution Time"
        )

st.caption(
    "Intelligent Ambulance Route Planning Agent | "
    "BFS • UCS • A* | Classical Artificial Intelligence"
)