# 20.有效的括号
#
# 给定一个只包括
# '('，')'，'{'，'}'，'['，']'
# 的字符串s ，判断字符串是否有效。
# 有效字符串需满足：左括号必须用相同类型的右括号闭合。左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。

# 示例
# 1：
#
# 输入：s = "()"
# 输出：true
# 示例
# 2：
#
# 输入：s = "()[]{}"
# 输出：true
# 示例
# 3：
#
# 输入：s = "(]"
# 输出：false

dict = {')': '(', '}': '{', ']': '['}

class validBracket:
    def isValid(self, str, dict):
        stuck = []
        lenth = len(str)    
        for i in range(lenth):
            if (str[i] in dict) and len(stuck) and dict[str[i]] == stuck[-1] :
                stuck.pop()
                continue
            stuck.append(str[i])
        return len(stuck)==0


s = ")"
solution = validBracket()
print(solution.isValid(s, dict))
