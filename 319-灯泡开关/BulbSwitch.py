# -*- coding: utf-8 -*-
# LeetCode 319-灯泡开关

"""
Created on Mon Nov 15 16:41 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** 0.5)

        # lights = [1] * n
        # for i in range(2, n + 1):
        #     x = i - 1
        #     while x < n:
        #         lights[x] = 1 - lights[x]
        #         x += i
        # return sum(lights)

        # ans = 0
        # for i in range(1, n + 1):
        #     curr_light_on = True
        #     for j in range(2, i + 1):
        #         if i % j == 0:
        #             curr_light_on = not curr_light_on
        #     if curr_light_on:
        #         ans += 1
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.bulbSwitch(3))
