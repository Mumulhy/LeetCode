# -*- coding: utf-8 -*-
# LeetCode 904-水果成篮

"""
Created on Mon Oct 17 14:33 2022

@author: _Mumu
Environment: py39
"""

from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        dp = 1
        pick = {fruits[0]}
        curr = fruits[0]
        cnt = 1
        ans = 1
        for i in range(1, n):
            if fruits[i] == curr:
                cnt += 1
                dp += 1
            else:
                if fruits[i] in pick:
                    dp += 1
                else:
                    dp = cnt + 1
                pick = {curr, fruits[i]}
                curr = fruits[i]
                cnt = 1
            ans = max(ans, dp)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
