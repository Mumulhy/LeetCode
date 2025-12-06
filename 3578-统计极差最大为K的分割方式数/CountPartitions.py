# -*- coding: utf-8 -*-
# LeetCode 3578-统计极差最大为K的分割方式数

"""
Created on Sat Dec 6 11:26 2025

@author: _Mumu
Environment: py38
"""

from collections import deque
from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        min_q = deque()
        max_q = deque()

        dp[0] = 1
        prefix[0] = 1
        j = 0

        for i in range(n):
            # 维护最大值队列
            while max_q and nums[max_q[-1]] <= nums[i]:
                max_q.pop()
            max_q.append(i)

            # 维护最小值队列
            while min_q and nums[min_q[-1]] >= nums[i]:
                min_q.pop()
            min_q.append(i)

            # 调整窗口
            while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] > k:
                if max_q[0] == j:
                    max_q.popleft()
                if min_q[0] == j:
                    min_q.popleft()
                j += 1

            if j > 0:
                dp[i + 1] = (prefix[i] - prefix[j - 1] + mod) % mod
            else:
                dp[i + 1] = prefix[i] % mod
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod

        return dp[n]

        # mod = 10 ** 9 + 7
        # dp = [[[None] * 3 for _ in range(len(nums))] for _ in range(len(nums))]
        # dp[0][0] = [1, nums[0], nums[0]]
        # for j in range(1, len(nums)):
        #     dp[j][j] = [sum([dp[i][j - 1][0] for i in range(j)]) % mod, nums[j], nums[j]]
        #     for i in range(j):
        #         dp[i][j][1] = min(nums[j], dp[i][j - 1][1])
        #         dp[i][j][2] = max(nums[j], dp[i][j - 1][2])
        #         dp[i][j][0] = 0 if dp[i][j][2] - dp[i][j][1] > k else dp[i][j - 1][0]
        # return sum([dp[i][len(nums) - 1][0] for i in range(len(nums))]) % mod


if __name__ == "__main__":
    s = Solution()
    print(s.countPartitions([9, 4, 1, 3, 7], 4))
