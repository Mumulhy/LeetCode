# 剑指 Offer 42-连续子数组的最大和

Author：_Mumu

创建日期：2021/7/17

通过日期：2021/7/17

![](https://github.com/Mumulhy/LeetCode/blob/master/剑指 Offer 42-连续子数组的最大和/通过截图2.jpg)

![](https://github.com/Mumulhy/LeetCode/blob/master/剑指 Offer 42-连续子数组的最大和/通过截图1.jpg)

*****

踩过的坑：

1. 就很难受，一开始想写动态规划，然后死活想不出来怎么写
2. 然后想用最大前缀和减去最小前缀和，然后发现下标问题死活不知道怎么处理
3. 题解第一遍还没看懂（其实是累了没仔细看
4. 思路就是依次计算以第$i$个数为右端点的子数组最大和$f(i)$，就能找到整个数组$\{a_i\}_0^{n-1}$的子数组最大和
5. 假设已知$f(i-1)$，因为$f(i)$必须含有$a_i$，那么$f(i)$要么为$f(i-1)+a_i$，要么为$a_i$
   因此递推公式为：$f(i)=\left\{\begin{array}{lr}f(i-1)+a_i & f(i-1)>0\\a_i & otherwise \end{array}\right.$
   代码可写为`f[i] = max(f[i-1]+a[i], a[i])`
6. 同时每次递推就更新一次最大值，就不需要额外空间存储$f(i)$数组

已解决：44/2159

*****

难度：简单

问题描述：

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof