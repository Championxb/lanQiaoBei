# 77.组合
# 给定两个整数 n 和 k，返回 [1 , n] 中所有可能的 k 个数的组合。
# 你可以按顺序返回答案
# 示例: 输入: n = 4, k = 2
# 输出: [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]
# 示例 2：
#
# 输入：n = 1, k = 1
# 输出：[[1]]
from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.path = []
        self.startIndex = 1

    def combine(self, n: int, k: int) -> List[List[int]]:

        # 暴力解法
        # for i in range(1,n+1):
        #     for j in range(i+1,n+1):
        #         print( i, j)

        # path = []
        # result = []
        self.backtracking(n, k, self.startIndex, self.path, self.result)
        return self.result

    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n-(k-len(path))+2):
            path.append(i)  # 添加节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤回添加的节点


n = 4
k = 2
s = Solution()
print(s.combine(n, k))

