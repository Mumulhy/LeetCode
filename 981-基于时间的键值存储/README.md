# 981-基于时间的键值存储

Author：_Mumu

创建日期：2021/7/10

通过日期：2021/7/10

![](./通过截图2.jpg)

![](./通过截图1.jpg)

*****

踩过的坑：

1. 数据格式选了字典，感觉用key做键是比较合理的
2. 第一次蠢蠢地直接用晚的timestamp和value覆盖早的，然后才意识到get函数并不要求时间递增，还是必须存储所有的数据
3. 第二次用了嵌套的字典来存储，timestamp为键，value为值，然后蠢蠢地顺序查找，结果当然是超时
4. 看了题解才想到可以用二分法查找，于是最后才选定了双列表来分别存储timestamp和value
5. 艰辛(；′⌒`)

已解决：37/2153

*****

难度：中等

问题描述：

创建一个基于时间的键值存储类 TimeMap，它支持下面两个操作：

1. set(string key, string value, int timestamp)

存储键 key、值 value，以及给定的时间戳 timestamp。
2. get(string key, int timestamp)

返回先前调用 set(key, value, timestamp_prev) 所存储的值，其中 timestamp_prev <= timestamp。
如果有多个这样的值，则返回对应最大的  timestamp_prev 的那个值。
如果没有值，则返回空字符串（""）。


示例 1：

输入：inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
输出：[null,null,"bar","bar",null,"bar2","bar2"]
解释：  
TimeMap kv;   
kv.set("foo", "bar", 1); // 存储键 "foo" 和值 "bar" 以及时间戳 timestamp = 1   
kv.get("foo", 1);  // 输出 "bar"   
kv.get("foo", 3); // 输出 "bar" 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"）   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // 输出 "bar2"   
kv.get("foo", 5); // 输出 "bar2"   

示例 2：

输入：inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
输出：[null,null,null,"","high","high","low","low"]


提示：

所有的键/值字符串都是小写的。
所有的键/值字符串长度都在 [1, 100] 范围内。
所有 TimeMap.set 操作中的时间戳 timestamps 都是严格递增的。
1 <= timestamp <= 10^7
TimeMap.set 和 TimeMap.get 函数在每个测试用例中将（组合）调用总计 120000 次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/time-based-key-value-store