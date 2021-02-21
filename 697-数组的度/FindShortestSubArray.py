# -*- coding: utf-8 -*-
# LeetCode 697-数组的度

"""
Created on Sun Feb 21 15:55 2021

@author: _Mumu
Environment: py37
"""

class Solution:
    def findShortestSubArray(self, nums: list) -> int:
        nums_dict = dict(zip(set(nums), [[] for num in set(nums)]))
        for i, num in enumerate(nums):
            nums_dict[num].append(i)
        max_times = 0
        max_nums = []
        for num in nums_dict.keys():
            now_times = len(nums_dict[num])
            if now_times > max_times:
                max_times = now_times
                max_nums.clear()
                max_nums.append(num)
            elif now_times == max_times:
                max_nums.append(num)
        res_num = min(max_nums, key=lambda x: nums_dict[x][-1]-nums_dict[x][0])
        return nums_dict[res_num][-1]-nums_dict[res_num][0]+1

if __name__ == '__main__':
    s = Solution()
    print(s.findShortestSubArray([1,2,2,3,1,4,2]))