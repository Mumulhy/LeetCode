# -*- coding: utf-8 -*-
# LeetCode 1846-减小和重新排列数组后的最大元素

"""
Created on Thu Jul 15 16:30 2021

@author: _Mumu
Environment: py38
"""

from typing import List

from sortedcontainers import SortedDict, SortedList


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        count_times = SortedDict()
        count_more_than_one = SortedList()
        for number in arr:
            if number >= n:
                num = n
            else:
                num = number
            if num in count_times:
                count_times[num] += 1
            else:
                count_times[num] = 1
        for num in count_times:
            if count_times[num] > 1:
                count_more_than_one.add(num)
        max_num = 0
        for i in range(1, n + 1):
            if i in count_times:
                max_num += 1
            elif count_more_than_one:
                while count_more_than_one and count_more_than_one[0] < i:
                    count_more_than_one.remove(count_more_than_one[0])
                if count_more_than_one:
                    max_num += 1
                    count_times[count_more_than_one[0]] -= 1
                    if count_times[count_more_than_one[0]] == 1:
                        count_more_than_one.remove(count_more_than_one[0])
        return max_num

        # 看完下面这段代码我的内心只有一个草字
        # arr.sort()
        # 返回 = 0
        # for i in arr:
        #     if i > 返回: 返回 += 1
        # return 返回


if __name__ == '__main__':
    s = Solution()
    print(s.maximumElementAfterDecrementingAndRearranging([2000] * 1000))
