# -*- coding: utf-8 -*-
# LeetCode 517-超级洗衣机

"""
Created on Wed Sept 29 14:30 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        if n == 1:
            return 0
        total = sum(machines)
        if total % n:
            return -1
        avg = total // n
        s, ans = 0, 0
        for num in machines:
            num -= avg
            s += num
            ans = max(ans, abs(s), num)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMinMoves([0, 3, 0]))
