# -*- coding: utf-8 -*-
# LeetCode 563-二叉树的坡度

"""
Created on Thu Nov 18 14:42 2021

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
    def __init__(self):
        self.ans = 0

    def findTilt(self, root: TreeNode) -> int:
        self._dfs(root)
        return self.ans

    def _dfs(self, node: TreeNode) -> int:
        if not node:
            return 0
        left_sum = self._dfs(node.left)
        right_sum = self._dfs(node.right)
        self.ans += abs(left_sum - right_sum)
        return left_sum + right_sum + node.val

    # def findTilt(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     ans = 0
    #
    #     def dfs(node: TreeNode) -> int:
    #         if not node:
    #             return 0
    #         nonlocal ans
    #         left_sum = dfs(node.left)
    #         right_sum = dfs(node.right)
    #         ans += abs(left_sum - right_sum)
    #         return left_sum + right_sum + node.val
    #
    #     dfs(root)
    #     return ans


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(21,
                    TreeNode(7,
                             TreeNode(1,
                                      TreeNode(3),
                                      TreeNode(3)),
                             TreeNode(1)),
                    TreeNode(14,
                             TreeNode(2),
                             TreeNode(2)))
    print(s.findTilt(root))
