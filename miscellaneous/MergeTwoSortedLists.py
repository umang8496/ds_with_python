
#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
    ## END
## END


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    ## END

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        ## END
        self.tail = node
    ## END
## END

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data),end=' ')
        node = node.next
        if node:
            print(sep,end=' ')
        ## END
    ## END
## END


# def print_singly_linked_list(node, sep):
#     ptr = node.head
#     print(ptr.data)
#     sys.exit()
#     while(ptr != None):
#         print(str(ptr.data),sep='-->', end='')
#         node = ptr.next
#     ## END
#     print('None')
# ## END


def mergeLists(head1, head2):
    ptr1 = head1
    ptr2 = head2
    node_ptr = SinglyLinkedList()

    while(ptr1!= None and ptr2!= None):
        if(ptr1.data <= ptr2.data):
        	node_ptr.insert_node(ptr1.data)
        	ptr1 = ptr1.next
        else:
        	node_ptr.insert_node(ptr2.data)
        	ptr2 = ptr2.next
        ## END
    ## END

    if(ptr1 == None):
    	while(ptr2 != None):
    		node_ptr.insert_node(ptr2.data)
    		ptr2 = ptr2.next
		## END
    else:
        while(ptr1 != None):
        	node_ptr.insert_node(ptr1.data)
        	ptr1 = ptr1.next
		## END
    ## END

    return node_ptr.head
## END


if __name__ == '__main__':
    # tests = int(input())
    tests = 1

    for tests_itr in range(tests):
        llist1_count = int(input())
        llist1 = SinglyLinkedList()
        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
        ## END

        llist2_count = int(input())
        llist2 = SinglyLinkedList()
        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
        ## END

        llist3 = mergeLists(llist1.head, llist2.head)
        print_singly_linked_list(llist3, ' ')
    ## END
## END
