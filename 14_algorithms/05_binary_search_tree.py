# Binary Search Tree Example

class Node:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None


def binary_tree_search(node, target):

    # Value not found
    if node is None:

        return False

    print(f"Checking node: {node.value}")

    # Target found
    if node.value == target:

        return True

    # Move left
    elif target < node.value:

        return binary_tree_search(node.left, target)

    # Move right
    else:

        return binary_tree_search(node.right, target)


# Create Binary Search Tree

root = Node(18)

root.left = Node(4)
root.right = Node(32)

root.left.right = Node(6)

root.left.right.left = Node(5)
root.left.right.right = Node(15)


# Search for value

target = 15

found = binary_tree_search(root, target)

if found:

    print(f"{target} found in tree")

else:

    print("Value not found")
