# -*- coding: utf-8 -*-
# LeetCode 165-比较版本号

"""
Created on Tues Sept 1 21:11 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1 = len(version1)
        n2 = len(version2)
        i, j = 0, 0
        while i < n1 or j < n2:
            e1 = 0
            e2 = 0
            while i < n1 and version1[i] != '.':
                e1 = e1 * 10 + int(version1[i])
                i += 1
            while j < n2 and version2[j] != '.':
                e2 = e2 * 10 + int(version2[j])
                j += 1
            if e1 != e2:
                return 1 if e1 > e2 else -1
            i += 1
            j += 1
        return 0

        # n1 = len(version1)
        # n2 = len(version2)
        # i, j = 0, 0
        # while i < n1 and j < n2:
        #     e1 = ''
        #     e2 = ''
        #     while i < n1 and version1[i] != '.':
        #         e1 += version1[i]
        #         i += 1
        #     while j < n2 and version2[j] != '.':
        #         e2 += version2[j]
        #         j += 1
        #     if int(e1) > int(e2):
        #         return 1
        #     if int(e1) < int(e2):
        #         return -1
        #     i += 1
        #     j += 1
        # if i >= n1:
        #     while j < n2:
        #         e2 = ''
        #         while j < n2 and version2[j] != '.':
        #             e2 += version2[j]
        #             j += 1
        #         if int(e2) > 0:
        #             return -1
        #         j += 1
        # if j >= n2:
        #     while i < n1:
        #         e1 = ''
        #         while i < n1 and version1[i] != '.':
        #             e1 += version1[i]
        #             i += 1
        #         if int(e1) > 0:
        #             return 1
        #         i += 1
        # return 0


if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion(version1="7.5.3.4", version2="7.5.3"))
