# -*- coding: utf-8 -*-
# LeetCode 973-最接近原点的K个点

"""
Created on Sat Feb 20 20:23 2021

@author: _Mumu
Environment: py37
"""

class Solution:
    def kClosest(self, points: list, K: int) -> list:
        points.sort(key=lambda x: x[0]**2+x[1]**2)
        return points[0:K]

        # 以下是自己初次写的占用内存较大的写法

        # dist_list = [point[0]**2 + point[1]**2 for point in points]
        # res = [point for point, dist in sorted(zip(points, dist_list), key=lambda x:x[1])]
        # return res[0:K]

if __name__ == '__main__':
    s = Solution()
    print(s.kClosest([[-5, 4], [-6, -5], [4, 6]], 2))