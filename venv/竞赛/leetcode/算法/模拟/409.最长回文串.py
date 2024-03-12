# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/19 16:47'

import time


class Solution:
    # 方法一:模拟
    # 偶数直接用,奇数只能取数量最大的用,其它奇数个都只能取数量-1
    def longestPalindrome(self, s: str) -> int:
        import collections
        c = collections.Counter(s)
        ans = 0
        odd = 1
        flag = False
        for each in c:
            if c[each] % 2 == 0:
                ans += c[each]
            else:
                flag = True
                if c[each] > odd:
                    ans += odd - 1
                    odd = c[each]
                else:
                    ans += c[each] - 1
        return ans + odd if flag else ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
