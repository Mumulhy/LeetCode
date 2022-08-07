# -*- coding: utf-8 -*-
# LeetCode 636-函数的独占时间

"""
Created on Sun Aug 7 10:05 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        last_time_stamp = 0
        last_is_start = False
        for log in logs:
            log_list = log.split(':')
            func, time_stamp = int(log_list[0]), int(log_list[2])
            is_start = log_list[1] == 'start'
            if is_start:
                if stack:
                    ans[stack[-1]] += time_stamp - last_time_stamp
                    if not last_is_start:
                        ans[stack[-1]] -= 1
                stack.append(func)
            else:
                assert func == stack[-1]
                ans[func] += time_stamp - last_time_stamp
                if last_is_start:
                    ans[func] += 1
                stack.pop()
            last_time_stamp = time_stamp
            last_is_start = is_start
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.exclusiveTime(n=1, logs=["0:start:0", "0:end:0"]))
