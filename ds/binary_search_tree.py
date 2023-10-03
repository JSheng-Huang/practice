# Refer to:
# Insert: https://lovedrinkcafe.com/python-binary-search-tree-part-1/
# Search/Delete: https://lovedrinkcafe.com/python-binary-search-tree-2/
#
# Created by JSheng <jasonhuang0124@gmail.com>
#

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, cur_node, value):
        if cur_node.value > value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(cur_node.left_child, value)
        elif cur_node.value < value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(cur_node.right_child, value)
        else:
            print('[ERROR] THE INSERTED VALUE HAS EXISTED!')

    def search(self, value):
        if self.root != None:
            return self._search(self.root, value)
        else:
            return None

    def _search(self, cur_node, value):
        if cur_node.value == value:
            return cur_node
        if cur_node.value > value and cur_node.left_child != None:
            return self._search(cur_node.left_child, value)
        if cur_node.value < value and cur_node.right_child != None:
            return self._search(cur_node.right_child, value)
        return None

    def delete():
        pass

    def _delete():
        pass

    def print_tree(self, cur_node):
        if cur_node != None:
            self.print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self.print_tree(cur_node.right_child)


def fill_tree(tree, num_element=10, max_int=50):
    from random import randint
    for _ in range(num_element):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree


if __name__ == '__main__':
    tree = BinarySearchTree()

    # # (jason_huang): Fill tree with random number.
    # tree = fill_tree(tree)

    for i in range(10):
        tree.insert(i)
    if tree.search(5):
        print('Value found.')
    else:
        print('[ERROR] VALUE NOT FOUND!')
    if tree.root:
        tree.print_tree(tree.root)
    else:
        print('[ERROR] THIS TREE IS EMPTY!')
