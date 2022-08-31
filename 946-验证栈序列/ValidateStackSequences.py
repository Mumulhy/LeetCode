# -*- coding: utf-8 -*-
# LeetCode 946-验证栈序列

"""
Created on Wed Aug 31 09:39 2022

@author: _Mumu
Environment: py39
"""

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0
        n = len(popped)
        while j < n:
            while i < n and (not stack or stack[-1] != popped[j]):
                stack.append(pushed[i])
                i += 1
            while j < n and (stack and stack[-1] == popped[j]):
                stack.pop()
                j += 1
            if i == n and j < n:
                return False
        return True
