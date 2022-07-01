# -*- coding: utf-8 -*-
# LeetCode 241-为运算表达式设计优先级

"""
Created on Fri Jul 1 10:25 2022

@author: _Mumu
Environment: py38
"""

from functools import lru_cache
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ADD, SUB, MUL = '+', '-', '*'
        ops = []
        m = len(expression)
        i = 0
        while i < m:
            if expression[i].isdigit():
                digit = expression[i]
                i += 1
                while i < m and expression[i].isdigit():
                    digit += expression[i]
                    i += 1
                ops.append(int(digit))
            else:
                if expression[i] == ADD:
                    ops.append(ADD)
                elif expression[i] == SUB:
                    ops.append(SUB)
                else:
                    ops.append(MUL)
                i += 1

        @lru_cache(None)
        def dfs(l: int, r: int) -> List[int]:
            if l == r:
                return [ops[l]]
            res = []
            for j in range(l + 1, r, 2):
                l_results = dfs(l, j - 1)
                r_results = dfs(j + 1, r)
                for l_result in l_results:
                    for r_result in r_results:
                        if ops[j] == ADD:
                            res.append(l_result + r_result)
                        elif ops[j] == SUB:
                            res.append(l_result - r_result)
                        else:
                            res.append(l_result * r_result)
            return res

        return dfs(0, len(ops) - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.diffWaysToCompute("2-1-1"))
