# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/15 20:56'
from typing import List


class Solution:
    # 方法一:单调栈的运用,先将元素的索引(天数)入栈,当遇到大于栈顶的元素时出栈(即单调递减栈),并将当前索引值减去栈顶元素索引值,即所求间隔的天数
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        answer = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                pre = stack.pop()
                answer[pre] = i - pre
            stack.append(i)
        return answer

    # 方法二:枚举
    # nxt存储每个温度第一次出现的下标
    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans, nxt, big = [0] * n, dict(), 10 ** 9
        for i in range(n - 1, -1, -1):  # 逆序保证正确
            warmer_index = min(nxt.get(t, big) for t in range(temperatures[i] + 1, 102))  # 找到比当前天数温度高的最小下标
            if warmer_index != big:
                ans[i] = warmer_index - i
            nxt[temperatures[i]] = i
        return ans
