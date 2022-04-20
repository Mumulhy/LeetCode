# -*- coding: utf-8 -*-
# LeetCode 388-文件的最长绝对路径

"""
Created on Wed Apr 20 10:50 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dirs = [(dr.count('\t'), dr.lstrip('\t')) for dr in input.split('\n')]
        curr_path = []
        ans = 0
        for layer, dr in dirs:
            while len(curr_path) > layer:
                curr_path.pop()
            curr_path.append(dr)
            if '.' in dr:
                ans = max(ans, sum(map(len, curr_path)) + len(curr_path) - 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt"))
