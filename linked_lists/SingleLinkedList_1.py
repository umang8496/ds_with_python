class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    ## END

    def getData(self):
        return self.data
    ## END

    def getNext(self):
        return self.next
    ## END

    def setData(self,newdata):
        self.data = newdata
    ## END

    def setNext(self,newnext):
        self.next = newnext
    ## END
## END

class MyList:
    #head = None
    def __init__(self):
        self.head = None
    ## END

    def isEmpty(self):
        return self.head == None
    ## END

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    ## END

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        ## END
        return count
    ## END

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
            ## END
        ## END
        return found
    ## END

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        ## END
    ## END
## END

if __name__ == "__main__":
    mylist = MyList()
    #print(mylist)

    mylist.add(31)
    mylist.add(77)
    # mylist.add(17)
    # mylist.add(93)
    # mylist.add(26)
    # mylist.add(54)
    #
    # print(mylist.size())
    # print(mylist.search(93))
    # print(mylist.search(100))
    #
    # mylist.add(100)
    # print(mylist.search(100))
    # print(mylist.size())
    #
    # mylist.remove(54)
    # print(mylist.size())
    # mylist.remove(93)
    # print(mylist.size())
    # mylist.remove(31)
    # print(mylist.size())
    # print(mylist.search(93))
## END
