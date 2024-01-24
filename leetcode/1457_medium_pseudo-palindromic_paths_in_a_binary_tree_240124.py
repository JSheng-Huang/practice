"""LeetCode#1457(Medium) Pseudo-Palindromic Paths in a Binary Tree
Link: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/?envType=daily-question&envId=2024-01-24
Problem:
        Given a binary tree where node values are digits from 1 to 9. A path in 
    the binary tree is said to be pseudo-palindromic if at least one 
    permutation of the node values in the path is a palindrome.
        Return the number of pseudo-palindromic paths going from the root node 
    to leaf nodes.
Example:
    #1:
      Input: root = [2,3,1,3,1,null,1]
      Output: 2 
      Explanation: 
            The figure above represents the given binary tree. There are three 
        paths going from the root node to leaf nodes: the red path [2,3,3], the 
        green path [2,1,1], and the path [2,3,1]. Among these paths only red 
        path and green path are pseudo-palindromic paths since the red path [2,
        3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,
        1] can be rearranged in [1,2,1] (palindrome).
    #2:
      Input: root = [2,1,1,1,3,null,null,null,null,null,1]
      Output: 1 
      Explanation: 
            The figure above represents the given binary tree. There are three 
        paths going from the root node to leaf nodes: the green path [2,1,1], 
        the path [2,1,3,1], and the path [2,1]. Among these paths only the 
        green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,
        2,1] (palindrome)
    #3:
      Input: root = [9]
      Output: 1
Constraints: 
    #1. The number of nodes in the tree is in the range [1, 105].
    #2. 1 <= Node.val <= 9
Refer to: 
Date: 240124.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        """240124: Happy Birthday to myself:)"""
        ans = 0

        return ans

    def dfs(self):
        return


if __name__ == '__main__':
    qwe = Solution()

    """Should return `2`."""
    root = TreeNode(2)
    root.left = TreeNode(3, TreeNode(3), TreeNode(1))
    root.right = TreeNode(1, None, TreeNode(1))
    print(qwe.pseudoPalindromicPaths([2, 3, 1, 3, 1, None, 1]))

    """Should return `1`."""
    root = TreeNode(2)
    root.left = TreeNode(1, TreeNode(1), TreeNode(3, None, 1))
    root.right = TreeNode(1)
    print(qwe.pseudoPalindromicPaths(
        [2, 1, 1, 1, 3, None, None, None, None, None, 1]))

    """Should return `1`."""
    root = TreeNode(9)
    print(qwe.pseudoPalindromicPaths([9]))
