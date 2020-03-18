import sys

class Node(object):
    data = None
    next = None

    def __init__(self,element):
        self.data = element
        self.next = None

class LinkedList(object):
    firstNode = None
    lastNode = None

    def createNodes(self, element):
        node = Node(element)
        if self.firstNode == None:
            self.firstNode = self.lastNode = node
        else:
            self.lastNode.next = node
        self.lastNode = node
        # print("id :",id(node))

    def displayNodes(self, node):
        tmp = node
        while tmp != None:
            print(tmp.data, "-->", end="")
            tmp = tmp.next
        print("None")

    def sizeOfList(self):
        length = 0
        tmp = self.firstNode
        while tmp != None:
            length = length + 1
            tmp = tmp.next
        print("Size of the LinkedList :",length)
        return length

    def nthNodeFromLast(self):
        # Accessing 2nd from the last of a list having 5 nodes.
        print("Enter the Node Number from the Last to be displayed.")
        nthfromlast = int(input())          # 2
        lengthoflist = list.sizeOfList()    # 5

        if nthfromlast > lengthoflist:
            print("Invalid Number")
            # sys.exit(0)
            return

        tmp = self.firstNode

        for i in range(1, lengthoflist-nthfromlast+1):
            tmp = tmp.next

        print(nthfromlast,"from the last is :",tmp.data)
        print()


# Driver Code
if __name__ == "__main__":
    list = LinkedList()

    print("First create some nodes.")
    print("========================",end="\n\n")

    option = -1

    while True:
        print("Select anyone option out of the given options.")
        print("1..Creation of Nodes")
        print("2..Display of Nodes")
        print("3..Go For Nth Node From Last ")
        print("4..Exit")
        print("\n")

        option = int(input())

        if option == 1:
            print("Enter as many elements as you want in the nodes.")
            while True:
                element = input()
                if element == "":
                    break
                list.createNodes(element)

        elif option == 2:
            list.displayNodes(list.firstNode)

        elif option == 3:
            list.nthNodeFromLast()

        elif option == 4:
            sys.exit(0)

        else:
            sys.exit("You have entered an invalid option.")