# 1037-有效的回旋镖

Author：_Mumu

创建日期：2022/06/08

通过日期：2022/06/08

![](./通过截图2.jpg)

![](./通过截图1.jpg)

*****

踩过的坑：

1. 轻松愉快

已解决：364/2662

*****

难度：简单

问题描述：

给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，如果这些点构成一个 回旋镖 则返回 true 。

回旋镖 定义为一组三个点，这些点 各不相同 且 不在一条直线上 。

 

示例 1：

输入：points = [[1,1],[2,3],[3,2]]
输出：true
示例 2：

输入：points = [[1,1],[2,2],[3,3]]
输出：false


提示：

points.length == 3
points[i].length == 2
0 <= xi, yi <= 100

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-boomerang