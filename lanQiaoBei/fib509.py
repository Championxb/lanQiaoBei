# 509.斐波那契数
# 斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。
# 该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
# 给定n ，请计算F(n) 。

# 示例1：
# 输入：n = 2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1
#
# 示例2：
# 输入：n = 3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2
#
# 示例3：
# 输入：n = 4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3

# 动态规划问题，五步曲:
# 1.确定dp数组（dp table）以及下标的含义
# 2.确定递推公式
# 3.dp数组如何初始化
# 4.确定遍历顺序
# 5.举例推导dp数组


class Solution:
    def fib(self, n: int) -> int:
        if n <=1:
            return n
        else:
            dp = [0 for _ in range(n + 1)]
            dp[0] = 0
            dp[1] = 1
            for i in range(2,n+1):
                dp[i]=(dp[i-1]+dp[i-2])
            print(dp)
        return dp[-1]

n = 0
s = Solution()
print(s.fib(n))
