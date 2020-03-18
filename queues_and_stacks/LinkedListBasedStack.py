class Node():
    def __init__(self,data):
        self.next = None
        self.data = data

class LinkedListStack():
    topNode = None
    topOfStack = -1

    def push(self,data):
        node = Node(data)
        if self.topOfStack == -1:
            self.topNode = node
            self.topOfStack = self.topOfStack + 1
            print(data,"pushed into stack")
            # print("topNode",id(self.topNode))
            # print("node",id(node))
        else:
            node.next = self.topNode
            self.topNode = node
            self.topOfStack = self.topOfStack + 1
            print(data, "pushed into stack")
            # print("topNode", id(self.topNode))
            # print("node", id(node))

    def stackStatus(self):
        currentNode = self.topNode
        while currentNode != None:
            print(currentNode.data,"-->",end="")
            currentNode = currentNode.next
        print("None")

    def pop(self):
        currentNode = self.topNode
        self.topNode = currentNode.next
        self.topOfStack = self.topOfStack - 1

    def size(self):
        print("size of the stack :",self.topOfStack+1)

    def peek(self):
        print("Peek Element is :",self.topNode.data)

if __name__=="__main__":
    stack = LinkedListStack()

    print("Put elements into Stack.")
    while True:
        element = input()
        if element == "":
            break;
        else:
            stack.push(element)

    print()
    stack.stackStatus()
    print()
    stack.size()
    print()
    print("after one pop()")
    stack.pop()
    print()
    stack.peek()
    print()
    stack.stackStatus()
    print()
    stack.size()