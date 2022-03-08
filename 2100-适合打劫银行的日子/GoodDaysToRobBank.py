# -*- coding: utf-8 -*-
# LeetCode 2100-适合打劫银行的日子

"""
Created on Sun Mar 6 12:52 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return [i for i in range(n)]
        if n <= 2 * time:
            return []
        left, right = 0, 0
        for i in range(time):
            if security[i] >= security[i + 1]:
                left += 1
            else:
                left = 0
            if security[i + time] <= security[i + time + 1]:
                right += 1
            else:
                right = 0
        ans = []
        if left == right == time:
            ans.append(time)
        for i in range(time + 1, n - time):
            if security[i - 1] >= security[i]:
                left = min(time, left + 1)
            else:
                left = 0
            if security[i - 1 + time] <= security[i + time]:
                right = min(time, right + 1)
            else:
                right = 0
            if left == right == time:
                ans.append(i)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.goodDaysToRobBank([1], 2))
