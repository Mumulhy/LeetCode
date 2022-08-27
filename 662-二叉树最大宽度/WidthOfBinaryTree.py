# -*- coding: utf-8 -*-
# LeetCode 662-二叉树最大宽度

"""
Created on Sat Aug 27 10:33 2022

@author: _Mumu
Environment: py38
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 0]]
        ans = 1
        while stack:
            new_stack = []
            for node, idx in stack:
                if node.left:
                    new_stack.append([node.left, idx * 2])
                if node.right:
                    new_stack.append([node.right, idx * 2 + 1])
            ans = max(ans, stack[-1][1] - stack[0][1] + 1)
            stack = new_stack
        return ans
