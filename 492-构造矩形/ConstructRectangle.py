# -*- coding: utf-8 -*-
# LeetCode 492-构造矩形

"""
Created on Fri Oct 23 23:14 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = int(area ** 0.5)
        while W >= 1:
            if area % W == 0:
                return [area // W, W]
            W -= 1

        # ans = [area, 1]
        # for W in range(2, int(area ** 0.5) + 1):
        #     if area % W == 0:
        #         ans = [area // W, W]
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.constructRectangle(4))
