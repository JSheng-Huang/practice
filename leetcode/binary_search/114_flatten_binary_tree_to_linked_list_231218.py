"""LeetCode#114(Medium) Flatten Binary Tree to Linked List
Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Problem:
        Given the root of a binary tree, flatten the tree into a "linked list":
            The "linked list" should use the same TreeNode class where the 
        right child pointer points to the next node in the list and the left 
        child pointer is always null.
            The "linked list" should be in the same order as a pre-order 
        traversal of the binary tree.
Note: N/A.
Example:
    #1:
      Input: root = [1,2,5,3,4,null,6]
      Output: [1,null,2,null,3,null,4,null,5,null,6]
    #2:
      Input: root = []
      Output: []
    #2:
      Input: root = [0]
      Output: [0]
Constraints: 
    #1. The number of nodes in the tree is in the range [0, 2000].
    #2. -100 <= Node.val <= 100
Follow up: Can you flatten the tree in-place (with O(1) extra space)?
Refer to: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
    Time Complexity: ???
    Space Complexity: ???
    Explanation: ???
Date: 231218.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List, Optional, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # cur = root
        # while cur:
        #     if cur.left:
        #         prev = cur.left
        #         while prev.right:
        #             prev = prev.right    # We go to left Subtree's rightMost Node
        #         prev.right = cur.right  # We make current Node's right Subtree prev's right Subtree
        #         cur.right = cur.left    # We make it right Subtree
        #         cur.left = None   # Removing left
        #     cur = cur.right
        while n:
            temp = n.left  # get left tree
            if temp:
                while temp.right:  # find its right most node
                    temp = temp.right
                # "cut" n.right and attach it to temp
                temp.right, n.right, n.left = n.right, n.left, None
            n = n.right
        """
        I think thats because we only every node once, Recursion also does that ryt.
        Only improvement is the time complexity.
        """
        """
        Only improvement is the time complexity.
        Agree.
        Since execution time is the same exactly - does it mean the difference due to recursion insignificant?
        The test cases are relatively big.
        Or it might be due to "server load" fluctuation?
        """


if __name__ == '__main__':
    qwe = Solution()
