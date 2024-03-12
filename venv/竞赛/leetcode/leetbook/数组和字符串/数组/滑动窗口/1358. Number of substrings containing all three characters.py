# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/24 8:08'

import time


class Solution:
    # 方法一:滑动窗口--窗口内符合条件,与右侧剩余字母组合.
    # 按长度统计子字符串数目
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cnt_a = 0
        cnt_b = 0
        cnt_c = 0

        res = 0
        L = 0
        for R in range(n):
            if s[R] == 'a':
                cnt_a += 1
            elif s[R] == 'b':
                cnt_b += 1
            else:
                cnt_c += 1

            while cnt_a >= 1 and cnt_b >= 1 and cnt_c >= 1:
                res += (n - R)  # 与右侧剩下的，可以组成合法的情况（R也是合理的）

                if s[L] == 'a':
                    cnt_a -= 1
                elif s[L] == 'b':
                    cnt_b -= 1
                else:
                    cnt_c -= 1
                L += 1
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
