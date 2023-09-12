class Node:
    def __init__(self,item):
        self.val=item
        self.left=None
        self.right=None
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

postorder(root)