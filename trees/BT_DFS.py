class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def dfs(node):
  """
  Performs a Depth First Search on a binary tree.

  Args:
    node: The current node being explored.
  """
  if node:
    print(node.value)
    dfs(node.left)
    dfs(node.right)

#example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

dfs(root)
