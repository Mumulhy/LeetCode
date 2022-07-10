# -*- coding: utf-8 -*-
# LeetCode 873-最长的斐波那契子序列的长度

"""
Created on Sat Jul 9 10:52 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_s = set(arr)
        vis = set()
        n = len(arr)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                curr = 2
                p = arr[i]
                q = arr[j]
                if (p, q) in vis:
                    continue
                while p + q in arr_s:
                    vis.add((p, q))
                    p, q = q, p + q
                    curr += 1
                if curr > 2:
                    ans = max(ans, curr)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))
