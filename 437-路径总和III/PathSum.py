# -*- coding: utf-8 -*-
# LeetCode 437-路径总和III

"""
Created on Tues Sept 28 13:15 2021

@author: _Mumu
Environment: py38
"""

from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        paths = 0
        preSums = defaultdict(int)
        preSums[0] = 1

        def getPaths(node: TreeNode, pre: int) -> None:
            nonlocal paths
            pre += node.val
            paths += preSums[pre - targetSum]
            preSums[pre] += 1
            if node.left:
                getPaths(node.left, pre)
            if node.right:
                getPaths(node.right, pre)
            preSums[pre] -= 1
            return

        getPaths(root, 0)
        return paths


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(10,
                    TreeNode(5,
                             TreeNode(3,
                                      TreeNode(3),
                                      TreeNode(-2)),
                             TreeNode(2,
                                      None,
                                      TreeNode(1))),
                    TreeNode(-3,
                             None,
                             TreeNode(11)))
    print(s.pathSum(root, 8))
