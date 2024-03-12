# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/16 9:07'

class Solution:
    # 方法一:利用辅助栈实现字符串的由内向外解构
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])  # 存储未处理的数字与字符串
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res

    def decodeString2(self, s: str) -> str:
        stack = []
        num = 0
        string = ""  # 单个括号内对应的字符串
        for each in s:
            if each.isdigit():
                num = num * 10 + int(each)  # 数字可能大于10
            elif each == "[":  # 当遇到左括号说明数字部分结束
                stack.append(num)  # 将相应数字入栈
                stack.append(each)
                num = 0
            elif each.isalpha():
                stack.append(each)
            elif each == "]":  # 遇到右括号时开始解码字符串
                while True:
                    top = stack.pop()  # 持续弹出栈顶元素直至遇到数字
                    if type(top) == int:  # 遇到数字说明一对括号结束
                        stack.append(string * top)
                        string = ""  # 将当前右括号对应解码后的字符串入栈
                        break
                    if top != "[":  # 确定单个括号内字符串
                        string = top + string
        return "".join(stack[::-1])


s = Solution()
print(s.decodeString("3[a2[bc]]"))
