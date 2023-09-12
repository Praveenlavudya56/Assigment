class Node:
    def __init__(self,item):
        self.val=item
        self.left=None
        self.right=None
def Preorder(root):
    if root is not None:
        print(root.val)
        Preorder(root.left)
        Preorder(root.right)
        

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


root=Node("A")
root.left=Node("F")
root.left.left=Node("Y")
root.right=Node('K')
root.right.right=Node('T')
root.left.right=Node('X')

# Preorder(root)
print('-------------------')
inorder(root)
print('-------------------')
postorder(root)