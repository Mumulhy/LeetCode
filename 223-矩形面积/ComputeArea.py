# -*- coding: utf-8 -*-
# LeetCode 223-矩形面积

"""
Created on Thu Sept 30 14:30 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        cxDiff, cyDiff = min(ax2, bx2) - max(ax1, bx1), min(ay2, by2) - max(ay1, by1)
        if cxDiff > 0 and cyDiff > 0:
            return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - cxDiff * cyDiff
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)

        # if bx1 <= ax1 <= bx2:
        #     cx1 = ax1
        # elif ax1 <= bx1 <= ax2:
        #     cx1 = bx1
        # else:
        #     return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        # if ax1 <= bx2 <= ax2:
        #     cx2 = bx2
        # elif bx1 <= ax2 <= bx2:
        #     cx2 = ax2
        # else:
        #     return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        # if by1 <= ay1 <= by2:
        #     cy1 = ay1
        # elif ay1 <= by1 <= ay2:
        #     cy1 = by1
        # else:
        #     return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        # if ay1 <= by2 <= ay2:
        #     cy2 = by2
        # elif by1 <= ay2 <= by2:
        #     cy2 = ay2
        # else:
        #     return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        # return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - abs(cx1 - cx2) * abs(cy1 - cy2)


if __name__ == '__main__':
    s = Solution()
    print(s.computeArea(ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-2, by1=-2, bx2=2, by2=2))
