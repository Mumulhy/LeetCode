# 21-合并两个有序链表

Author：_Mumu

创建日期：2019/10/4

通过日期：2019/10/4

![](https://github.com/Mumulhy/LeetCode/blob/master/21-合并两个有序链表/通过截图2.jpg)

![](https://github.com/Mumulhy/LeetCode/blob/master/21-合并两个有序链表/通过截图1.jpg)

*****

踩过的坑：

1. 没啥坑吧，一次就过辽，开心o(*￣▽￣*)ブ
2. 不过这个算法的瑕疵在于改变了原链表的连接了，想要不改变的话需要在比较大小后创建新的节点接在结果链表后，但是其实这样思路更单纯，更好写

已解决：5/1189

*****

难度：简单

问题描述：

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4

输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists