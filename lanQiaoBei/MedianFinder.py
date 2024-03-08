# 295.数据流的中位数
# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
#
# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:
#
# MedianFinder() 初始化 MedianFinder 对象。
#
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
#
# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
#
# 示例 1：
#
# 输入
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# 输出
# [null, null, null, 1.5, null, 2.0]
#
# 解释
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
import heapq
# heapq 模块是小顶堆。实现 大顶堆 方法： 小顶堆的插入和弹出操作均将元素 取反 即可。

# 思路：设元素总数为 N=m+n，其中 m 和 n 分别为 A 和 B 中的元素个数。
# 1.当 m=n(即 N 为偶数):需向 A 添加一个元素。
# 实现方法:将新元素 num 插入至 B，再将 B 堆顶元素插入至 A 。
#
# 2.当 m≠n(即  为奇数):需向 B 添加一个元素。
# 实现方法:将新元素 num 插入至 A ，再将 A 堆顶元素插入至 B 。

# 假设插入数字 num 遇到情况 1.。由于 num 可能属于“较小的一半((即属于 B)，
# 因此不能将 nums 直接插入至 A 。而应先将 num 插入至 B ，再将 B 堆顶元素插入至 4 。
# 这样就可以始终保持 A 保存较大一半、 B 保存较小一半。)

# 当m=n(N为偶数):则中位数为(4的堆顶元素+B的堆顶元素 )/2。
# 当m≠n(N为奇数)则中位数为 4 的堆顶元素。


from heapq import *


class MedianFinder:

    def __init__(self):
        self.A = []  # 较大的一半  小根堆
        self.B = []  # 较小的一般  大根堆

    def addNum(self, num: int) -> None:
        if len(self.A) == len(self.B):
            heapq.heappush(self.A, -heapq.heappushpop(self.B, -num))
        else:
            heapq.heappush(self.B, -heapq.heappushpop(self.A, num))
    def findMedian(self) -> float:
        if len(self.A) == len(self.B):
            return (self.A[0] + (-self.B[0])) / 2
        else:
            return self.A[0]

s = MedianFinder()
s.addNum(1)
s.addNum(2)
print(s.findMedian())
s.addNum(3)
print(s.findMedian())