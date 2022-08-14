# -*- coding: utf-8 -*-
# LeetCode 1422-分割字符串的最大得分

"""
Created on Sun Aug 14 10:31 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def maxScore(self, s: str) -> int:
        ones, zeros = [0], [0]
        for ch in s[:-1]:
            if ch == '0':
                zeros.append(zeros[-1] + 1)
            else:
                zeros.append(zeros[-1])
        for ch in s[::-1]:
            if ch == '1':
                ones.append(ones[-1] + 1)
            else:
                ones.append(ones[-1])
        ones = ones[1:][::-1]
        return max(zeros[i] + ones[i] for i in range(1, len(ones)))


if __name__ == '__main__':
    s = Solution()
    print(s.maxScore("11"))
