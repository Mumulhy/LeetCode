# -*- coding: utf-8 -*-
# LeetCode 81-搜索旋转排序数组II

"""
Created on Wed Apr 7 23:09 2021

@author: _Mumu
Environment: py37
"""


class Solution:
    def search(self, nums: list, target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while True:
            if nums[left] == target or nums[right] == target:
                return True
            if left == right or left == right - 1:
                return False
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] and nums[right] == nums[mid]:
                left += 1
                right -= 1
            elif nums[left] < target:
                if nums[mid] > target:
                    right = mid
                elif nums[right] > target or nums[mid] >= nums[left]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[mid] < target:
                    left = mid
                elif nums[right] < target:
                    return False
                else:
                    if nums[left] <= nums[mid]:
                        left = mid
                    else:
                        right = mid

        # 错惹
        # n = len(nums)
        # Ilen = n // 2
        # index = [Ilen]
        # existI = -1
        # existII = -1
        # while True:
        #     for item in index:
        #         if nums[item] == target:
        #             return True
        #     if Ilen == 0:
        #         return False
        #     m = len(index)
        #     Ilen = Ilen // 2
        #     if m > 1:
        #         for i in range(m - 1):
        #             if target > nums[index[i]] and target < nums[index[i + 1]]:
        #                 existI = i
        #             elif nums[index[i]] > nums[index[i + 1]] and target < nums[index[i + 1]]:
        #                 existII = i
        #         if existI == -1 and existII == -1:
        #             index = [Ilen, index[0], index[-1], index[-1] + Ilen]
        #         else:
        #             index = [index[existI], index[existI] + Ilen, index[existI + 1]]
        #     else:
        #         index = [Ilen, index[0], index[0] + Ilen]
        #     existI = -1
        #     existII = -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([2, 5, 6, 0, 0, 1, 2], 3))
