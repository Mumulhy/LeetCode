# -*- coding: utf-8 -*-
# LeetCode 1224-最大相等频率

"""
Created on Thu Aug 18 09:42 2022

@author: _Mumu
Environment: py39
"""

from collections import Counter
from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq, cnt = Counter(), Counter()
        ans = max_freq = 0
        for i, num in enumerate(nums):
            if num in cnt:
                freq[cnt[num]] -= 1
            cnt[num] += 1
            freq[cnt[num]] += 1
            max_freq = max(max_freq, cnt[num])
            if (max_freq == 1
                    or (freq[max_freq] == 1
                        and freq[max_freq] * max_freq + freq[max_freq - 1] * (max_freq - 1) == i + 1)
                    or (freq[1] == 1 and freq[max_freq] * max_freq == i)):
                ans = i + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxEqualFreq([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]))
