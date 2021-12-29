# -*- coding: utf-8 -*-
# LeetCode 1995-统计特殊四元组

"""
Created on Wed Dec 29 14:56 2021

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        cnt = defaultdict(int)
        for b in range(n - 3, 0, -1):
            for d in range(b + 2, n):
                if (diff := nums[d] - nums[b + 1]) > 1:
                    cnt[diff] += 1
            for a in range(b):
                if (total := nums[a] + nums[b]) in cnt:
                    ans += cnt[total]
        return ans

        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         curr_sum2 = nums[i] + nums[j]
        #         for k in range(j + 1, n):
        #             curr_sum3 = curr_sum2 + nums[k]
        #             for l in range(k + 1, n):
        #                 if nums[l] == curr_sum3:
        #                     ans += 1
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countQuadruplets([28, 8, 49, 85, 37, 90, 20, 8]))
