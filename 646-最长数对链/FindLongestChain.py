# -*- coding: utf-8 -*-
# LeetCode 646-最长数对链

"""
Created on Sat Sept 3 10:58 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        curr, ans = float('-inf'), 0
        for x, y in sorted(pairs, key=lambda p: p[1]):
            if curr < x:
                curr = y
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findLongestChain([[7, 9], [4, 5], [7, 9], [-7, -1], [0, 10], [3, 10], [3, 6], [2, 3]]))
