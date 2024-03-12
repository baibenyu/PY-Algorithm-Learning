# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/9 20:28'

import time
from collections import defaultdict


class Solution:
    # 方法一:滑动窗口
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Step 1:
        # 定义需要维护的变量, 本题求最大长度，所以需要定义max_len,
        # 该题又涉及计算不重复元素格式，因此还需要一个哈希表
        max_len, hashmap = 0, {}

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(s)):
            # Step 3
            # 首先，把当前元素的计数加一
            # 一旦哈希表长度小于等于2(之多包含2个不同元素)，尝试更新最大长度
            tail = s[end]
            hashmap[tail] = hashmap.get(tail, 0) + 1
            if len(hashmap) <= 2:
                max_len = max(max_len, end - start + 1)

            # Step 4:
            # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 哈希表长度大于2的时候 (说明存在至少3个重复元素)，窗口不合法
            # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashmap)
            while len(hashmap) > 2:
                head = s[start]
                hashmap[head] -= 1
                if hashmap[head] == 0:
                    del hashmap[head]
                start += 1
        return max_len


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
