# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/15 9:14'

import time


# kmp算法
# 利用遍历过程中前缀和后缀的最长相等字符串,
# [1]排除了原前缀其它字符起始位置的可能性,因为nextarr中的前后缀匹配长度已经是最长的,若可能存在则会导致产生更长的前后缀匹配长度,与原命题条件不符合,所以可以排除
# [2]省略了比较后缀是否与前缀相等(在getnextarr中已经证明相等)
def strStr2(self, haystack: str, needle: str) -> int:
    def getnextarr(str2):
        if len(str2) == 1:
            return [-1]
        else:
            nextarr = [0 for _ in range(len(str2))]  # 存储前一个下标的最长前缀后缀相等长度
            nextarr[0] = -1  # 下标0的前一个是空,规定是-1
            nextarr[1] = 0   # 下标1的前一个只有一个字符串,前后缀都不包含本身,所以为0
            i = 2  # 当前位置
            cur = 0  # 既是前后缀的最大匹配长度,也表示下一次比较的起始位置
            while i < len(nextarr):
                if str2[i - 1] == str2[cur]:
                    cur += 1
                    nextarr[i] = cur
                    i += 1
                elif cur > 0:  # 逐步缩小前后缀匹配长度
                    cur = nextarr[cur]
                else:
                    nextarr[i] = 0  # 无匹配
                    i += 1
        return nextarr

    if haystack is None or needle is None or len(needle) < 1 or len(haystack) < len(needle):
        return -1
    x, y = 0, 0  # x表示目标串的起始位置,y表示模式串的起始位置
    nextarr = getnextarr(needle)
    while x < len(haystack) and y < len(needle):
        if haystack[x] == needle[y]:
            x += 1
            y += 1
        elif nextarr[y] == -1:  # 回到开头说明无论如何都匹配不了,此时目标串的字符无法在模式串中找到,所以直接越过
            x += 1
        else:
            y = nextarr[y]
    return x - y if y == len(needle) else -1


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
