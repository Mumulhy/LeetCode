# 707-设计链表

Author：_Mumu

创建日期：2019/10/3

通过日期：2019/10/3

![](https://github.com/Mumulhy/LeetCode/blob/master/141-环形链表/通过截图2.jpg)

![](https://github.com/Mumulhy/LeetCode/blob/master/141-环形链表/通过截图1.jpg)

*****

踩过的坑：

1. 若遍历链表并存储每个元，则会占用大量内存
2. 使用的方法其实是老师上课讲过的，自己写还真想不到这样的解法555

已解决：2/1189

*****

难度：简单

问题描述：

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：

输入：head = [3,2,0,-4], pos = 1

输出：true

解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0

输出：true

解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1

输出：false

解释：链表中没有环。


进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle