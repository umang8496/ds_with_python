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
            # print("[",tmp.data,"|",id(tmp),"]-->", end="")
            print(tmp.data,"-->",end="")
            tmp = tmp.next
        print("None")

    def sizeOfList(self):
        length = 0
        tmp = self.firstNode
        while tmp != None:
            length = length + 1
            tmp = tmp.next
        # print("Size of the LinkedList :",length)
        return length

class Stack(object):
    topofstack = -1
    stack = []

    def push(self,node):
        self.stack.append(node)
        self.topofstack = self.topofstack + 1
        # print(node.data,"pushed into stack")

    def pop(self):
        element = self.stack[-1]
        self.topofstack = self.topofstack - 1
        del self.stack[-1]
        # print(element.data,"popped out of stack")
        return element

    def sizeOfStack(self):
        return self.topofstack + 1


class Swapping(object):
    stk = Stack()

    def swap(self,ptr):
        n1 = None
        n2 = None
        node = None
        sizeofstack = 0

        while ptr != None:
            # print(id(ptr))
            sizeofstack = self.stk.sizeOfStack()
            print("sizeofstack",sizeofstack)

            if sizeofstack == 2:
                n1 = self.stk.pop()
                n2 = self.stk.pop()
                if node == None:
                    node = n1
                n1.next = n2
                n2.next = ptr.next

            self.stk.push(ptr)
            if ptr.next == None:
                n2.next = ptr
            ptr = ptr.next


        if sizeofstack == 1:
            n1 = self.stk.pop()
            n2 = self.stk.pop()
            if node == None:
                node = n1
            tmp = n1.next
            n1.next = n2
            n2.next = tmp

        return node


# Driver Code
if __name__ == "__main__":
    list = LinkedList()
    swap = Swapping()

    print("Enter as many elements as you want in the nodes.")
    while True:
        element = input()
        if element == "":
            break
        list.createNodes(element)

    list.displayNodes(list.firstNode)

    print("")
    print("Now the entered list has got swapped pairwise.")

    node = swap.swap(list.firstNode)
    list.displayNodes(node)