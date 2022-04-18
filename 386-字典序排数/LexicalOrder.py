# -*- coding: utf-8 -*-
# LeetCode 386-字典序排数

"""
Created on Mon Apr 18 11:30 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        num = 1
        ans = [0] * n
        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lexicalOrder(192))
