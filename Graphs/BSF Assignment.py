from collections import deque

# Define a class for the tree node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to perform BFS traversal using a deque
def bfs(root):
    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()  # Dequeue the first node in the queue
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Construct a sample binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform BFS traversal on the tree
result = bfs(root)
print(result)  # Output should be [1, 2, 3, 4, 5]
