# -*- coding: utf-8 -*-
# LeetCode 825-适龄的朋友

"""
Created on Mon Dec 27 20:55 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1
        pre = [0] * 121
        for age in range(1, 121):
            pre[age] = pre[age - 1] + cnt[age]
        ans = 0
        for age in range(15, 121):
            if cnt[age] == 0:
                continue
            bound = int(0.5 * age + 7)
            ans += cnt[age] * (pre[age] - pre[bound] - 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numFriendRequests([20, 30, 100, 110, 120]))
