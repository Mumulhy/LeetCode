# -*- coding: utf-8 -*-
# LeetCode 525-连续数组

"""
Created on Fri Jun 3 20:48 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def findMaxLength(self, nums: list) -> int:
        prefix_sums = [1 if nums[0] == 1 else -1]
        for i in nums[1:]:
            if i == 1:
                prefix_sums.append(prefix_sums[-1] + 1)
            else:
                prefix_sums.append(prefix_sums[-1] - 1)
        presum_first = {0: -1}
        max_len = 0
        for i, presum in enumerate(prefix_sums):
            if presum in presum_first:
                if i - presum_first[presum] > max_len:
                    max_len = i - presum_first[presum]
            else:
                presum_first[presum] = i
        return max_len

        # 大佬的代码就是这么简洁牛逼
        # m = {0: -1}
        # cnt = 0
        # res = 0
        # for i, num in enumerate(nums):
        #     cnt = cnt + 1 if num == 1 else cnt - 1
        #     if cnt in m:
        #         res = max(res, i - m[cnt])
        #     else:
        #         m[cnt] = i
        #
        # return res


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxLength(nums=[0, 1, 0]))
