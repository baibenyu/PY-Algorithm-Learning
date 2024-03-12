# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/4 10:14'

import time
from typing import List, Callable


class Solution:
    # 方法一:DP
    # dp表示以nums[i]结尾的最长递增序列长度,cnt表示以nums[i]结尾的最长递增序列的个数
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n, max_len, ans = len(nums), 0, 0
        dp = [0] * n
        cnt = [0] * n
        for i, x in enumerate(nums):
            dp[i] = 1
            cnt[i] = 1
            for j in range(i):
                if x > nums[j]:
                    if dp[j] + 1 > dp[i]:  # 当最长长度更新时,计数也要更新为前驱数据的数量
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]  # 重置计数
                    elif dp[j] + 1 == dp[i]:  # 后续遇到相等的长度就+1
                        cnt[i] += cnt[j]
            if dp[i] > max_len:  # 实时更新最长长度和个数,便于返回
                max_len = dp[i]
                ans = cnt[i]  # 重置计数
            elif dp[i] == max_len:
                ans += cnt[i]
        return ans


class Solution:
    # 方法二:贪心+二分+前缀和
    # 搞不懂!!!
    # d[i] 数组表示所有能成为长度为 i 的最长上升子序列的末尾元素的值。具体地，我们将更新 d[i]=nums[j] 这一操作替换成将
    # nums[j] 置于 d[i] 数组末尾。这样 d[i] 中就保留了历史信息，且 d[i] 中的元素是有序的（单调非增）

    def findNumberOfLIS(self, nums: List[int]) -> int:
        def bisect(n: int, f: Callable[[int], bool]) -> int:
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if f(mid):
                    r = mid
                else:
                    l = mid + 1
            return l

        d, cnt = [], []
        for v in nums:
            i = bisect(len(d), lambda i: d[i][-1] >= v)
            c = 1  # 至少长度为1
            if i > 0:
                k = bisect(len(d[i - 1]), lambda k: d[i - 1][k] < v)  # 判断在序列中的具体位置
                c = cnt[i - 1][-1] - cnt[i - 1][k]

            if i == len(d):  # 若无大于当前值则新建
                d.append([v])
                cnt.append([0, c])
            else:  # 否则在原有基础上增加
                d[i].append(v)
                cnt[i].append(cnt[i][-1] + c)
        return cnt[-1][-1]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
