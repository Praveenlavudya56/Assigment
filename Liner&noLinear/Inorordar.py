class Node:
    def __init__(self,item):
        self.val=item
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right) 

root=Node("A")
root.left=Node("F")
root.left.left=Node("Y")
root.right=Node('K')
root.right.right=Node('T')
root.left.right=Node('X')

inorder(root)