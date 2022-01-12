# -*- coding: utf-8 -*-
# LeetCode 334-递增的三元子序列

"""
Created on Wed Jan 12 10:28 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

        # first = float('inf')
        # second = float('inf')
        # first_fake = float('inf')
        # for num in nums:
        #     if num > second:
        #         return True
        #     if num < first:
        #         if second == float('inf'):
        #             first = num
        #         elif num < first_fake:
        #             first_fake = num
        #         elif num > first_fake:
        #             first = first_fake
        #             second = num
        #             first_fake = float('inf')
        #     elif num < second:
        #         if num > first:
        #             second = num
        #         if first_fake < float('inf'):
        #             first = first_fake
        #             second = num
        #             first_fake = float('inf')
        # return False


if __name__ == '__main__':
    s = Solution()
    print(s.increasingTriplet([4, 6, 3, 4, 5]))
