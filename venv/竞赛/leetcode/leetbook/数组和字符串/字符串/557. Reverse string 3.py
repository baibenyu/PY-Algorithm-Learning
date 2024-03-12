# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/24 8:56'

import time


class Solution:
    # 方法一:双指针,将原字符串按空格分割,然后逐个反转
    def reverseWords(self, s: str) -> str:
        string = s.split()
        ans = ""
        for index, each in enumerate(string):
            length = len(each)
            temp = list(each)
            for i in range(length // 2):
                temp[i], temp[length - i - 1] = temp[length - i - 1], temp[i]
            ans += "".join(temp)
            if index != len(string) - 1:
                ans += " "
        ans.rstrip()
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
