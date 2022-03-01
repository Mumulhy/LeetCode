# -*- coding: utf-8 -*-
# LeetCode 6-Z字形变换

"""
Created on Tues Mar 1 17:00 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        ans = [s[::2 * numRows - 2]]
        for i in range(1, numRows - 1):
            ans.append('')
            p = i
            jump = 2 * (numRows - 1 - i)
            while p < n:
                ans[-1] += s[p]
                p += jump
                jump = 2 * (numRows - 1) - jump
        ans.append(s[numRows - 1::2 * numRows - 2])
        return ''.join(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.convert(s="PAYPALISHIRING", numRows=5))
