# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/18 16:18'

import time


class Solution:
    # 方法一:重构字符串后再比较
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack, t_stack = [], []
        for each in s:
            if each == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(each)
        for each in t:
            if each == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(each)
        if s_stack == t_stack:
            return True
        else:
            return False

    # 方法二:双指针+计数器
    # 遇到#就说明前面的非#字符应该被删除,所以无需比较
    def backspaceCompare2(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1

        return True


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
