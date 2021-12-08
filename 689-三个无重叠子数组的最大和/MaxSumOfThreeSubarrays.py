# -*- coding: utf-8 -*-
# LeetCode 689-三个无重叠子数组的最大和

"""
Created on Wed Dec 8 14:56 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ans = []
        sum1, max_sum1, id1 = 0, 0, 0
        sum2, max_sum2, id2 = 0, 0, []
        sum3, max_sum3 = 0, 0
        for i in range(k * 2, len(nums)):
            sum1 += nums[i - k * 2]
            sum2 += nums[i - k]
            sum3 += nums[i]
            if i >= k * 3 - 1:
                if sum1 > max_sum1:
                    max_sum1 = sum1
                    id1 = i - k * 3 + 1
                if max_sum1 + sum2 > max_sum2:
                    max_sum2 = max_sum1 + sum2
                    id2 = [id1, i - k * 2 + 1]
                if max_sum2 + sum3 > max_sum3:
                    max_sum3 = max_sum2 + sum3
                    ans = [*id2, i - k + 1]
                sum1 -= nums[i - k * 3 + 1]
                sum2 -= nums[i - k * 2 + 1]
                sum3 -= nums[i - k + 1]
        return ans

        # n = len(nums)
        # dp = [[0] * n for _ in range(4)]
        # pos = [[[]] * n for _ in range(4)]
        # for i in range(1, 4):
        #     curr_sum = 0
        #     for l in range(k * (i - 1), k * i):
        #         curr_sum += nums[l]
        #     dp[i][k * i - 1] = dp[i - 1][k * (i - 1) - 1] + curr_sum
        #     pos[i][k * i - 1] = [*pos[i - 1][k * (i - 1) - 1], k * (i - 1)]
        #     for j in range(k * i, n):
        #         curr_sum += nums[j] - nums[j - k]
        #         if dp[i - 1][j - k] + curr_sum > dp[i][j - 1]:
        #             dp[i][j] = dp[i - 1][j - k] + curr_sum
        #             pos[i][j] = [*pos[i - 1][j - k], j - k + 1]
        #         else:
        #             dp[i][j] = dp[i][j - 1]
        #             pos[i][j] = pos[i][j - 1]
        # return pos[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxSumOfThreeSubarrays(nums=[1, 2, 1, 2, 6, 7, 5, 1], k=2))
