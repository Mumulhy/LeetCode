# -*- coding: utf-8 -*-
# LeetCode 902-最大为N的数字组合

"""
Created on Tues Oct 18 10:06 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        m = len(digits)
        s = str(n)
        bits = []
        is_limit = True
        for ch in s:
            if not is_limit:
                bits.append(m - 1)
                continue
            select_idx = -1
            for j, d in enumerate(digits):
                if d > ch:
                    break
                select_idx = j
            if select_idx >= 0:
                bits.append(select_idx)
                if digits[select_idx] < ch:
                    is_limit = False
            else:
                sz = len(bits)
                while bits and bits[-1] == 0:
                    bits.pop()
                if bits:
                    bits[-1] -= 1
                else:
                    sz -= 1
                bits.extend([m - 1] * (sz - len(bits) + 1))
                is_limit = False
        ans = 0
        for b in bits:
            ans = ans * m + b + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.atMostNGivenDigitSet(digits=["7"], n=8))
