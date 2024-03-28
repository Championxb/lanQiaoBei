# 62.不同路径
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 问总共有多少条不同的路径？

# 示例 1：
# |_S_|___|___|___|___|___|___|
# |___|___|___|___|___|___|___|
# |___|___|___|___|___|___|_F_|
# 输入：m = 3, n = 7
# 输出：28

# 示例 2：
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下

# 思路：可抽象的理解为二叉树，因为下一步始终面临连个选择1向左 2向下
# 此时问题就可以转化为求二叉树叶子节点的个数，
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 推导公式：dp[i][j]=dp[i][j-1] + dp[i-1][j],
        # dp[i][j]表示从（0 ，0）出发，到(i, j) 有dp[i][j]条不同的路径。
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # dp[i][0]和dp[0][j]一定都是1，因为只能走直线
        dp[0] = [1] * n  # 第一行
        for row in dp:
            row[0] = 1  # 第一列

        for i in range(1, m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]


m = 3
n = 7
s = Solution()
print(s.uniquePaths(m, n))
