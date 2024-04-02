# 131.分割回文串
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例: 输入: "aab" 输出: [ ["aa","b"], ["a","a","b"] ]

from typing import List


class Solution:
    def __init__(self):
        self.result= []
        self.part = []
        self.startIndex = 0
    def partition(self, s: str) -> List[List[str]]:
        self.backtracking(s,self.startIndex)
        return self.result

    def backtracking(self,s,startIndex):
        # if sum(len(x) for x in self.part) == len(s):
        #     self.result.append(self.part[:])
        #     return
        if startIndex >= len(s):  # 如果起始位置已经大于s的大小，说明已经找到了一组分割方案了
            self.result.append(self.part[:])
            return
        for i in range(startIndex,len(s)):
            if s[startIndex:i+1] == s[startIndex:i+1][::-1]:
                # print(s[startIndex:i+1])
                self.part.append(s[startIndex:i+1])
                self.backtracking(s,i+1)
                self.part.pop()

string="aab"
s= Solution()
print(s.partition(string))