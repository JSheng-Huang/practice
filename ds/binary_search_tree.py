# Refer to: https://www.geeksforgeeks.org/binary-search-tree-data-structure/
#
# Created by JSheng <jasonhuang0124@gmail.com>
#

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)


def search(root, key):
    if root is None or root.key == key:
        return root
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)


if __name__ == '__main__':
    #     50
    #   /	\
    #  30	70
    #  / \  / \
    # 20 40 60 80
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    in_order(r)
