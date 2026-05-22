
# Set up the nodes.
# What pattern do you notice?
# How would you add more nodes to this tree?
graph = {
    "S": ["A", "D"],
    "A": ["B", "C"],
    "D": ["E", "F"],
    "B": ["G"],
    "C": [],
    "E": [],
    "F": [],
    "G": []
}

def dfs(start_node):

    visited = []
    stack = []

    stack.append(start_node)

    while stack:

        current = stack.pop()

        if current not in visited:

            print(current)
            visited.append(current)

            # Reverse keeps traversal visually left-to-right
            for neighbour in reversed(graph[current]):

                stack.append(neighbour)

dfs("S")
