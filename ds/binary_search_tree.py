# # (jason_huang):
# # Insert: https://lovedrinkcafe.com/python-binary-search-tree-part-1/
# # Delete: https://lovedrinkcafe.com/python-binary-search-tree-2/
# # Search: https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
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

    def print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)


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
    if tree.root:
        tree.print_tree(tree.root)
    else:
        print('[ERROR] THIS TREE IS EMPTY!')
