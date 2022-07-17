# -*- coding: utf-8 -*-
# LeetCode 565-数组嵌套

"""
Created on Sun Jul 17 11:02 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        left = set(range(n))
        ans = 0
        while left:
            curr_loop = set()
            curr = next(iter(left))
            while curr not in curr_loop:
                curr_loop.add(curr)
                curr = nums[curr]
            ans = max(ans, len(curr_loop))
            left -= curr_loop
            if ans >= len(left):
                break
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.arrayNesting([5, 4, 0, 3, 1, 6, 2]))
