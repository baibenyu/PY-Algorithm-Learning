# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/7 15:17'

import time
import bisect
from collections import defaultdict
from typing import List


class Solution:
    # 方法一:DP
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # 预处理左边最近和右边最近三个颜色分别所在的位置
        n = len(colors)
        # 从左向右预处理
        site = [float('-inf'), float('-inf'), float('-inf')]  # 存储离当前下标最近的1,2,3颜色的下标
        left_dis = [[0 for _ in range(n)] for _ in range(3)]
        for i in range(n):  # [i][j]表示离j下标对应的1-3颜色的从左往右的最短距离
            site[colors[i] - 1] = i
            for j in range(3):
                left_dis[j][i] = i - site[j]  # 从左往右,说明颜色值对应的下标小于等于当前下标

        # 从右向左预处理
        site = [float('inf'), float('inf'), float('inf')]  # 同理
        right_dis = [[0 for _ in range(n)] for _ in range(3)]
        for i in range(n - 1, -1, -1):  # 同理,反向
            site[colors[i] - 1] = i
            for j in range(3):
                right_dis[j][i] = site[j] - i  # 同理,反向

        ans = []
        for i, c in queries:
            min_dis = min(left_dis[c - 1][i], right_dis[c - 1][i])
            if min_dis == float('inf'):
                ans.append(-1)
            else:
                ans.append(min_dis)
        return ans

    # 方法二:二分查找+哈希表
    def shortestDistanceColor2(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        color_idxs = defaultdict(list)
        for i, c in enumerate(colors):  # 统计各颜色对应的下标集合
            color_idxs[c].append(i)
        res = []
        for i, c in queries:
            if c not in color_idxs:  # 这个颜色不存在
                res.append(-1)
            elif colors[i] == c:  # 就是自己
                res.append(0)
            else:
                a = color_idxs[c]
                r = bisect.bisect_left(a, i)  # 利用二分缩短查找时间
                if r == 0:
                    res.append(a[0] - i)
                elif r == len(a):
                    res.append(i - a[-1])
                else:
                    res.append(min(a[r] - i, i - a[r - 1]))
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
