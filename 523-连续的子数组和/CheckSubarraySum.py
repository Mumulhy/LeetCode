# -*- coding: utf-8 -*-
# LeetCode 523-连续的子数组和

"""
Created on Fri Jun 2 23:07 2021

@author: _Mumu
Environment: py38
"""

class Solution:
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        k_mod_first = {}
        totals = [nums[0]]
        for i in nums[1:]:
            totals.append(totals[-1]+i)
        for i, total in enumerate(totals):
            mod = total % k
            if mod == 0 and i >= 1:
                return True
            elif mod in k_mod_first:
                if i - k_mod_first[mod] >= 2:
                    return True
            else:
                k_mod_first[mod] = i
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.checkSubarraySum([23,2,4,6,6],7))