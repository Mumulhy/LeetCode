# -*- coding: utf-8 -*-
# LeetCode 1646-获取生成数组中的最大值

"""
Created on Tues Aug 24 14:30 2021

@author: _Mumu
Environment: py38
"""

# from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = [float('inf')] * n
        f[src] = 0
        price = float('inf')
        for _ in range(k + 1):
            g = [float('inf')] * n
            for i, j, cost in flights:
                g[j] = min(g[j], f[i] + cost)
            f = g
            price = min(price, f[dst])
        if price == float('inf'):
            return -1
        else:
            return price

        # 使用深度优先遍历所有路径并剔除长度超过k的路径，分别计算剩下路径花费，结果超时的代码
        # flights_dict = defaultdict(dict)
        # for flight in flights:
        #     flights_dict[flight[0]][flight[1]] = flight[2]
        # price = -1
        #
        # def search(node: int, route: list) -> None:
        #     nonlocal price
        #     if route and route[-1] == dst:
        #         route_price = flights_dict[src][route[0]]
        #         for i in range(len(route) - 1):
        #             route_price += flights_dict[route[i]][route[i + 1]]
        #         if price == -1 or route_price < price:
        #             price = route_price
        #         return
        #     elif len(route) == k + 1:
        #         return
        #     else:
        #         for next_node in flights_dict[node]:
        #             if next_node in route:
        #                 continue
        #             search(next_node, route + [next_node])
        #         return
        #
        # search(src, [])
        # return price


if __name__ == '__main__':
    s = Solution()
    print(s.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1))
