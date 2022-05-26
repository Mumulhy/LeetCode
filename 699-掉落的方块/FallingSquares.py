# -*- coding: utf-8 -*-
# LeetCode 699-掉落的方块

"""
Created on Thu May 26 10:53 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect_left
from sortedcontainers import SortedList
from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        skyline = SortedList([(1, 0)])
        ans = []
        for block_left, block_length in positions:
            block_right = block_left + block_length
            idx_left = bisect_left(skyline, (block_left, 0))
            idx_right = bisect_left(skyline, (block_right, 0))
            if idx_left == len(skyline) or skyline[idx_left][0] != block_left:
                height = skyline[idx_left - 1][1] + block_length
            else:
                height = skyline[idx_left][1] + block_length
            if idx_right > idx_left:
                height = max(height, max(h + block_length for _, h in skyline[idx_left:idx_right]))
            skyline2add = [(block_left, height)]
            if idx_right < len(skyline) and skyline[idx_right][0] > block_right:
                skyline2add.append((block_right, skyline[idx_right - 1][1]))
            if idx_right == len(skyline):
                skyline2add.append((block_right, 0))
            for _ in range(idx_right - idx_left):
                skyline.pop(idx_left)
            skyline.update(skyline2add)
            if not ans:
                ans.append(height)
            else:
                ans.append(max(ans[-1], height))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.fallingSquares([[1, 2], [1, 3]]))
