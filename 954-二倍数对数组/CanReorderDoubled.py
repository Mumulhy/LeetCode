# -*- coding: utf-8 -*-
# LeetCode 954-二倍数对数组

"""
Created on Fri Apr 1 10:30 2022

@author: _Mumu
Environment: py38
"""

from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        for num in sorted(cnt.keys(), key=lambda x: abs(x)):
            if cnt[num] == 0:
                continue
            if num * 2 in cnt and cnt[num * 2] >= cnt[num]:
                cnt[num * 2] -= cnt[num]
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canReorderDoubled([4, -2, 2, -4]))
