# -*- coding: utf-8 -*-
# LeetCode 1161-最大层内元素和

"""
Created on Sun Jul 31 10:39 2022

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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans, layer = 1, 1
        max_sum = root.val
        stack = {root}
        while stack:
            new_stack = set()
            for node in stack:
                if node.left:
                    new_stack.add(node.left)
                if node.right:
                    new_stack.add(node.right)
            stack = new_stack
            layer += 1
            if stack and (curr_sum := sum(node.val for node in stack)) > max_sum:
                max_sum = curr_sum
                ans = layer
        return ans
