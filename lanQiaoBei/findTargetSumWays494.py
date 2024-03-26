# 494.目标和
# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
# 对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

# 示例：
# 输入：nums: [1, 1, 1, 1, 1], S: 3
# 输出：5
# 解释：
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 一共有5种方法让最终目标和为3。

# 提示：
# 数组非空，且长度不会超过 20 。
# 初始的数组的和不会超过 1000 。
# 保证返回的最终结果能被 32 位整数存下。
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if sum(nums) <abs(target): return 0

        # 假设加法的总和为x，那么减法对应的总和就是sum - x。
        # 所以我们要求的是:  x - (sum - x) = target
        if (sum(nums) + target) % 2 != 0 or sum(nums) < target:
            return 0
        dpTarget = int((sum(nums) + target) / 2)

        dp = [0] * (dpTarget + 1)
        dp[0] = 1

        # dp[j]表示：填满j（包括j）这么大容积的包，有dp[j]种方法

        # 例如：dp[j]，j为5，
        # 已经有一个1的话，有dp[4]种方凑成容量为5的背包。
        # 已经有一个2的话，有dp[3]种方法凑成容量为5的背包。
        # 已经有一个3的话，有dp[2]中方法凑成容量为5的背包
        # 已经有一个4的话，有dp[1]中方法凑成容量为5的背包
        # 已经有一个5的话，有dp[0]中方法凑成容量为5的背包
        # 那么凑整dp[5]的方法呢，也就是把所有的dp[j - nums[i]]累加起来。

        # 所以求组合类问题的公式，都是类似这种：
        # dp[j] += dp[j - nums[i]]
        print(dp)
        for i in range(0, len(nums)):  # 物品
            for j in range(dpTarget, nums[i] - 1, -1):  # 背包
                dp[j] += dp[j - nums[i]]
            print(dp)

        # 创建二维动态规划数组，行表示选取的元素数量，列表示累加和
        dp = [[0] * (dpTarget + 1) for _ in range(len(nums) + 1)]

        # 初始化状态
        dp[0][0] = 1

        # 动态规划过程
        # i = 0 时为没有物品，所以 i-1 才是当前物品
        for i in range(1, len(nums) + 1):
            for j in range(dpTarget + 1):
                dp[i][j] = dp[i - 1][j]  # 先不加入当前元素
                if j >= nums[i - 1]:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]  # 选取当前元素，nums[i - 1]就是当前元素，因为i= 0 时初始化只有0元素情况的一行
        return dp


nums = [1, 1, 1, 1, 1]
target = 3
s = Solution()
print(s.findTargetSumWays(nums, target))
