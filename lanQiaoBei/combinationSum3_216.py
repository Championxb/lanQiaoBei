# 216.组合总和III
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 说明：
# 所有数字都是正整数。
# 解集不能包含重复的组合。

# 示例 1: 输入: k = 3, n = 7 输出: [[1,2,4]]
# 示例 2: 输入: k = 3, n = 9 输出: [[1,2,6], [1,3,5], [2,3,4]]
from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.path = []
        self.startIndex = 1

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtracking(k, n, self.startIndex, self.result, self.path)
        return self.result

    def backtracking(self, k, n, startIndex, result, path):
        if sum(path) > n:return 
        if sum(path) == n and len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, 9-(k-len(path))+2):
            path.append(i)
            self.backtracking(k, n, i + 1, result, path)
            path.pop()


k = 9
n = 45
s=Solution()
print(s.combinationSum3(k,n))
