class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    """
    Performs a Breadth First Search on a binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of nodes visited in order.
    """
    visited = []
    queue = [root]

    while queue:
        current_node = queue.pop(0)
        visited.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return visited

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

visited_nodes = bfs(root)
print("BFS traversal:", visited_nodes)

# 1) Initialization
# - `visited` is an empty list to store the values of visited nodes.
# - `queue` is a list containing the root node of the tree.

# 2) Loop condition:
# - `current_node` is assigned the first element of the queue by `pop(0)`.
#   This removes the element from the queue while also getting its value.
# - The value of `current_node` is appended to the `visited` list, marking it as visited.

# 4) Exploring children:
# - If the `left` child of `current_node` exists, it is appended to the queue.
#   This ensures that the left child will be visited in the next iteration of the loop.
# - Similarly, the same goes for the `right` child if it exists. 
#   This allows the BFS algo to explore the left and right subtrees level by level.

# 5) Loop Continuation:
# - The loop continues with the next element in the queue.
#   This ensures that all nodes at the current level are visited before moving to next level.


