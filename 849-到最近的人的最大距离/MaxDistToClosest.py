# -*- coding: utf-8 -*-
# LeetCode 849-到最近的人的最大距离

"""
Created on Sat Feb 20 17:46 2021

@author: _Mumu
Environment: py37
"""

class Solution:
    def maxDistToClosest(self, seats: list) -> int:
        n = len(seats)
        left = -1
        right = 0
        max_dist = 0
        last_seated = -1
        for i in range(n):
            if seats[i]:
                right = i
                if left == -1:
                    left = i
                if last_seated != -1:
                    max_dist = max(max_dist, i-last_seated)
                last_seated = i
        print('{} {} {}'.format(left, right, max_dist))
        return max(left, n-1-right, max_dist//2)

        # 以下是一个神奇的写法

        # used = [index for index, seat in enumerate(seats) if seat == 1]
        # return max(max([right - left for left, right in zip([used[0]] + used, used + [used[-1]])]) // 2,
        #            used[0],
        #            len(seats) - used[-1] - 1)

if __name__ == '__main__':
    s = Solution()
    print(s.maxDistToClosest([1, 0, 0, 0, 0, 1, 0, 1]))