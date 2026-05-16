# Adjacency Matrix Example
# Represents connections between nodes using a 2D list

# Nodes:
# A = 0
# B = 1
# C = 2
# D = 3

adjacency_matrix = [
    #A B C D
    [0, 1, 1, 0],  # A
    [1, 0, 0, 1],  # B
    [1, 0, 0, 1],  # C
    [0, 1, 1, 0]   # D
]

# Print the matrix
print("Adjacency Matrix:")
for row in adjacency_matrix:
    print(row)

# Check if two nodes are connected
node1 = 0  # A
node2 = 2  # C

if adjacency_matrix[node1][node2] == 1:
    print("\nA and C are connected")
else:
    print("\nA and C are not connected")
