# -*- coding: utf-8 -*-
# LeetCode 870-优势洗牌

"""
Created on Sat Oct 8 10:20 2022

@author: _Mumu
Environment: py39
"""

from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        idx1 = list(range(n))
        idx2 = list(range(n))
        idx1.sort(key=lambda x: nums1[x])
        idx2.sort(key=lambda x: nums2[x])

        ans = [0] * n
        left, right = 0, n - 1
        for i in range(n):
            if nums1[idx1[i]] > nums2[idx2[left]]:
                ans[idx2[left]] = nums1[idx1[i]]
                left += 1
            else:
                ans[idx2[right]] = nums1[idx1[i]]
                right -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.advantageCount(nums1=[12, 24, 8, 32], nums2=[13, 25, 32, 11]))
