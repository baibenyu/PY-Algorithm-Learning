# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/29 20:54'

import time


class Solution:
    def freqAlphabets(self, s: str) -> str:
        def get(st):
            return chr(int(st) + 96)

        i, ans = 0, ""
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                ans += get(s[i: i + 2])
                i += 2
            else:
                ans += get(s[i])
            i += 1
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
