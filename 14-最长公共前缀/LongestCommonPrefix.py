# -*- coding: utf-8 -*-
# LeetCode 14-最长公共前缀

"""
Created on Fri Sept 3 22:20 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        commonPrefix = ''
        for i in range(len(strs[0])):
            isCommon = True
            for str in strs[1:]:
                if len(str) < i + 1 or str[i] != strs[0][i]:
                    isCommon = False
                    break
            if isCommon:
                commonPrefix += strs[0][i]
            else:
                break
        return commonPrefix


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["ab", "a"]))
