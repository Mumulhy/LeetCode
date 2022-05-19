# -*- coding: utf-8 -*-
# LeetCode 462-最少移动次数使数组元素相等II

"""
Created on Thu May 19 10:47 2022

@author: _Mumu
Environment: py38
"""

from collections import deque
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        q = deque(sorted(nums))
        ans = 0
        while len(q) > 1:
            ans += q.pop() - q.popleft()
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minMoves2([1, 10, 2, 9]))
