## BST, also called as ordered or sorted Binary Tree, is a special kind of data structure that holds or stores items in memory.
## BSTs keep their keys in sorted order, so that lookup and other operations can use the principle of binary search:
## when looking for a key in a tree, they traverse the tree from root to leaf,
## making comparisons to keys stored in the nodes of the tree and deciding, on the basis of the comparison,
## to continue searching in the left or right subtrees.
## On average, this means that each comparison allows the operations to skip about half of the tree,
## so that each lookup, insertion or deletion takes time proportional to the LOG of the number of items stored in the tree.
## This is much better than the linear time required to find items by key in an (unsorted) array,
## but slower than the corresponding operations on hash tables.

## Operations on BST
## Insertion
## Searching
## Deletion
## Traversal
## Verification


class BstNode:
    left = None
    right = None

    def __init__(self, data):
        self.data = data
    ##END
##END

class BST(object):
    def __init__(self):
        pass
    ##END

    def insert(self, node, data):
        if node is None:
            return BstNode(data)

        if data <= node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        return node
    ##END

    def printInOrder(self,root):
        if (root is not None):
            self.printInOrder(root.left)
            print(root.data,end=" ")
            self.printInOrder(root.right)
    ##END

    def printPreOrder(self,root):
        if (root is not None):
            print(root.data, end=" ")
            self.printPreOrder(root.left)
            self.printPreOrder(root.right)
    ##END

    def printPostOrder(self,root):
        if (root is not None):
            self.printPostOrder(root.left)
            self.printPostOrder(root.right)
            print(root.data,end=" ")
    ##END

    def minValueNode(self, node):
        current = node
        while (current.left is not None):
            current = current.left
        return current
    ##END

    def search(self, root, value):
        if (value == root.data):
            return True
        elif (value < root.data):
            if (root.left is None):
                return False
            else:
                return self.search(root.left, value)
        else:
            if (root.right is None):
                return False
            else:
                return self.search(root.right, value)
    ##END

    def deleteNode(self, root, data):
        if root is None:
            return root

        if (data < root.data):
            root.left = self.deleteNode(root.left, data)

        elif (data > root.data):
            root.right = self.deleteNode(root.right, data)

        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.minValueNode(root.right)

            # Copy the inorder successor's content to this node
            root.data = temp.data

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.data)

        return root
    ##END

    def printLevelOrderTraversal(self,root):
        pass
##END

if __name__ == "__main__":
    root = None
    bst = BST()
    root = bst.insert(root, 50)
    root = bst.insert(root, 30)
    root = bst.insert(root, 20)
    root = bst.insert(root, 40)
    root = bst.insert(root, 70)
    root = bst.insert(root, 60)
    root = bst.insert(root, 80)

    #print("\n InOrder traversal of the given tree")
    bst.printInOrder(root)

    #print("\n PreOrder traversal of the given tree")
    #bst.printPreOrder(root)

    #print("\n PostOrder traversal of the given tree")
    #bst.printPostOrder(root)

    #print("\n"+(str(bst.search(root,20))))     #True
    root = bst.deleteNode(root,20)
    #print("\nroot :",root)
    print()
    bst.printInOrder(root)
##END