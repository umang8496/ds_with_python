class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


class SingleList(object):
    firstNode = None
    lastNode = None

    def show(self):
        print('Showing list data:')
        current_node = self.firstNode
        while current_node is not None:
            print(current_node.data, " -> ", end="")
            print("current_node",id(current_node))
            print("current_node.next",id(current_node.next))
            print()
            current_node = current_node.next
        print(None)

    def append(self, data):
        node = Node(data, None)
        if self.firstNode is None:
            self.firstNode = self.lastNode = node
        else:
            self.lastNode.next = node
        self.lastNode = node

        print("node",id(node))
        print("node.data",id(node.data))
        print("node.next",id(node.next))
        print("self.firstNode",id(self.firstNode))
        print("self.lastNode",id(self.lastNode))
        print()

    def remove(self, node_value):
        current_node = self.firstNode
        previous_node = None
        while current_node is not None:
            if current_node.data == node_value:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.firstNode = current_node.next

            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next

    def size(self):
        size = 0
        current_node = self.firstNode
        while current_node is not None:
            size = size + 1
            current_node = current_node.next
        print("Size :",size)

    def operations(self,option):
        if option == 1:
            self.show()
        elif option == 2:
            pass
        elif option == 3:
            self.size()
        else:
            pass


if __name__ == "__main__":
    s = SingleList()

    print("Enter values into the LinkedList.")
    while True:
        x = input()
        if x == "":
            break
        else:
            s.append(x)
    print("You have successfully entered elements into the LinkedList")

    print("Now select one of the following options.")
    print("1..To See the Current Status of LinkedList")
    print("2..To Delete any element of the LinekdList")
    print("3..To know the size of the LinkedList")
    option = int(input())

    s.operations(option)
