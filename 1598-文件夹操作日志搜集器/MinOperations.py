# -*- coding: utf-8 -*-
# LeetCode 1598-文件夹操作日志搜集器

"""
Created on Fri Sept 9 12:52 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0
        for log in logs:
            if log == '../':
                if steps > 0:
                    steps -= 1
            elif log == './':
                pass
            else:
                steps += 1
        return steps


if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(["d1/", "d2/", "../", "d21/", "./"]))
