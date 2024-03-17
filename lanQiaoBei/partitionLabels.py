# 763.划分字母区间
# 给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
# 注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
# 返回一个表示每个字符串片段的长度的列表。


# 示例 1：
# 输入：s = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。

# 示例 2：
# 输入：s = "eccbbbbdec"
# 输出：[10]
from typing import List


# 思路：
# 1统计每一个字符最后出现的位置
# 2从头遍历字符，并更新字符的最远出现下标，如果找到字符最远出现位置下标和当前下标相等了，则找到了分割点
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}  # 存储每个字符最后出现的位置
        for i, str in enumerate(s):
            last_occurrence[str] = i  # 每个字母最后的位置
        print(last_occurrence)
        starPoint, endPoint =  0, 0
        res = []
        for i, str in enumerate(s):
            if last_occurrence[str] > endPoint:
                endPoint = last_occurrence[str]
            # 最远位置和下标相等
            if i == endPoint:
                res.append(endPoint - starPoint + 1)
                starPoint = endPoint + 1
        return res


s = "eccbbbbdec"
sol = Solution()
print(sol.partitionLabels(s))
