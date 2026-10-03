# 🚑 Intelligent Ambulance Route Planning Agent

An intelligent route-planning system that uses classical AI search algorithms to determine efficient ambulance routes from a starting location to a hospital while dynamically handling blocked roads.

## 📌 Project Overview

The **Intelligent Ambulance Route Planning Agent** models a road network as a weighted graph and applies classical Artificial Intelligence search algorithms to find routes between an ambulance location and a hospital.

The system supports:

- **Breadth-First Search (BFS)**
- **Uniform Cost Search (UCS)**
- **A\* Search**
- Blocked-road handling
- Route cost calculation
- Nodes explored measurement
- Execution-time measurement
- Algorithm comparison
- Interactive Streamlit interface

The project demonstrates how an intelligent agent can perceive a road environment, reason using search algorithms, and select a route toward the hospital.

---

## 🎯 Problem Statement

During emergency situations, ambulances need to reach hospitals efficiently. Road closures or blocked roads can make a previously selected route unavailable.

This project develops an intelligent route-planning agent that:

1. Represents roads as a graph.
2. Identifies available routes.
3. Handles blocked roads.
4. Searches for a route from the ambulance to the hospital.
5. Compares different AI search algorithms.
6. Provides the selected route, cost, and search performance.

---

## 🎯 Objectives

- Model a road network using a weighted graph.
- Implement BFS, UCS, and A\* search algorithms.
- Find routes from ambulance location **A** to hospital **H**.
- Dynamically avoid blocked roads.
- Compare algorithm performance.
- Provide an interactive visualization using Streamlit.

---

## 🧠 AI Algorithms

### 1. Breadth-First Search (BFS)

**BFS — Breadth-First Search**

BFS explores the graph level by level and finds a path with the minimum number of edges.

In this project, BFS is used as a baseline search algorithm.

### 2. Uniform Cost Search (UCS)

**UCS — Uniform Cost Search**

UCS expands the node with the lowest accumulated path cost.

It is suitable for weighted road networks because different roads can have different costs.

### 3. A* Search

**A\* — A-Star Search**

A\* combines the actual cost from the starting point with an estimated cost to the goal.

It uses:

**f(n) = g(n) + h(n)**

where:

- `g(n)` = cost from the start node to the current node
- `h(n)` = estimated cost from the current node to the goal
- `f(n)` = total estimated cost

A\* can reduce the number of nodes explored when an appropriate heuristic is available.

---

## 🗺️ Road Network

The project uses the following weighted road network:

```text
             2              3
        A -------- B --------------- C
        |          |                  |
        | 4        | 2                | 1
        |          |                  |
        D -------- E --------------- F -------- H
             1              2              3
```

### Nodes

| Node | Meaning |
|------|---------|
| A | Ambulance starting location |
| B | Road intersection |
| C | Road intersection |
| D | Road intersection |
| E | Road intersection |
| F | Road intersection |
| H | Hospital / destination |

### Edge Costs

| Road | Cost |
|------|------|
| A-B | 2 |
| A-D | 4 |
| B-C | 3 |
| B-E | 2 |
| D-E | 1 |
| C-F | 1 |
| E-F | 2 |
| F-H | 3 |

---

## 🚧 Blocked Road Handling

The system allows roads to be marked as blocked.

When a road is blocked, the search algorithms ignore that edge and calculate an alternative route.

For example:

```text
Normal:

A → B → E → F → H

If E-F is blocked:

A → B → C → F → H
```

This allows the ambulance agent to adapt to changing road conditions.

---

## 🔄 Agent Workflow

```text
Environment
     ↓
Perceive Road Network
     ↓
Identify Start & Hospital
     ↓
Check Blocked Roads
     ↓
Select Search Algorithm
     ↓
Search Available Routes
    
































