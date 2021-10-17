# -*- coding: utf-8 -*-
# LeetCode 230-二叉搜索树中第K小的元素

"""
Created on Sun Oct 17 15:17 2021

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

        # ans = []
        #
        # def searchNode(node: TreeNode, nth: int) -> Optional[int]:
        #     if node.left:
        #         nth = searchNode(node.left, nth)
        #     if nth is None:
        #         return
        #     nth += 1
        #     if nth == k:
        #         ans.append(node.val)
        #         return
        #     if node.right:
        #         nth = searchNode(node.right, nth)
        #     return nth
        #
        # searchNode(root, 0)
        # return ans[0]


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3,
                    TreeNode(1,
                             None,
                             TreeNode(2)),
                    TreeNode(4))
    print(s.kthSmallest(root, 4))
