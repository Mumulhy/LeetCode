# -*- coding: utf-8 -*-
# LeetCode 856-括号的分数

"""
Created on Sun Oct 9 10:20 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack[0]

        # def take_parts(ss: str):
        #     parts = []
        #     lefts = 0
        #     curr_s = ''
        #     for ch in ss:
        #         curr_s += ch
        #         if ch == '(':
        #             lefts += 1
        #         else:
        #             lefts -= 1
        #             if lefts == 0:
        #                 parts.append(curr_s)
        #                 curr_s = ''
        #     return parts
        #
        # def dfs(ss: str, is_part: bool):
        #     if ss == '()':
        #         return 1
        #     if is_part:
        #         return dfs(ss[1:-1], False) * 2
        #     ans = 0
        #     for part in take_parts(ss):
        #         ans += dfs(part, True)
        #     return ans
        #
        # return dfs(s, False)


if __name__ == '__main__':
    s = Solution()
    print(s.scoreOfParentheses("(()(()))"))
