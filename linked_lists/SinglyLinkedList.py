import sys

class Node(object):
    data = None
    next = None

    def __init__(self,element):
        self.data = element
        self.next = None
    ## END
## END

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
    ## END

    def displayNodes(self,node):
        tmp = node
        while tmp != None:
            print(tmp.data,"-->",end="")
            tmp = tmp.next
        print("None")
    ## END

    def deleteByValue(self):
        print("Enter the Element that you want to delete")
        elementToBeDeleted = input()
        flag = False
        tmp = self.firstNode

        if tmp == None:
            print("LinkedList is Empty")
        else:
            if self.firstNode.data == elementToBeDeleted:
                self.firstNode = tmp.next
                flag = True
                print(elementToBeDeleted, "deleted successfully")
                return
            ## END

            while tmp.next != None:
                if tmp.next.data == elementToBeDeleted:
                    tmp.next = tmp.next.next
                    flag = True
                    print(elementToBeDeleted, "deleted successfully")
                    return
                ## END
                tmp = tmp.next
            ## END

            if tmp.data == elementToBeDeleted:
                self.lastNode = tmp
                tmp.next = None
                flag = True
                print(elementToBeDeleted, "deleted successfully")
                return
            ## END

        if flag == False:
            print(elementToBeDeleted,"not found in the list.")
        ## END
    ## END

    def deleteByPosition(self):
        print("Enter the Position of Node to be Deleted")
        position = int(input())
        length = self.sizeOfList()

        if position > length:
            print("Deletion is not Possible here")
            return
        ## END
                
        if position == 1:
            self.firstNode = self.firstNode.next
            print("Node at",position,"deleted successfully.")
            return
        elif position == length:
            tmp = self.firstNode
            for i in range(1,position-1):
                tmp = tmp.next
            ## END
            self.lastNode = tmp
            self.lastNode = None
        else:
            tmp = self.firstNode
            for i in range(1,position-1):
                tmp = tmp.next
            ## END
            tmp.next = tmp.next.next
        ## END
    ## END

    def insertAtBeginning(self):
        print("Enter the value for the node.")
        value = input()
        node = Node(value)
        node.next = self.firstNode
        self.firstNode = node
    ## END

    def insertAtEnd(self):
        value = input("Enter the value for the node.")
        node = Node(value)
        tmp = self.firstNode

        while tmp.next != None:
            tmp = tmp.next
        ## END
        tmp.next = node
        self.lastNode = node
    ## END

    def insertAtPosition(self):
        print("Enter the Position at which nodes is to be Inserted.")
        position = int(input())
        print("Enter the value for the node.")
        value = input()

        node = Node(value)
        tmp = self.firstNode

        for i in range(1,position-1):
            tmp = tmp.next
        ## END
        node.next = tmp.next
        tmp.next = node
    ## END

    def search(self):
        print("Enter the value to be Searched.")
        elementToBeSearched = input()
        count = 0
        flag = False
        currentNode = self.firstNode

        while currentNode != None:
            count = count + 1
            if currentNode.data == elementToBeSearched:
                flag = True
                print(elementToBeSearched,"found at position",count)
            ## END
            currentNode = currentNode.next
        ## END
        if flag == False:
            print(elementToBeSearched,"not found in the list.")
        ## END
    ## END

    def reverseByIteration(self,MyNode):
        p = None
        while MyNode:
            q = MyNode.next
            MyNode.next = p
            p = MyNode
            MyNode = q
        ## END
        return p
    ## END

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
        ## END
    ## END

    def sizeOfList(self):
        length = 0
        tmp = self.firstNode
        while tmp != None:
            length = length + 1
            tmp = tmp.next
        ## END
        print("Size of the LinkedList :",length)
        return length
    ## END

# Driver Code
if __name__ == "__main__":
    list = LinkedList()
    option = -1

    while True:
        print("\n")
        print("Select anyone option out of the given options.")
        print("1..Creation of Nodes")
        print("2..Display of Nodes")
        print("3..Insertion at the Beginning")
        print("4..Insertion at the End")
        print("5..Insertion at some Position")
        print("6..Deletion By Value")
        print("7..Deletion By Position")
        print("8..Searching for the Element")
        print("9..Reversing the LinkedList")
        print("10..Size of the LinkedList")
        print("11..Exit")
        print("\n")

        option = int(input())

        if option == 1:
            print("Enter as many elements as you want in the nodes.")
            while True:
                element = input()
                if element == "":
                    break
                list.createNodes(element)
            ## END
        elif option == 2:
            list.displayNodes(list.firstNode)

        elif option == 3:
            list.insertAtBeginning()

        elif option == 4:
            list.insertAtEnd()

        elif option == 5:
            list.insertAtPosition()

        elif option == 6:
            list.deleteByValue()

        elif option == 7:
            list.deleteByPosition()

        elif option == 8:
            list.search()

        elif option == 9:
            reversedList = list.reverseByIteration(list.firstNode)
            list.displayNodes(reversedList)

        elif option == 10:
            list.sizeOfList()

        elif option == 11:
            sys.exit(0)

        else:
            sys.exit("You have entered an invalid option.")
        ##END
    ##END
##END
