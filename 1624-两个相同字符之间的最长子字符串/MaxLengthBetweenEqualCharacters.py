# -*- coding: utf-8 -*-
# LeetCode 1624-两个相同字符之间的最长子字符串

"""
Created on Sat Sept 17 16:57 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pos = {}
        ans = -1
        for i, ch in enumerate(s):
            if ch in pos:
                ans = max(ans, i - pos[ch] - 1)
            else:
                pos[ch] = i
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxLengthBetweenEqualCharacters("cabbac"))
