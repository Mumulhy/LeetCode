# -*- coding: utf-8 -*-
# LeetCode 846-一手顺子

"""
Created on Thu Dec 30 11:02 2021

@author: _Mumu
Environment: py38
"""

from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        cnt = Counter(hand)
        sorted_keys = sorted(cnt.keys())
        m = len(sorted_keys)
        i = 0
        while i < m:
            for j in range(groupSize):
                curr_key = sorted_keys[i] + j
                if curr_key not in cnt:
                    return False
                cnt[curr_key] -= 1
                if cnt[curr_key] == 0:
                    cnt.pop(curr_key)
            while i < m and sorted_keys[i] not in cnt:
                i += 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8, 9, 10, 12], groupSize=3))
