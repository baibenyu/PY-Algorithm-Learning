# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/22 15:30'

import time


class Solution:
    # 方法一:双指针
    # 用target的子串去匹配source的子序列,若能找到则i的值改变
    def shortestWay(self, source: str, target: str) -> int:
        res = i = 0
        while i < len(target):
            j = 0
            pre = i
            while i < len(target) and j < len(source):
                if target[i] == source[j]:
                    i += 1
                j += 1
            if pre == i:
                return -1
            res += 1
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
