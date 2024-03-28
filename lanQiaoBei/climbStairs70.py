# 70.爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# 示例 1：
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
#
# 示例 2：
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶

# 1 <= n <= 45

# 思路：那么第一层楼梯再跨两步就到第三层 ，第二层楼梯再跨一步就到第三层。

# 下  标 | 1  2   3   4   5
# dp[i] | 1  2   3   5   8
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        dp[1], dp[2 if n > 1 else 0] = 1, 2 if n > 1 else 0

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        print(dp)
        return dp[n]


n = 2
s = Solution()
print(s.climbStairs(n))
