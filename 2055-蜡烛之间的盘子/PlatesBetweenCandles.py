# -*- coding: utf-8 -*-
# LeetCode 2055-蜡烛之间的盘子

"""
Created on Tues Mar 8 19:22 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        combined = []
        cradle = 0
        plate = 0
        if s[0] == '*':
            combined.append(0)
        for ss in s:
            if ss == '|':
                if plate == 0:
                    cradle += 1
                else:
                    combined.append(plate)
                    cradle = 1
                    plate = 0
            else:
                if cradle == 0:
                    plate += 1
                else:
                    combined.append(cradle)
                    plate = 1
                    cradle = 0
        combined.append(max(cradle, plate))
        prefix = [combined[0]]
        prefix_plate = [0]
        for i, num in enumerate(combined):
            if i == 0:
                continue
            prefix.append(num + prefix[-1])
            prefix_plate.append((i & 1) * num + prefix_plate[-1])
        ans = []
        n = len(prefix_plate)
        for l, r in queries:
            idx_l, idx_r = bisect(prefix, l), bisect(prefix, r)
            idx_l += idx_l & 1
            if idx_l >= n:
                ans.append(0)
                continue
            idx_r -= idx_r & 1
            ans.append(max(0, prefix_plate[idx_r] - prefix_plate[idx_l]))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.platesBetweenCandles(s="||*", queries=[[2, 2]]))
