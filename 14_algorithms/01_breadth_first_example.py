from collections import deque

graph = {
    "S": ["A", "D"],
    "A": ["B", "C"],
    "D": ["E", "F"],
    "B": [],
    "C": [],
    "E": [],
    "F": []
}

def bfs(start_node):

    visited = []
    queue = deque()

    visited.append(start_node)
    queue.append(start_node)

    while queue:

        current = queue.popleft()
        print(current)

        for neighbour in graph[current]:

            if neighbour not in visited:

                visited.append(neighbour)
                queue.append(neighbour)

bfs("S")
