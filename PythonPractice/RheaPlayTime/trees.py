class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                print(str(lkpval)+" Not Found")
            else:
                return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                print(str(lkpval)+" Not Found")
            else:
                return self.right.findval(lkpval)
        else:
             print(str(lkpval) + " is found")

    # inOrderTraversal
    def traverseInOrder(root):
        if root:
            traverseInOrder(root.left)
            print(root.data)
            traverseInOrder(root.right)
    
    def PrintTree(self):
        if self is not None:
            print(self.data)

        if self.left:
            self.left.PrintTree()
        
        if self.right:
            self.right.PrintTree()

    def PrintTreeInOrder(self):
        if self.left:
            self.left.PrintTree()
        
        if self is not None:
            print(self.data)
        
        if self.right:
            self.right.PrintTree()
    
    def PrintTreePreOrder(self):
        if self is not None:
            print(self.data)

        if self.left:
            self.left.PrintTree()

        if self.right:
            self.right.PrintTree()

    def PrintTreePostOrder(self):
        if self.left:
            self.left.PrintTree()
        
        if self.right:
            self.right.PrintTree()
        
        if self is not None:
            print(self.data)

    def height(root, l_height, r_height):
        if root.left:
            l_height = l_height + 1
            return root.left.height(l_height, r_height)
        if root.right:
            r_height = r_height + 1
            return root.right.height(l_height, r_height)
        if l_height > r_height:
            return l_height
        else:
            return r_height

    def balancedtree(root, l_height, r_height):
        if root.left:
            l_height = l_height + 1
            root.left.balancedtree(l_height, r_height)
            l_height = l_height + 1
        if root.right:
            r_height = r_height + 1
            root.right.balancedtree(l_height, r_height)
            
        if l_height == r_height:
            return "yes, balanced tree"
        else:
            return "no, it's not a balanced tree"
    
    def leftTreeHeight(root, l_height):
        if root is not None:
            if root.left:
                l_height = l_height + 1
                return root.left.leftTreeHeight(l_height)
        return l_height

    def rightTreeHeight(root, r_height):
        if root is not None:
            if root.right:
                r_height = r_height + 1
                return root.right.rightTreeHeight(r_height)
        return r_height

root = Node(3)
root.insert(2)
root.insert(1)
root.insert(4)
root.insert(5)
print("printing a tree...")
root.PrintTree()
print("printing a tree in InOrder: L Root R")
root.PrintTreeInOrder()
print("printing a tree in PreOrder: Root L R")
root.PrintTreePreOrder()
print("printing a tree in PostOrder:L R Root")
root.PrintTreePostOrder()

print("finding if a given value exists")
root.findval(2)
root.findval(10)
print("find the height of the tree")
print(root.height(l_height=1, r_height=1))
print("Find if the tree is balanced")
print(root.balancedtree(l_height=1, r_height=1))
print("left tree max height")
print(root.leftTreeHeight(l_height=0))
print("right tree max height")
print(root.rightTreeHeight(r_height=0))

#traverseInOrder(node)