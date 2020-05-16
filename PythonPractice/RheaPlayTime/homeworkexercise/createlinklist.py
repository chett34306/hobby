class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
    
    def InsertNode(root, data):
        nextNode = Node(data)
        self.next = nextNode
        
def printlinklist(root):
    while root:
        print(root.data)
        root = root.next
def isCircularLinklist(root):
    head = root
    while root:
        if head == root.next:
            print ("yes circular link list")
            return
        else:
            root = root.next
    print("not circular linklist")
        

linklist = Node(1)
second =  Node(3)
third = Node(4)
fourth = Node(2)
linklist.next = second
second.next = third
third.next = fourth
fourth.next = linklist
print("printing the linklist")
# printlinklist(linklist)

print("print if the given list is circular or not")
# isCircularLinklist(linklist)