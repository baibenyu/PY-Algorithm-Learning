# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/14 19:46'

import time


class Solution:
    # 方法一:语言API
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    # 方法二:KMP算法
    # 利用遍历过程中前缀和后缀的最长相等字符串,排除了原前缀其它字符起始位置的可能性,同时省略了比较后缀是否与前缀相等(在getnextarr中已经证明相等)
    def strStr2(self, haystack: str, needle: str) -> int:
        def getnextarr(str2):
            if len(str2) == 1:
                return [-1]
            else:
                nextarr = [0 for _ in range(len(str2))]  # 存储前一位的最长前缀后缀相等长度
                nextarr[0] = -1
                nextarr[1] = 0
                i = 2  # 当前位置
                cur = 0  # 既是可能的最长长度,也表示前一个nextarr数据的后缀起始位置
                while i < len(nextarr):
                    if str2[i - 1] == str2[cur]:
                        cur += 1
                        nextarr[i] = cur
                        i += 1
                    elif cur > 0:
                        cur = nextarr[cur]
                    else:
                        nextarr[i] = 0
                        i += 1
            return nextarr

        if haystack is None or needle is None or len(needle) < 1 or len(haystack) < len(needle):
            return -1
        x, y = 0, 0  # x表示长字符串的可能起始位置,y表示短字符串的可能起始位置
        nextarr = getnextarr(needle)
        while x < len(haystack) and y < len(needle):
            if haystack[x] == needle[y]:
                x += 1
                y += 1
            elif nextarr[y] == -1:
                x += 1
            else:
                y = nextarr[y]
        return x - y if y == len(needle) else -1


if __name__ == '__main__':
    start = time.clock()
    s = Solution()
    s.strStr2("asas")
    end = time.clock()
    print(end - start)
