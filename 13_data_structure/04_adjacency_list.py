# Adjacency List Example
# Represents graph connections using a dictionary

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# Print all connections
print("Adjacency List:\n")

for node in graph:
    print(node, "->", graph[node])

# Show connections for one node
print("\nNodes connected to A:")
print(graph["A"])
