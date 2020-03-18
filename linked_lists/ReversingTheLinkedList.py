import sys
# for sys.exit(0)


class Node(object):
    data = None
    next = None

    def __init__(self,element):
        self.data = element
        self.next = None


class LinkedList(object):
    firstNode = None
    lastNode = None

    def createNodes(self,element):
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
            print(tmp.data,"-->",end="")
            tmp = tmp.next
        print("None")

    def reverseByIteration(self,MyNode):
        p = None
        while MyNode :
            q = MyNode.next
            MyNode.next = p
            p = MyNode
            MyNode = q

        return p

    def reverseByRecursion(self,MyNode):
        if not MyNode:
            return None

        elif MyNode.next:
            head = self.reverseByRecursion(MyNode.next)
            MyNode.next.next = MyNode
            MyNode.next = None
            return head

        else:
            return MyNode

    def sizeOfList(self):
        length = 0
        tmp = self.firstNode
        while tmp != None:
            length = length + 1
            tmp = tmp.next
        print("Size of the LinkedList :",length)
        return length


# Driver Code
if __name__ == "__main__":
    list = LinkedList()
    option = -1

    while True:
        print("\n")
        print("Select anyone option out of the given options.")
        print("1..Creation of Nodes")
        print("2..Display of Nodes")
        print("3..ReversingByIteration")
        print("4..ReversingByRecursion")
        print("5..Size of the LinkedList")
        print("6..Exit")
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
            reversedList = list.reverseByIteration(list.firstNode)
            list.displayNodes(reversedList)

        elif option == 4:
            reversedList = list.reverseByRecursion(list.firstNode)
            list.displayNodes(reversedList)

        elif option == 5:
            list.sizeOfList()

        elif option == 6:
            sys.exit(0)

        else:
            sys.exit("You have entered an invalid option.")