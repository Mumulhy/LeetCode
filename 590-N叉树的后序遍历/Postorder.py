# -*- coding: utf-8 -*-
# LeetCode 590-N叉树的后序遍历

"""
Created on Sat Mar 12 10:36 2022

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
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, ans, visited = [root], [], set()
        while stack:
            node = stack[-1]
            if node.children and node not in visited:
                stack.extend(node.children[::-1])
                visited.add(node)
            else:
                ans.append(node.val)
                stack.pop()
        return ans
