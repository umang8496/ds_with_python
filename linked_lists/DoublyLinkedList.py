class Node(object):
    def __init__(self,data):
        self.data = data
        self.forward = None
        self.backward = None

class MyList(object):
    headNode = None
    lastNode = None

    def insert(self,data):
        node = Node(data)
        if self.headNode is None:
            self.headNode = self.lastNode = node
            self.headNode.forward = self.headNode.backward = None
            self.lastNode.forward = self.lastNode.backward = None
        else:
            self.lastNode.forward = node
            node.backward = self.lastNode
            node.forward = None
        self.lastNode = node

    def forwardTraversing(self):
        print()
        print("here is the list elements in insertion order")
        currentNode = self.headNode
        while currentNode != None:
            print(currentNode.data,"-->",end=" ")
            currentNode = currentNode.forward
        print("None")

    def backwardTraversing(self):
        print()
        print("here is the list elements in reverse order")
        currentNode = self.lastNode
        while currentNode != None:
            print(currentNode.data,"-->",end=" ")
            currentNode = currentNode.backward
        print("None")

    def size(self):
        count = 0
        currentNode = self.headNode
        while currentNode != None:
            count = count + 1
            currentNode = currentNode.forward
        print("size of the list :",count)

if __name__ == "__main__":
    list = MyList()
    print("Enter as many nodes in the list as you want...")

    while True:
        element = input()
        if element == "":
            break
        else:
            list.insert(int(element))

    list.forwardTraversing()
    list.backwardTraversing()
    list.size()