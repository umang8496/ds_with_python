#!/bin/python3

import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def compare_lists(llist1, llist2):
    ll_1_ptr = llist1
    ll_2_ptr = llist2

    # while(ll_1_ptr != None or ll_2_ptr != None):
    while(True):
        if (ll_1_ptr == None and ll_2_ptr == None):
            break
        elif (ll_1_ptr == None and ll_2_ptr != None):
            return 0        
        elif (ll_1_ptr != None and ll_2_ptr == None):
            return 0
        else:
            if (ll_1_ptr.data != ll_2_ptr.data):
                return 0
            ## END
        ## END
        ll_1_ptr = ll_1_ptr.next
        ll_2_ptr = ll_2_ptr.next
        ## END
    ## END
    return 1
## END

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
