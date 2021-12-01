# -*- coding: utf-8 -*-
# LeetCode 1446-连续字符

"""
Created on Wed Dec 1 10:34 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        curr_power = 0
        last_letter = ''
        for letter in s:
            if letter == last_letter:
                curr_power += 1
            else:
                curr_power = 1
            ans = max(ans, curr_power)
            last_letter = letter
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxPower("abbcccddddeeeeedcba"))
