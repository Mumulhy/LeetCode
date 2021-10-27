# -*- coding: utf-8 -*-
# LeetCode 301-删除无效的括号

"""
Created on Wed Oct 27 14:24 2021

@author: _Mumu
Environment: py38
"""

from functools import lru_cache
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = set()
        s = s.lstrip(')').rstrip('(')
        n = len(s)
        left = 0
        right = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left:
                    left -= 1
                else:
                    right += 1

        @lru_cache(maxsize=8)
        def dfs(idx: int, lCount: int, rCount: int, lRemove: int, rRemove: int, st: str) -> None:
            if idx == n:
                if lRemove == 0 and rRemove == 0:
                    ans.add(st)
                return
            if s[idx] == '(':
                if lRemove:
                    dfs(idx + 1, lCount, rCount, lRemove - 1, rRemove, st)
                dfs(idx + 1, lCount + 1, rCount, lRemove, rRemove, st + '(')
            elif s[idx] == ')':
                if rRemove:
                    dfs(idx + 1, lCount, rCount, lRemove, rRemove - 1, st)
                if lCount > rCount:
                    dfs(idx + 1, lCount, rCount + 1, lRemove, rRemove, st + ')')
            else:
                dfs(idx + 1, lCount, rCount, lRemove, rRemove, st + s[idx])
            return

        dfs(0, 0, 0, left, right, '')
        return list(ans)

    #     ans = []
    #     s = s.lstrip(')').rstrip('(')
    #     stringsToCheck = {s}
    #
    #     while True:
    #         for ss in stringsToCheck:
    #             if self.__isValid(ss):
    #                 ans.append(ss)
    #         if ans:
    #             return ans
    #         stringsToCheckNext = set()
    #         for ss in stringsToCheck:
    #             for i in range(len(ss)):
    #                 if ss[i] == '(' or ss[i] == ')':
    #                     stringsToCheckNext.add(ss[:i] + ss[i + 1:])
    #         stringsToCheck = stringsToCheckNext
    #
    # def __isValid(self, s: str) -> bool:
    #     left = 0
    #     for ch in s:
    #         if ch == '(':
    #             left += 1
    #         elif ch == ')':
    #             if left == 0:
    #                 return False
    #             left -= 1
    #     return left == 0


if __name__ == '__main__':
    s = Solution()
    print(s.removeInvalidParentheses("(a)())()"))
