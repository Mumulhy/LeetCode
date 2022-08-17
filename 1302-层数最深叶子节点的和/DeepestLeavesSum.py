# -*- coding: utf-8 -*-
# LeetCode 1302-层数最深叶子节点的和

"""
Created on Wed Aug 17 09:37 2022

@author: _Mumu
Environment: py39
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
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
        return sum(node.val for node in stack)
