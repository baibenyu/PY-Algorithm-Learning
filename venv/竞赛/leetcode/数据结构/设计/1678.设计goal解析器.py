# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/28 14:40'

import time


class Solution:
    # 方法一:模拟
    def interpret(self, command: str) -> str:
        i = 0
        ans = ""
        while i < len(command):
            if command[i] == "G":
                ans += "G"
                i += 1
            else:
                if command[i + 1] == ")":
                    ans += "o"
                    i += 2
                else:
                    ans += "al"
                    i += 4
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
