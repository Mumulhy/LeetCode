# -*- coding: utf-8 -*-
# LeetCode 744-寻找比目标字母大的最小字母

"""
Created on Sun Apr 3 10:38 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect(letters, target)
        return letters[0] if idx == len(letters) else letters[idx]


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreatestLetter(letters=["c", "f", "j"], target="z"))
