# -*- coding: utf-8 -*-
# LeetCode 1609-奇偶树

"""
Created on Sat Dec 25 22:19 2021

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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        layer = 0
        stack = [root]
        while stack:
            if layer & 1 == 0:
                for i in range(len(stack)):
                    if stack[i].val & 1 == 0 or (i > 0 and stack[i].val <= stack[i - 1].val):
                        return False
            else:
                for i in range(len(stack)):
                    if stack[i].val & 1 == 1 or (i > 0 and stack[i].val >= stack[i - 1].val):
                        return False
            new_stack = []
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
            layer += 1
        return True
