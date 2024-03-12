# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/7 11:05'

import time
from typing import List


class Solution:
    # 方法一:纵向模拟
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlength = float("inf")
        ans = []
        for each in strs:
            minlength = min(len(each), minlength)  # 避免越界
        for i in range(minlength):
            if all(strs[0][i] == each[i] for each in strs):
                ans.append(strs[0][i])
            else:
                break
        return "".join(ans)

    # 方法二:横向模拟
    # 假定一个前缀,逐步缩短
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        def lcp(str1, str2):
            length, index = min(len(str1), len(str2)), 0
            while index < length and str1[index] == str2[index]:
                index += 1
            return str1[:index]

        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    # 方法三:分治-方法二的进阶
    def longestCommonPrefix3(self, strs: List[str]) -> str:
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs) - 1)

    # 方法四:二分--每一次都将数组分为可能相同和不可能相同两分
    def longestCommonPrefix4(self, strs: List[str]) -> str:
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
