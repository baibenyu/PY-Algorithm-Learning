# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/15 15:30'

class Solution:
    # 方法一:利用栈先入后出的特性
    def isValid(self, s: str) -> bool:
        stack = []
        for each in s:
            if each == "(" or each == "[" or each == "{":
                stack.append(each)
            if stack:
                if each == ")":
                    if stack.pop() == "(":
                        continue
                    else:
                        return False
                if each == "]":
                    if stack.pop() == "[":
                        continue
                    else:
                        return False
                if each == "}":
                    if stack.pop() == "{":
                        continue
                    else:
                        return False
            else:
                return False
        if not stack:
            return True
        else:
            return False
