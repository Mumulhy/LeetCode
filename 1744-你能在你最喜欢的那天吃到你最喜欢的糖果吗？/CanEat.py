# -*- coding: utf-8 -*-
# LeetCode 1744-你能在你最喜欢的那天吃到你最喜欢的糖果吗？

"""
Created on Fri Jun 1 21:14 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def canEat(self, candiesCount: list, queries: list) -> list:
        total = [candiesCount[0]]
        for candies in candiesCount[1:]:
            total.append(total[-1] + candies)
        answer = []
        for query in queries:
            query_pass = False
            x2 = 1 if query[0] == 0 else total[query[0] - 1] + 1
            if x2 > (query[1] + 1) * query[2]:
                pass
            elif total[query[0]] < query[1] + 1:
                pass
            else:
                query_pass = True
            answer.append(query_pass)
        return answer


if __name__ == '__main__':
    s = Solution()
    print(
        s.canEat(candiesCount=[5, 2, 6, 4, 1], queries=[[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]))
