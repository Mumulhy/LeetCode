# -*- coding: utf-8 -*-
# LeetCode 589-N叉树的前序遍历

"""
Created on Thu Mar 10 19:25 2022

@author: _Mumu
Environment: py38
"""

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(reversed(node.children))
        return ans

        # if not root:
        #     return []
        # if root.children:
        #     ans = [root.val]
        #     for child in root.children:
        #         ans += self.preorder(child)
        #     return ans
        # return [root.val]
