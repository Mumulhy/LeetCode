# -*- coding: utf-8 -*-
# LeetCode 1417-重新格式化字符串

"""
Created on Thu Aug 11 09:21 2022

@author: _Mumu
Environment: py39
"""


class Solution:
    def reformat(self, s: str) -> str:
        digits = []
        letter = []
        for ch in s:
            if ch.isdigit():
                digits.append(ch)
            else:
                letter.append(ch)
        if abs((d := len(digits)) - (l := len(letter))) > 1:
            return ''
        if d < l:
            digits, letter = letter, digits
        ans = [''] * (d + l)
        ans[::2], ans[1::2] = digits, letter
        return ''.join(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.reformat("ab123"))
