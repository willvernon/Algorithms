# using modified Depth-First Search
#
def topological_sort_dfs(graph):
    """
    Performs topological sort on a DAG using Depth-First Search.

    Args:
        graph: A dictionary where keys are nodes and values are lists of outgoing neighbors.

    Returns:
        A list of nodes in topological order.
    """
    visited = set()
    sorted_order = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        sorted_order.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return sorted_order

# Example usage
# graph
#   a 
#  / \
# b   c 
# |   |
# d   f 
# |
# e 
graph = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["f"],
    "d": [],
    "e": ["f"],
    "f": []
}

sorted_nodes = topological_sort_dfs(graph)

print("Topological order:", sorted_nodes)
