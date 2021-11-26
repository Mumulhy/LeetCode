# -*- coding: utf-8 -*-
# LeetCode 700-二叉搜索树中的搜索

"""
Created on Fri Nov 26 09:52 2021

@author: _Mumu
Environment: py38
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node and node.val != val:
            if node.val > val:
                node = node.left
            else:
                node = node.right
        return node


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(4,
                    TreeNode(2,
                             TreeNode(1),
                             TreeNode(3)),
                    TreeNode(7))
    print(s.searchBST(root, 5))
