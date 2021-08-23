# -*- coding: utf-8 -*-
# LeetCode 1646-获取生成数组中的最大值

"""
Created on Mon Aug 23 16:56 2021

@author: _Mumu
Environment: py38
"""

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        nums = [0, 1]
        num_max = 1
        for i in range(2, n + 1):
            if i & 1 == 1:
                nums.append(nums[i//2] + nums[i//2+1])
                if nums[-1] > num_max:
                    num_max = nums[-1]
            else:
                nums.append(nums[i//2])
        return num_max

if __name__ == '__main__':
    s = Solution()
    print(s.getMaximumGenerated(21))