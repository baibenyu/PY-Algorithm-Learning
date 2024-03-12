# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/24 8:38'
import collections
import time


class Solution:
    # 方法一:滑动窗口--先转化题目为找到p字符串中连续子串的种类有几个.
    # 以某个字母结尾的最长连续子串的长度,这个数字既是最长长度,也是包含的连续子串的数目
    def findSubstringInWraproundString(self, p: str) -> int:
        p = '^' + p
        len_mapper = collections.defaultdict(lambda: 0)
        w = 1
        for i in range(1, len(p)):
            if ord(p[i]) - ord(p[i - 1]) == 1 or ord(p[i]) - ord(p[i - 1]) == -25:
                w += 1
            else:
                w = 1
            len_mapper[p[i]] = max(len_mapper[p[i]], w)  # 取较大值,保证短的字符串的子串种类会被长字符串覆盖
        return sum(len_mapper.values())


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
