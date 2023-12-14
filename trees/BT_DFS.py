class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

def dfs(node, visited=None):
    if visited is None:
        visited = []
    visited.append(node.data)

    for child in node.children:
        if child.data not in visited:
            dfs(child, visited)

    return visited

# Example usage
root = Node(1)
root.children.append(Node(2))
root.children.append(Node(3))
root.children[0].children.append(Node(4))
root.children[0].children.append(Node(5))

print("DFS traversal:", dfs(root))
