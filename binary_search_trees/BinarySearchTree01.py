## This algorithm has been established by HackerRank.

class BstNode():
    left = None
    right = None
    #data = None

    def __init__(self,data):
        self.data = data
    ##END

    def insert(self,value):
        if (value < self.data):
            if (self.left is None):
                self.left = BstNode(value)
            else:
                self.left.insert(value)
        else:
            if (self.right is None):
                self.right = BstNode(value)
            else:
                self.right.insert(value)
    ##END

    def contains(self,value):
        if (value == self.data):
            return True
        elif (value < self.data):
            if (self.left is None):
                return False
            else:
                return self.left.contains(value)
        else:
            if (self.right is None):
                return False
            else:
                return self.right.conatins(value)
    ##END

    def printInOrder(self):
        if (self.left is not None):
            self.left.printInOrder()

        print(self.data,end = " ")

        if (self.right is not None):
            self.right.printInOrder()
    ##END

    def printPreOrder(self):
        print(self.data, end = " ")

        if (self.left is not None):
            self.left.printInOrder()

        if (self.right is not None):
            self.right.printInOrder()
    ##ENDs

    def printPostOrder(self):
        if (self.left is not None):
            self.left.printInOrder()

        if (self.right is not None):
            self.right.printInOrder()

        print(self.data, end= " ")
    ##END
##END

if __name__ == "__main__":
    bst = BstNode(10)
    bst.insert(5)
    bst.insert(20)
    bst.insert(3)
    bst.insert(9)
    bst.insert(15)
    bst.insert(25)

    print("\n InOrder :")
    bst.printInOrder()
    print("\n PreOrder :")
    bst.printPreOrder()
    print("\n PostOrder :")
    bst.printPostOrder()
##END