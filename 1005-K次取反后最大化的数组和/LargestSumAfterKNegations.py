# -*- coding: utf-8 -*-
# LeetCode 1005-K次取反后最大化的数组和

"""
Created on Fri Dec 3 10:47 2021

@author: _Mumu
Environment: py38
"""

from collections import Counter
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        ans = sum(nums)
        for i in range(-100, 0):
            if cnt[i]:
                ops = min(k, cnt[i])
                cnt[i] -= ops
                cnt[-i] += ops
                k -= ops
                ans -= 2 * i * ops
                if k == 0:
                    break
        if k & 1 == 1:
            for i in range(0, 101):
                if cnt[i]:
                    ans -= 2 * i
                    break
        return ans

        # minus = 0
        # for num in nums:
        #     if num < 0:
        #         minus += 1
        # if k > minus:
        #     ans = sum(abs(num) for num in nums)
        #     if (k - minus) & 1 == 1:
        #         ans -= 2 * min(abs(num) for num in nums)
        #     return ans
        # sorted_nums = sorted(nums)
        # return sum(sorted_nums[k:]) - sum(sorted_nums[:k])


if __name__ == '__main__':
    s = Solution()
    print(s.largestSumAfterKNegations(nums=[3, -1, 0, 2], k=3))
