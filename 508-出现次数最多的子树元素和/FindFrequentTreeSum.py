# -*- coding: utf-8 -*-
# LeetCode 508-出现次数最多的子树元素和

"""
Created on Sun Jun 19 15:28 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        cnt = defaultdict(int)
        most = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            nonlocal most
            ss = node.val + dfs(node.left) + dfs(node.right)
            cnt[ss] += 1
            most = max(most, cnt[ss])
            return ss

        dfs(root)
        return [key for key, val in cnt.items() if val == most]
