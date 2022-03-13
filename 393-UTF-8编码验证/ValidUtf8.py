# -*- coding: utf-8 -*-
# LeetCode 393-UTF-8编码验证

"""
Created on Sun Mar 13 10:30 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        need = 0
        for num in data:
            if need == 0:
                if num < 128:
                    pass
                elif 192 <= num < 224:
                    need = 1
                elif 224 <= num < 240:
                    need = 2
                elif 240 <= num < 248:
                    need = 3
                else:
                    return False
            else:
                if 128 <= num < 192:
                    need -= 1
                else:
                    return False
        return need == 0


if __name__ == '__main__':
    s = Solution()
    print(s.validUtf8([235, 140, 4]))
