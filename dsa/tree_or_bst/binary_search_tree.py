"""Binary Search Tree
Refer to:
    #1. Insert/Search/Delete: https://www.geeksforgeeks.org/binary-search-tree-data-structure/
    #2. Pre/In/Post Order: https://hackmd.io/@datastruct/ByfLfjlO9
Created by JSheng <jasonhuang0124@gmail.com>
"""


class Node:
    def __init__(self, value):
        self.root = value
        self.left_child = None
        self.right_child = None


def insert(node, value):
    if node is None:
        return Node(value)
    else:
        if node.root == value:
            return node
        elif node.root < value:
            node.right_child = insert(node.right_child, value)
        else:
            node.left_child = insert(node.left_child, value)
    return node


def inOrder(node):
    if node:
        inOrder(node.left_child)
        print(node.root, end=' ')
        inOrder(node.right_child)


def preOrder(node):
    if node:
        print(node.root, end=' ')
        preOrder(node.left_child)
        preOrder(node.right_child)


def postOrder(node):
    if node:
        postOrder(node.left_child)
        postOrder(node.right_child)
        print(node.root, end=' ')


def search(node, value):
    if node is None or node.root == value:
        return node
    if node.root > value:
        return search(node.left_child, value)
    return search(node.right_child, value)


def deleteNode(node, value):
    """Finding the target."""
    if node is None:
        return node
    if node.root > value:
        node.left_child = deleteNode(node.left_child, value)
        return node
    if node.root < value:
        node.right_child = deleteNode(node.right_child, value)
        return node
    """If one of the children is empty."""
    if node.left_child is None:
        tmp = node.right_child
        # del node
        return tmp
    if node.right_child is None:
        tmp = node.left_child
        # del node
        return tmp
    """If both of the children are filled."""
    successor_parent = node

    """Find successor"""
    successor = node.right_child

    while successor.left_child is not None:
        successor_parent = successor
        successor = successor.left_child

    """
    Since successor is always left child of its parent we can safely make 
    successor's right child as left of its parent. If there is no `successor`, 
    then assign `successor.right_child` to `successor_parent.right_child`.
    """
    if successor_parent != node:
        successor_parent.left_child = successor.right_child
    else:
        successor_parent.right_child = successor.right_child
    """Copy `successor.root` to `node.root`."""
    node.root = successor.root

    # del successor
    return node


if __name__ == '__main__':
    """
        50
       /   \
      30   70
      / \  / \
     20 40 60 80
    """

    root = Node(50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)
    print('In-order:')
    inOrder(root)
    print()
    print('Pre-order:')
    preOrder(root)
    print()
    print('Post-order:')
    postOrder(root)
    print()
    # value = 20
    value = 200
    if search(root, value):
        print(value, 'Found!')
    else:
        print('[ERROR]', value, "NOT FOUND!")
    root = deleteNode(root, 20)

    """
        50
       /   \
      40   70
      /   /  \
     30  60  80
    """
    print('In-order:')
    inOrder(root)
    print()
    root = deleteNode(root, 70)

    """
        50
       /  \
      40  80
      /   /
     30  60
    """
    print('In-order:')
    inOrder(root)
    print()

    """
        60
       /  \
      40  80
      /
     30
    """
    root = deleteNode(root, 50)
    print('In-order:')
    inOrder(root)
    print()
