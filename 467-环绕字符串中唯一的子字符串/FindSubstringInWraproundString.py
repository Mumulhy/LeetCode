# -*- coding: utf-8 -*-
# LeetCode 467-环绕字符串中唯一的子字符串

"""
Created on Wed May 25 09:30 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        cnt = 0
        last = ''
        for ch in p:
            if last and (ord(ch) - ord(last)) % 26 != 1:
                cnt = 0
            last = ch
            cnt += 1
            dp[ch] = max(dp[ch], cnt)
        return sum(dp.values())


if __name__ == '__main__':
    s = Solution()
    print(s.findSubstringInWraproundString('zab'))
