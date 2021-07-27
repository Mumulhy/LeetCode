# -*- coding: utf-8 -*-
# LeetCode 671-二叉树中第二小的节点

"""
Created on Tue Jul 27 20:31 2021

@author: _Mumu
Environment: py38
"""


# from sortedcontainers import SortedList


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        second_min = -1
        root_val = root.val

        def updateSecondMin(node: TreeNode) -> None:
            nonlocal second_min
            if not node:
                return
            if second_min != -1 and node.val >= second_min:
                return
            if node.val > root_val:
                second_min = node.val
                return
            updateSecondMin(node.left)
            updateSecondMin(node.right)

        updateSecondMin(root)
        return second_min

        # if not root.left:
        #     return -1
        # vals = SortedList([root.val])
        # vals = self.findSecondMin(root, vals)
        # if len(vals) > 1:
        #     return vals[1]
        # else:
        #     return -1
    #
    # def findSecondMin(self, root: TreeNode, vals: SortedList) -> SortedList:
    #     if root.val not in vals:
    #         vals.add(root.val)
    #         return vals
    #     if root.left:
    #         vals = self.findSecondMin(root.left, vals)
    #         vals = self.findSecondMin(root.right, vals)
    #     return vals


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(2)
    root.right.left.left = TreeNode(2)
    root.right.left.right = TreeNode(5)
    root.right.right.left = TreeNode(2)
    root.right.right.right = TreeNode(2)
    root.right.right.right.left = TreeNode(2)
    root.right.right.right.right = TreeNode(3)
    print(s.findSecondMinimumValue(root))
