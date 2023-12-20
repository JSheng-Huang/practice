"""LeetCode#114(Medium) Flatten Binary Tree to Linked List
Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Problem:
        Given the root of a binary tree, flatten the tree into a "linked list":
            The "linked list" should use the same TreeNode class where the 
        right child pointer points to the next node in the list and the left 
        child pointer is always null.
            The "linked list" should be in the same order as a pre-order 
        traversal of the binary tree.
Example:
    #1:
      Input: root = [1,2,5,3,4,null,6]
      Output: [1,null,2,null,3,null,4,null,5,null,6]
    #2:
      Input: root = []
      Output: []
    #3:
      Input: root = [0]
      Output: [0]
Constraints: 
    #1. The number of nodes in the tree is in the range [0, 2000].
    #2. -100 <= Node.val <= 100
Follow up: Can you flatten the tree in-place (with O(1) extra space)?
Refer to: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solutions/940394/python3-iterative-solution-with-explanation/
    Time Complexity: N/A.
    Space Complexity: O(1).
Date: 231218.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List, Optional


# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# # For testing.
class Node:
    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None


# # For testing.
def insert(node, value):
    if node is None:
        return Node(value)
    else:
        if node.root == value:
            return node
        elif not node.left:
            node.left = Node(value)
        elif not node.right:
            node.right = Node(value)
        else:
            node.left = insert(node.left, value)
    return node


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        Written by LeetCode."""
        while root:
            if root.left:
                prev = root.left
                while prev.right:
                    """We go to left Subtree's rightMost Node."""
                    prev = prev.right
                """We make current Node's right Subtree prev's right Subtree."""
                prev.right = root.right

                """We make it right Subtree."""
                root.right = root.left

                """Removing left."""
                root.left = None
            root = root.right


if __name__ == '__main__':
    qwe = Solution()

    """
        1
       /  \
      2    5
      / \   \
     3   4   6
    """
    root = Node(1)
    root = insert(root, 2)
    root = insert(root, 5)
    root = insert(root, 3)
    root = insert(root, 4)
    root.right.right = Node(6)
    print(root.root)
    print(root.left.root)
    print(root.right.root)
    print(root.left.left.root)
    print(root.left.right.root)
    print(root.right.right.root)
    print()

    """
    1
      \
       2
        \
         3
          \
           4
            \
             5
              \
               6
    """
    qwe.flatten(root)
    print(root.root)
    print(root.right.root)
    print(root.right.right.root)
    print(root.right.right.right.root)
    print(root.right.right.right.right.root)
    print(root.right.right.right.right.right.root)
