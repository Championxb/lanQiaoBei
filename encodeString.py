# 394. 字符串解码
# 给定一个经过编码的字符串，返回它解码后的字符串。编码规则为: k[encoded_string]，
# 表示其中方括号内部的encoded_string正好重复k次。注意k保证为正整数。
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数
# k ，例如不会出现像3a或2[4]的输入。
#
# 示例
# 1：
#
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
# 示例
# 2：
#
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
# 示例
# 3：
#
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
# 示例
# 4：
#
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"

s = "2[abc]3[cd]ef"
stuck = [1, 2, 3]
s = ["c", "d"]
# print(stuck.pop() * s.pop())

dict = {']': '['}


class Encode:
    def decodeString(self, s):
        res, stack, mult = "", [], 0
        for str in s:
            if str.isdigit():
                mult = 10*mult + int(str)
            if str.isalpha():
                res += str
            if str == '[':
                stack.append([res, mult])
                res, mult = "", 0
            if str == ']':
                temp_res, temp_mult = stack.pop()
                res = temp_res + res*temp_mult
        return res
        # encoded = ""
        # strTemp = ""
        # number = []
        # str = []
        # lenth = len(s)
        #
        # i = 0
        # flag = 0
        # while i < lenth:
        #     if s[i].isdigit():
        #         number.append(s[i])
        #
        #     if s[i] == '[':
        #         str.append(s[i])
        #         for j in range(i + 1, lenth):
        #             if s[j].isalpha():
        #                 strTemp = strTemp + s[j]
        #             if s[j] == ']' or s[j].isdigit():
        #                 if s[j].isdigit():
        #                     number.append(s[j])
        #                 i = j
        #                 str.append(strTemp)
        #                 strTemp = ''
        #                 break
        #
        #     if s[i] == ']':
        #         encoded = int(number.pop()) * str.pop() if flag > 1 else encoded + int(number.pop()) * str.pop()
        #         str.pop()
        #         flag += 1
        #         if str and str[-1].isalpha():
        #             str.append(str.pop() + encoded)
        #
        #     i = i + 1
        # return encoded


solution = Encode()
print(solution.decodeString("2[abc]3[cd]ef"))
# 3[a2[c]] 3[a]2[bc]
