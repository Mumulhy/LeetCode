# -*- coding: utf-8 -*-
# LeetCode 面试题04.06-后继者

"""
Created on Mon May 16 10:28 2022

@author: _Mumu
Environment: py38
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        ans = None
        if p.right:
            node = p.right
            while node:
                ans = node
                node = node.left
            return ans
        node = root
        while node is not p:
            if node.val > p.val:
                ans = node
                node = node.left
            else:
                node = node.right
        return ans
