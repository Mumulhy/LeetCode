# -*- coding: utf-8 -*-
# LeetCode 513-找树左下角的值

"""
Created on Wed Jun 22 10:39 2022

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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        while True:
            new_stack = []
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            if not new_stack:
                break
            stack = new_stack
        return stack[0].val
