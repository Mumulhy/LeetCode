# -*- coding: utf-8 -*-
# LeetCode 137-只出现一次的数字II

"""
Created on Fri Apr 30 15:21 2021

@author: _Mumu
Environment: py37
"""


class Solution:
    def singleNumber(self, nums: list) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        for num in nums_dict:
            if nums_dict[num] == 1:
                return num

        # 大佬写的不占用额外空间的代码
        # while nums:
        #     i = nums.pop()
        #     if i in nums:
        #         nums.remove(i)
        #         nums.remove(i)
        #     else:
        #         return i

        # 大佬写的一行解决而且还巨快的代码
        # return (3 * sum(set(nums)) - sum(nums)) // 2


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2, 2, 3, 2]))
