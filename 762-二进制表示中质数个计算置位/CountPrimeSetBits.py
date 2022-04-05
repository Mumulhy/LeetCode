# -*- coding: utf-8 -*-
# LeetCode 762-二进制表示中质数个计算置位

"""
Created on Tues Apr 5 08:18 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum((665772 >> bin(num).count('1')) & 1 for num in range(left, right + 1))

        # prime = {2, 3, 5, 7, 11, 13, 17, 19}
        # return sum(bin(num).count('1') in prime for num in range(left, right + 1))


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimeSetBits(left=10, right=15))
