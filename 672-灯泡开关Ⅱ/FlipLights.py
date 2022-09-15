# -*- coding: utf-8 -*-
# LeetCode 672-灯泡开关Ⅱ

"""
Created on Thu Sept 15 09:51 2022

@author: _Mumu
Environment: py39
"""


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        seen = set()
        for i in range(2 ** 4):
            press_arr = [(i >> j) & 1 for j in range(4)]
            if sum(press_arr) & 1 == presses & 1 and sum(press_arr) <= presses:
                status = press_arr[0] ^ press_arr[2] ^ press_arr[3]
                if n >= 2:
                    status |= (press_arr[0] ^ press_arr[1]) << 1
                if n >= 3:
                    status |= (press_arr[0] ^ press_arr[2]) << 2
                if n >= 4:
                    status |= (press_arr[0] ^ press_arr[1] ^ press_arr[3]) << 3
                seen.add(status)
        return len(seen)


if __name__ == '__main__':
    s = Solution()
    print(s.flipLights(3, 1))
