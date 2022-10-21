# -*- coding: utf-8 -*-
# LeetCode 779-第K个语法符号

"""
Created on Thu Oct 20 09:45 2022

@author: _Mumu
Environment: py39
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = 0
        while k > 1:
            if k & 1:
                k = k // 2 + 1
            else:
                k //= 2
                ans = 1 - ans
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.kthGrammar(n=2, k=2))
