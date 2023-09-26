class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

def inorder(root):
    if not root:
        return []
    
    stack = []
    result = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    
    return result

def postorder(root):
    if not root:
        return []
    
    stack1 = [root]
    stack2 = []
    result = []
    
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    while stack2:
        result.append(stack2.pop().value)
    
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Preorder :", preorder(root))
print("Inorder  :", inorder(root))
print("Postorder:", postorder(root))
