# 973-最接近原点的K个点

Author：_Mumu

创建日期：2021/2/20

通过日期：2021/2/20

![](./通过截图2.jpg)

![](./通过截图1.jpg)

*****

踩过的坑：

1. 第一反应，sort搞定
2. 然后发现出错，因为把^当成了幂运算，python的幂是**，^是异或
3. 自己写的时候多建了列表导致占用内存变大，直接用lambda函数原位sort更舒适
4. 不必考虑开根号，因为开不开是等效的，开还要浪费时间，还可能产生误差
5. 题解中提到了神奇的大根堆（python中为小根堆）

已解决：11/1973

*****

难度：中等

问题描述：

我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。



示例 1：

输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释： 
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
示例 2：

输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）


提示：

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-closest-points-to-origin