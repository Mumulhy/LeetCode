# -*- coding: utf-8 -*-
# LeetCode 1672-最富有客户的资产总量

"""
Created on Thu Apr 14 10:23 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(wealth) for wealth in accounts)


if __name__ == '__main__':
    s = Solution()
    print(s.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
