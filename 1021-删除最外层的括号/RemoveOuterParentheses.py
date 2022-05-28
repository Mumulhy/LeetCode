# -*- coding: utf-8 -*-
# LeetCode 1021-删除最外层的括号

"""
Created on Sat May 28 10:21 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        left_cnt = 0
        ans = ''
        for ch in s:
            if ch == ')':
                left_cnt -= 1
            if left_cnt:
                ans += ch
            if ch == '(':
                left_cnt += 1
        return ans

        # left_cnt = 0
        # ans = ''
        # for ch in s:
        #     if ch == '(':
        #         if left_cnt > 0:
        #             ans += ch
        #         left_cnt += 1
        #     else:
        #         if left_cnt > 1:
        #             ans += ch
        #         left_cnt -= 1
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.removeOuterParentheses("()()"))
