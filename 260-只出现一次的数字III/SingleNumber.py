# -*- coding: utf-8 -*-
# LeetCode 260-只出现一次的数字III

"""
Created on Fri Oct 30 23:53 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        l = 0
        while xor & 1 == 0:
            xor >>= 1
            l += 1
        xor1, xor2 = 0, 0
        for num in nums:
            if (num >> l) & 1 == 0:
                xor1 ^= num
            else:
                xor2 ^= num
        return [xor1, xor2]

        # counts = set()
        # for num in nums:
        #     if num in counts:
        #         counts.remove(num)
        #     else:
        #         counts.add(num)
        # return list(counts)


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1, 2, 1, 3, 2, 5]))
