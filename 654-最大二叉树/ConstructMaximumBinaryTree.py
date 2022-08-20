# -*- coding: utf-8 -*-
# LeetCode 654-最大二叉树

"""
Created on Sat Aug 20 14:26 2022

@author: _Mumu
Environment: py38
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        curr_node = TreeNode(max(nums))
        idx = nums.index(curr_node.val)
        curr_node.left = self.constructMaximumBinaryTree(nums[:idx])
        curr_node.right = self.constructMaximumBinaryTree(nums[idx + 1:])
        return curr_node
