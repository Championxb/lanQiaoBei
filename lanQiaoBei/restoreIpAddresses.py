# 93.复原IP地址
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
#
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。
#
# 示例 1：
#
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 示例 2：
#
# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 示例 3：
#
# 输入：s = "1111"
# 输出：["1.1.1.1"]
# 示例 4：
#
# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]

from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.ipStr = []
        self.startIndex = 0

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.backtracking(s, self.startIndex)
        return self.result

    def backtracking(self, s, startIndex):
        if self.ipStr:
            if len(self.ipStr[-1]) >= 2 and self.ipStr[-1][0] == '0':
                # print(self.ipStr[-1], self.ipStr)
                return
            if int(self.ipStr[-1])>255:
                # print(self.ipStr[-1], self.ipStr)
                return
        if startIndex<len(s) and len(self.ipStr) >= 4:  # 剪枝 还没遍历到末尾 ip长度就已经大于四段了
            return
        if startIndex >= len(s):
            if len(self.ipStr) == 4:
                # print(self.ipStr)
                self.result.append('.'.join(self.ipStr))
                return
            return


        for i in range(startIndex, len(s)):
            # if int(s[startIndex:i + 1]) <= 255:
            self.ipStr.append(s[startIndex:i + 1])
            self.backtracking(s, i + 1)
            self.ipStr.pop()


s = "101023"
res = Solution()

print(res.restoreIpAddresses(s))
