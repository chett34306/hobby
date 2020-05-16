import queue
class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    # Left, Root, Right
def inOrder(root): 
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

    # Root, Left, Right
def preOrder(root):
    if root:
        print(root.data)
        inOrder(root.left)
        inOrder(root.right)

    # Left, Right, Root
def postOrder(root):
    if root:
        inOrder(root.left)
        inOrder(root.right)
        print(root.data)

q = queue.Queue()

def levelOrder(root):
    
    if root is None:
        return
    if root.left:
        q.put(root.left)
    if root.right:
        q.put(root.right)
    if q.empty():
        return
    else:
        root = q.get()
        print(root.data)
    levelOrder(root)
            


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
"""print("In order traversal")
inOrder(root)
print("Pre order traversal")
preOrder(root)
print("Post order traversal")
postOrder(root)"""
print("traverse level order or breadthwise")
print(root.data)
levelOrder(root)
print("Hi")
