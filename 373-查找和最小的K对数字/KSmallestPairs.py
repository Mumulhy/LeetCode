# -*- coding: utf-8 -*-
# LeetCode 373-查找和最小的K对数字

"""
Created on Fri Jan 14 21:47 2022

@author: _Mumu
Environment: py38
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(m)]
        while pq and len(ans) < k:
            _, i, j = heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
