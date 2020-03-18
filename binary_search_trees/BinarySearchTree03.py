## Geeks for Geeks

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    ##END
##END

def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.data,end=" ")
        inorder(root.right)
##END

def insert(node, data):
    if node is None:
        return Node(data)

    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)

    return node
##END

def minValueNode(node):
    current = node

    while (current.left is not None):
        current = current.left

    return current
##END

def deleteNode(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = deleteNode(root.left, data)

    elif (data > root.data):
        root.right = deleteNode(root.right, data)

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
        temp = minValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.data = temp.data

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.data)

    return root
##END

if __name__ == "__main__":
    root = None

    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    print("Inorder traversal of the given tree")
    inorder(root)

    print("\nDelete 70")
    root = deleteNode(root, 70)
    print("Inorder traversal of the modified tree")
    inorder(root)

    #print("\nDelete 30")
    #root = deleteNode(root, 30)
    #print("Inorder traversal of the modified tree")
    #inorder(root)

    #print("\nDelete 50")
    #root = deleteNode(root, 50)
    #print("Inorder traversal of the modified tree")
    #inorder(root)
##END