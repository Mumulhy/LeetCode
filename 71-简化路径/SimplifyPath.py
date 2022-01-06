# -*- coding: utf-8 -*-
# LeetCode 71-简化路径

"""
Created on Thu Jan 6 12:00 2022

@author: _Mumu
Environment: py38
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for d in path.split('/'):
            if d and d != '.':
                if d == '..':
                    if res:
                        res.pop()
                else:
                    res.append(d)
        return '/' + '/'.join(res)

if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath('/home/'))