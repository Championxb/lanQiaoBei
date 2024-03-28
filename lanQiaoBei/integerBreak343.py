# 343.整数拆分
# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
# 返回 你可以获得的最大乘积 。

# 示例 1:
# 输入: n = 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
#
# 示例 2:
# 输入: n = 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 提示:
#
# 2 <= n <= 58


# 思路：
# dp[i]：分拆数字i，可以得到的最大乘积为dp[i]。因为n是大于等于2的,所以初始的下表从2开始
# 而dp[i]的最大乘积是通过  (i-j)*j ----(即拆成两部分）和dp[i-j]*j -----即拆分成两个以及两个以上的个数相乘
# 所以递推公式为：dp[i] = max({dp[i], (i - j) * j, dp[i - j] * j});
# 在每次的计算过程可能会改变d[i],所以最终的公式为：
# dp[i] = max(dp[i],max(dp[i], (i - j) * j, dp[i - j] * j))


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        # 从下标2开始初始化 ，因为n>=2
        dp[2] = 1
        for i in range(3,n+1):
             for j in range(1,i//2+1):
                 dp[i] = max(dp[i],max((i-j)*j,dp[i-j]*j))
        print(dp)
        return dp[n]

n = 10
s= Solution()
print(s.integerBreak(n))