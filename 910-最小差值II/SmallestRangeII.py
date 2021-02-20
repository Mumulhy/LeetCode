# -*- coding: utf-8 -*-
# LeetCode 910-最小差值II

"""
Created on Sat Feb 20 16:41 2021

@author: _Mumu
Environment: py37
"""

class Solution:
    def smallestRangeII(self, A: list, K: int) -> int:
        A.sort()
        K *= 2
        res = A[-1] - A[0]
        for i in range(len(A)-1):
            A[i] += K
            res = min(res, max(A[i], A[-1])-min(A[i+1], A[0]))
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.smallestRangeII([6, 1, 3], 3))