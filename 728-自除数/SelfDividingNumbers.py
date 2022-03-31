# -*- coding: utf-8 -*-
# LeetCode 728-自除数

"""
Created on Thu Mar 31 09:37 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            seed = num
            div = True
            while seed:
                divisor = seed % 10
                if divisor == 0 or num % divisor != 0:
                    div = False
                    break
                seed //= 10
            if div:
                ans.append(num)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.selfDividingNumbers(left=1, right=10000))
