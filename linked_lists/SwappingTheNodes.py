# This program swaps the nodes by taking the inputs from the user.

# Input:  10->15->12->13->20->14,  x = 12, y = 20
# Output: 10->15->20->13->12->14
#
# Input:  10->15->12->13->20->14,  x = 10, y = 20
# Output: 20->15->12->13->10->14
#
# Input:  10->15->12->13->20->14,  x = 12, y = 13
# Output: 10->15->13->12->20->14

import sys

class Node(object):
    data = None
    next = None

    def __init__(self,element):
        data = element
        next = None

class LinkedList(object):
    firstNode = None
    lastNode = None
    length = 0
    currentposition = 0

    def createNodes(self,element):
        node = Node(element)
        if self.firstNode == None:
            self.firstNode = self.lastNode = node
        else:
            self.lastNode.next = node
        self.lastNode = node

    def displayNodes(self,node):
        while node != None:
            print(node.data,"-->",end="")
            node = node.next
        print("None")

    def sizeOfList(self,node):
        while node != None:
            self.length = self.length + 1
            node = node.next
        return self.length

    def checkForValue(self,value):
        tmp = self.firstNode

        while tmp != None:
            self.currentposition = self.currentposition + 1
            if tmp.data == value:
                print(value,"present inside the list at the position :",self.currentposition)
                return self.currentposition
            tmp = tmp.next

        print(value,"not present inside the list")
        return -1

    def getNodeReference(self,val):
        tmp = self.firstNode
        while tmp != None:
            if tmp.data == val:
                return tmp
            tmp = tmp.next

    def exchangeNodes(self,p,q):
        pass


if __name__ == "__main__":
    list = LinkedList()

    print("Enter as many nodes as you want")
    while True:
        element = input()
        if element == "":
            break
        list.createNodes(element)

    list.displayNodes(list.firstNode)

    val1 = input("Enter the first value to be exchanged")
    val2 = input("Enter the second value to be exchanged")

    # Now Check for the availability of the values by fetching the current positions of the values
    presence1 = list.checkForValue(val1)
    presence2 = list.checkForValue(val2)

    if presence1 != -1 and presence2 != -1:
        p = list.getNodeReference(val1)
        q = list.getNodeReference(val2)

        list.exchangeNodes(p,q)
    else:
        print("Entered values are not sufficient to carry out the operation")
        sys.exit(0)