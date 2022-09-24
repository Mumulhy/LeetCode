# -*- coding: utf-8 -*-
# LeetCode 1652-拆炸弹

"""
Created on Sat Sept 24 12:18 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        curr_sum = sum(code[k:]) if k < 0 else sum(code[1:1 + k])
        left = k if k < 0 else 1
        k = abs(k)
        ans = []
        for _ in range(n):
            ans.append(curr_sum)
            curr_sum += code[(left + k) % n] - code[left]
            left = (left + 1) % n
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.decrypt(code=[2, 4, 9, 3], k=-2))
