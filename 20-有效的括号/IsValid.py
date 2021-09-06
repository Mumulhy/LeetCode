# -*- coding: utf-8 -*-
# LeetCode 20-有效的括号

"""
Created on Sun Sept 6 19:12 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for item in s:
            if item in pairs:
                if stack and stack[-1] == pairs[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return False if stack else True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid(')'))
