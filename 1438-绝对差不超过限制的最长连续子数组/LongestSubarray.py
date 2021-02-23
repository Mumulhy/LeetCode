# -*- coding: utf-8 -*-
# LeetCode 1438-绝对差不超过限制的最长连续子数组

"""
Created on Mon Feb 22 17:47 2021

@author: _Mumu
Environment: py37
"""

class Solution:
    def longestSubarray(self, nums: list, limit: int) -> int:
        from collections import deque
        q_max = deque()
        q_min = deque()
        n = len(nums)
        left = 0
        right = 0
        res = 0
        while right < n:
            while q_max and q_max[-1] < nums[right]:
                q_max.pop()
            while q_min and q_min[-1] > nums[right]:
                q_min.pop()
            q_max.append(nums[right])
            q_min.append(nums[right])
            while q_max[0] - q_min[0] > limit:
                if nums[left] == q_max[0]:
                    q_max.popleft()
                elif nums[left] == q_min[0]:
                    q_min.popleft()
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res

        # 以下为滑动窗口+有序集合代码

        # from sortedcontainers.sortedlist import SortedList
        # sl = SortedList()
        # n = len(nums)
        # left = 0
        # right = 0
        # res = 0
        # while right < n:
        #     sl.add(nums[right])
        #     while sl[-1] - sl[0] > limit:
        #         sl.remove(nums[left])
        #         left += 1
        #     right += 1
        #     res = max(res, right-left)
        # return res

        # 以下为自己写的超时的代码

        # left = 0
        # right = 1
        # n = len(nums)
        # max_num = nums[0]
        # min_num = nums[0]
        # res = 1
        # while 1:
        #     if right == n:
        #         res = max(res, right-left)
        #         break
        #     elif abs(nums[right]-max_num) <= limit and abs(nums[right]-min_num) <= limit:
        #         max_num = max(max_num, nums[right])
        #         min_num = min(min_num, nums[right])
        #         right += 1
        #     elif left == right-1:
        #         left += 1
        #         right += 1
        #         max_num = nums[left]
        #         min_num = nums[left]
        #     else:
        #         res = max(res, right-left)
        #         left += 1
        #         if max_num in nums[left:right]:
        #             pass
        #         else:
        #             max_num = max(nums[left:right])
        #         if min_num in nums[left:right]:
        #             pass
        #         else:
        #             min_num = min(nums[left:right])
        # return res

if __name__ == '__main__':
    s = Solution()
    print(s.longestSubarray([4,2,2,2,4,4,2,2], 0))