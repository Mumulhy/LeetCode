# -*- coding: utf-8 -*-
# LeetCode 1588-所有奇数长度子数组的和

"""
Created on Sun Aug 29 23:16 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            ans += arr[i] * (((i + 1) // 2) * ((n - i) // 2) + (i // 2 + 1) * ((n - i - 1) // 2 + 1))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
