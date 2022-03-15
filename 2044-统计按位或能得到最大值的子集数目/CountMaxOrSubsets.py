# -*- coding: utf-8 -*-
# LeetCode 2044-统计按位或能得到最大值的子集数目

"""
Created on Tues Mar 15 14:54 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or, ans = 0, 0
        for num in nums:
            max_or |= num

        def dfs(pos: int, xor: int) -> None:
            nonlocal ans
            if xor == max_or:
                ans += 1 << (n - pos)
                return
            for i in range(pos, n):
                dfs(i + 1, xor | nums[i])
            return

        dfs(0, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countMaxOrSubsets([3, 2, 1, 5]))
