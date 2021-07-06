# -*- coding: utf-8 -*-
# LeetCode 1418-点菜展示表

"""
Created on Fri Jul 6 21:41 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        menu_list = []
        result = []
        for order in orders:
            if order[2] not in menu_list:
                menu_list.append(order[2])
        result.append(['Table'] + sorted(menu_list))
        orders.sort(key=lambda x: int(x[1]))
        table_list = []
        for order in orders:
            if order[1] not in table_list:
                result.append([order[1]] + ['0'] * len(menu_list))
                table_list.append(order[1])
            result[-1][result[0].index(order[2])] = str(int(result[-1][result[0].index(order[2])]) + 1)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.displayTable([["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
                          ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]))
