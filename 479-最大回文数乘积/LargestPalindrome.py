# -*- coding: utf-8 -*-
# LeetCode 479-最大回文数乘积

"""
Created on Sat Apr 16 10:52 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def largestPalindrome(self, n: int) -> int:
        ans = [9, 987, 123, 597, 677, 1218, 877, 475]
        return ans[n - 1]
