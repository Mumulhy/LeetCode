# -*- coding: utf-8 -*-
# LeetCode 1748-唯一元素的和

"""
Created on Sun Feb 6 11:58 2022

@author: _Mumu
Environment: py38
"""

from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for num in cnt:
            if cnt[num] == 1:
                ans += num
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.sumOfUnique([1, 2, 3, 2]))
