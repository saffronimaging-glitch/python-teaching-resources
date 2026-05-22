graph = {
    "S": ["A", "D"],
    "A": ["B", "C"],
    "D": ["E", "F"],
    "B": [],
    "C": [],
    "E": [],
    "F": []
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
