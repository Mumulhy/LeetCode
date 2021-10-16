# -*- coding: utf-8 -*-
# LeetCode 282-给表达式添加运算符

"""
Created on Sat Oct 16 23:41 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []
        suffix = [int(num[i:]) for i in range(n)]

        def backTrack(expr: List[str], i: int, res: int, mul: int) -> None:
            if i == n:
                if res == target:
                    ans.append(''.join(expr))
                return

            signIndex = len(expr)
            if i > 0:
                expr.append('')
            val = 0
            for j in range(i, n):
                if j > i and num[i] == '0':
                    break
                val = val * 10 + int(num[j])
                expr.append(num[j])
                if i == 0:
                    backTrack(expr, j + 1, val, val)
                else:
                    if suffix[i] >= abs(res - target):
                        expr[signIndex] = '+'
                        backTrack(expr, j + 1, res + val, val)

                        expr[signIndex] = '-'
                        backTrack(expr, j + 1, res - val, -val)

                    expr[signIndex] = '*'
                    backTrack(expr, j + 1, res + mul * (val - 1), mul * val)

            del expr[signIndex:]
            return

        backTrack([], 0, 0, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.addOperators('00', 0))
