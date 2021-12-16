# -*- coding: utf-8 -*-
# LeetCode 1610-可见点的最大数目

"""
Created on Wed Dec 16 19:44 2021

@author: _Mumu
Environment: py38
"""

# from bisect import bisect
# from numpy import tan, pi
from math import atan2, pi
from typing import List


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        n = len(points)
        pos_x, pos_y = location
        polar_degrees = []
        origins = 0
        for x, y in points:
            if x == pos_x and y == pos_y:
                origins += 1
                continue
            polar_degrees.append(atan2(y - pos_y, x - pos_x))
        polar_degrees.sort()
        m = n - origins
        polar_degrees += [deg + 2 * pi for deg in polar_degrees]
        alpha = pi * angle / 180
        left, right = 0, 0
        cnt = 0
        while left < m:
            while polar_degrees[right] - polar_degrees[left] <= alpha:
                right += 1
            cnt = max(cnt, right - left)
            if cnt == m:
                return n
            while polar_degrees[right] - polar_degrees[left] > alpha:
                left += 1
        return cnt + origins

        # n = len(points)
        # pos_x, pos_y = location
        # quadrant_and_gradient = {i: [] for i in range(1, 5)}
        # origins = 0
        # for x, y in points:
        #     if x == pos_x and y == pos_y:
        #         origins += 1
        #         continue
        #     x -= pos_x
        #     y -= pos_y
        #     if x > 0 and y >= 0:
        #         quadrant_and_gradient[1].append(y / x)
        #     elif x <= 0 and y > 0:
        #         quadrant_and_gradient[2].append(y / x if x != 0 else float('-inf'))
        #     elif x < 0 and y <= 0:
        #         quadrant_and_gradient[3].append(y / x)
        #     else:
        #         quadrant_and_gradient[4].append(y / x if x != 0 else float('-inf'))
        # for i in range(1, 5):
        #     quadrant_and_gradient[i].sort()
        # tan_alpha = tan(pi * angle / 180) if angle != 90 and angle != 270 else float('inf')
        # alpha_div_90 = angle // 90
        # quadrant_len = [0] + [len(quadrant) for quadrant in quadrant_and_gradient.values()]
        # ans = origins
        # for i in range(1, 5):
        #     last_k1 = None
        #     for k1_idx, k1 in enumerate(quadrant_and_gradient[i]):
        #         if k1 == last_k1:
        #             continue
        #         curr_ans = origins
        #         if tan_alpha == float('inf'):
        #             k2 = -1 / k1 if k1 != 0 else float('-inf')
        #         else:
        #             k2 = (tan_alpha + k1) / (1 - tan_alpha * k1) if k1 != float('-inf') else -1 / tan_alpha
        #         if k1 == 0:
        #             j = i + alpha_div_90
        #         elif k2 == 0:
        #             j = i + alpha_div_90 + 1
        #         else:
        #             if k1 * k2 > 0:
        #                 if alpha_div_90 == 0 or alpha_div_90 == 3:
        #                     j = i
        #                 else:
        #                     j = i + 2
        #             else:
        #                 if alpha_div_90 == 0 or alpha_div_90 == 1:
        #                     j = i + 1
        #                 else:
        #                     j = i + 3
        #         if j == i:
        #             k2_idx = bisect(quadrant_and_gradient[i], k2)
        #             curr_ans += k2_idx - k1_idx
        #         else:
        #             curr_ans += quadrant_len[i] - k1_idx
        #             for k in range(i + 1, j + 1):
        #                 curr_quadrant = k if k <= 4 else k - 4
        #                 if k == j:
        #                     k2_idx = bisect(quadrant_and_gradient[curr_quadrant], k2)
        #                     curr_ans += k2_idx
        #                 else:
        #                     curr_ans += quadrant_len[curr_quadrant]
        #         if curr_ans == n:
        #             return n
        #         ans = max(ans, curr_ans)
        #         last_k1 = k1
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.visiblePoints([[89, 45], [34, 13], [21, 62], [23, 30], [24, 50], [89, 70], [63, 84], [10, 1], [35, 47],
                           [94, 19], [51, 94], [5, 26], [87, 87], [27, 48], [56, 20], [19, 49], [13, 61], [17, 86],
                           [56, 1], [53, 16], [11, 6], [90, 52], [99, 25], [9, 18], [70, 74], [25, 25], [58, 70],
                           [15, 67], [59, 13], [8, 3], [20, 70], [22, 11], [36, 94], [83, 55], [58, 69], [0, 35],
                           [7, 58], [39, 43], [57, 50], [48, 65], [52, 72], [36, 94], [8, 46], [5, 67], [36, 84],
                           [50, 57], [42, 47], [9, 1], [57, 54], [35, 39], [35, 66], [15, 51], [82, 56], [64, 38],
                           [57, 3], [87, 55], [62, 48], [44, 53], [7, 6], [12, 49], [81, 31], [8, 71], [96, 20],
                           [40, 97], [59, 90], [87, 35], [99, 12], [40, 35], [96, 50], [58, 82], [76, 35], [48, 79],
                           [85, 93], [50, 6], [78, 27], [70, 16], [21, 74], [57, 21], [79, 85], [74, 100], [24, 89],
                           [90, 79], [53, 12], [29, 84], [85, 63], [51, 57], [100, 34], [78, 68], [48, 5], [34, 36],
                           [61, 17], [71, 92], [79, 17], [36, 25], [87, 30], [16, 30], [19, 34], [31, 97], [73, 94],
                           [56, 18], [57, 86], [32, 39], [26, 68], [44, 61], [52, 40], [9, 72], [50, 27], [42, 70],
                           [79, 74], [78, 2], [68, 5], [98, 76], [84, 84], [96, 26], [97, 53], [35, 66], [57, 27],
                           [34, 99], [45, 37], [19, 57], [8, 31], [87, 37], [46, 15], [34, 53], [31, 45], [6, 45],
                           [13, 93], [89, 36], [22, 47], [39, 96], [3, 4], [1, 61], [92, 62], [92, 68], [55, 11],
                           [13, 57], [64, 37], [93, 9], [47, 93], [75, 63], [68, 55], [11, 51], [82, 32], [97, 55],
                           [44, 80], [62, 98], [24, 84], [32, 44], [63, 79], [75, 55], [65, 96], [37, 94], [51, 51],
                           [53, 87], [32, 7], [87, 54], [96, 54], [39, 93], [91, 23], [32, 57], [26, 96], [60, 32],
                           [51, 82], [14, 100], [50, 33], [77, 63], [22, 65], [41, 4], [17, 53], [29, 34], [1, 25],
                           [89, 13], [46, 74], [86, 47], [0, 42], [73, 69], [7, 72], [24, 100], [26, 83], [73, 22],
                           [86, 17], [1, 44], [10, 50], [34, 42], [64, 39], [5, 32], [31, 97], [65, 97], [83, 16],
                           [96, 11], [90, 70], [90, 74], [58, 50], [17, 72], [89, 51], [92, 91], [60, 63], [29, 72],
                           [23, 48], [29, 60], [62, 73], [46, 18], [65, 99], [25, 10], [98, 74], [37, 39], [63, 51],
                           [18, 65], [98, 40], [19, 0], [55, 48], [37, 30], [55, 15], [15, 86], [58, 10], [55, 28],
                           [69, 64], [37, 8], [87, 2], [33, 57], [79, 45], [46, 65], [52, 36], [23, 88], [85, 16],
                           [58, 59], [80, 75], [98, 96], [2, 52], [44, 84], [77, 63], [98, 62], [51, 53], [46, 30],
                           [94, 93], [31, 40], [9, 11], [14, 100], [40, 35], [21, 46], [84, 96], [50, 76], [56, 93],
                           [61, 6], [3, 91], [68, 94], [1, 66], [5, 78], [54, 69], [3, 13], [44, 61], [8, 0], [10, 54],
                           [8, 79], [15, 35], [97, 82], [90, 17], [50, 1], [86, 66], [40, 86], [66, 13], [71, 73],
                           [93, 54], [11, 48], [62, 1], [87, 71], [48, 40], [41, 48], [34, 69], [80, 56], [81, 60],
                           [89, 90], [54, 37], [60, 62], [29, 12], [12, 75], [29, 16], [11, 98], [80, 51], [28, 79],
                           [73, 51], [53, 98], [34, 6], [89, 5], [72, 100], [77, 17], [0, 44], [69, 82], [41, 86],
                           [5, 33], [89, 0], [39, 3], [34, 46], [76, 58], [69, 94], [12, 81], [2, 80], [27, 36],
                           [77, 26], [70, 96], [32, 33], [35, 12], [83, 51], [83, 85], [69, 20], [82, 66], [81, 77],
                           [48, 33], [94, 3], [67, 45], [88, 37], [34, 97], [81, 28], [47, 86], [61, 51], [53, 70],
                           [39, 46], [16, 15], [66, 23], [75, 37], [14, 53], [26, 33], [52, 38], [16, 55], [27, 96],
                           [47, 76], [19, 62], [12, 40], [80, 70], [66, 61], [42, 16], [98, 38], [51, 21], [22, 12],
                           [29, 96], [22, 86], [57, 96], [99, 56], [34, 15], [8, 22], [69, 37], [36, 76], [59, 93],
                           [30, 40], [2, 77], [30, 2], [77, 17], [85, 55], [86, 72], [82, 93], [36, 30], [59, 10],
                           [92, 94], [14, 98], [93, 84], [96, 46], [91, 45], [99, 93], [23, 42], [47, 59], [80, 73],
                           [74, 12], [67, 77], [31, 17], [56, 96], [77, 46], [93, 59], [68, 8], [45, 60], [11, 29],
                           [54, 95], [17, 50], [56, 53], [56, 39], [51, 34], [83, 39], [93, 93], [60, 20], [31, 38],
                           [42, 51], [27, 51], [58, 24], [8, 70], [34, 28], [37, 64], [73, 63], [71, 7], [48, 71],
                           [22, 44], [92, 73], [81, 77], [85, 43], [76, 55], [33, 32], [22, 67], [13, 15], [12, 74],
                           [95, 46], [13, 21], [37, 14], [47, 93], [22, 20], [79, 58], [29, 52], [61, 28], [26, 91],
                           [1, 4], [39, 12], [60, 20], [23, 90], [8, 34], [65, 48], [40, 18], [88, 41], [24, 97],
                           [16, 47], [26, 93], [31, 62], [96, 92], [23, 75], [69, 88], [87, 9], [16, 100], [35, 18],
                           [29, 14], [54, 32], [29, 95], [76, 53], [47, 0], [21, 72], [80, 92], [6, 80], [34, 46],
                           [1, 44], [61, 82], [21, 36], [19, 42], [84, 96], [63, 86], [21, 71], [82, 58], [31, 49],
                           [52, 1], [97, 6], [63, 53], [68, 11], [13, 77], [99, 23], [78, 96], [40, 44], [59, 98],
                           [22, 16], [14, 36], [97, 53], [58, 36], [53, 98], [48, 91], [33, 10], [58, 46], [53, 26],
                           [53, 68], [44, 13], [45, 69], [57, 62], [30, 38], [92, 6], [94, 60], [15, 4], [12, 77],
                           [62, 80], [33, 26], [8, 60], [65, 83], [54, 66], [38, 71], [28, 93], [33, 32], [67, 70],
                           [47, 45], [82, 38], [76, 5], [88, 84], [52, 3], [96, 41], [59, 24], [76, 11], [94, 26],
                           [87, 47], [59, 11], [32, 58], [48, 36], [97, 51], [51, 34], [43, 0], [88, 79], [25, 35],
                           [59, 75], [11, 52], [7, 22], [39, 38], [98, 7], [70, 64], [51, 19], [59, 39], [17, 16],
                           [98, 84], [25, 13], [78, 1], [3, 1], [43, 70], [87, 59], [6, 71], [18, 85], [17, 88],
                           [97, 46], [65, 39], [70, 18], [43, 38], [46, 72], [84, 26], [97, 35], [19, 87], [41, 68],
                           [38, 91], [86, 12], [57, 81], [10, 95], [33, 83], [81, 48], [87, 42], [60, 86], [83, 80],
                           [91, 41], [22, 32], [19, 37], [2, 93], [29, 82], [51, 31], [43, 65], [78, 50], [4, 99],
                           [26, 84], [60, 71], [81, 1], [77, 80], [20, 6], [66, 37], [60, 50], [2, 9], [63, 52],
                           [34, 44], [67, 70], [48, 19], [3, 86], [59, 64], [88, 92], [33, 65], [53, 2], [99, 41],
                           [21, 84], [75, 59], [64, 9], [97, 23], [65, 40], [20, 56], [4, 75], [92, 99], [32, 6],
                           [83, 29], [14, 36], [58, 59], [69, 55], [92, 23], [11, 66], [5, 50], [85, 33], [100, 92],
                           [98, 88], [20, 49], [46, 24], [78, 90], [81, 0], [99, 52], [3, 7], [70, 59], [89, 8],
                           [59, 48], [97, 18], [24, 42], [57, 40], [32, 76], [73, 13], [28, 96], [90, 13], [74, 70],
                           [86, 25], [79, 88], [92, 84], [46, 5], [22, 38], [85, 69], [81, 8], [56, 42], [81, 26],
                           [15, 62], [46, 7], [71, 62], [44, 2], [25, 14], [85, 59], [66, 51], [31, 57], [3, 57],
                           [70, 15], [41, 37], [66, 34], [1, 69], [66, 39], [59, 51], [53, 73], [19, 52], [5, 26],
                           [27, 19], [90, 16], [10, 52], [59, 96], [70, 74], [29, 35], [98, 54], [24, 90], [17, 8],
                           [13, 66], [100, 95], [76, 87], [25, 81], [62, 66], [60, 20], [55, 67], [64, 27], [85, 14],
                           [11, 88], [27, 67], [94, 14], [60, 46], [98, 79], [46, 72], [92, 20], [42, 30], [18, 33],
                           [62, 41], [23, 13], [18, 41], [16, 69], [1, 25], [6, 43], [13, 11], [92, 37], [99, 24],
                           [20, 33], [35, 97], [23, 10], [40, 93], [96, 86], [44, 14], [95, 19], [85, 73], [2, 61],
                           [98, 67], [32, 46], [90, 72], [12, 76], [47, 93], [84, 80], [32, 78], [98, 88], [86, 53],
                           [21, 33], [23, 38], [45, 36], [68, 54], [20, 47], [36, 28], [90, 97], [45, 89], [15, 75],
                           [76, 78], [41, 89], [39, 90], [91, 49], [16, 44], [0, 24], [69, 98], [46, 1], [74, 35],
                           [75, 1], [30, 38], [35, 19], [99, 90], [78, 36], [99, 97], [66, 20], [87, 27], [10, 5],
                           [55, 92], [90, 86], [63, 10], [7, 50], [90, 41], [32, 36], [26, 2], [31, 76], [56, 36],
                           [98, 48], [100, 19], [72, 37], [20, 7], [12, 21], [51, 19], [17, 19], [27, 85], [9, 18],
                           [86, 56], [19, 89], [61, 44], [38, 21], [14, 21], [7, 92], [99, 22], [73, 33]],
                          321,
                          [5, 74]))
