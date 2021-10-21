# -*- coding: utf-8 -*-
# LeetCode 66-加一

"""
Created on Thu Oct 21 21:28 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 2, 3, 9, 9]))
