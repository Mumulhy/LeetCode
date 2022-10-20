# -*- coding: utf-8 -*-
# LeetCode 1700-无法吃午餐的学生数量

"""
Created on Wed Oct 19 09:43 2022

@author: _Mumu
Environment: py39
"""

from collections import Counter
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        cnt = Counter(students)
        i = 0
        while i < n:
            if cnt[sandwiches[i]] > 0:
                cnt[sandwiches[i]] -= 1
            else:
                break
            i += 1
        return n - i


if __name__ == '__main__':
    s = Solution()
    print(s.countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]))
