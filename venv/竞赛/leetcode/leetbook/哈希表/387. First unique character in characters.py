# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/26 21:01'
import collections
import time


class Solution:
    # 方法一:哈希表
    def firstUniqChar(self, s: str) -> int:
        stack = {}
        for i in range(len(s)):
            if s[i] not in stack:
                stack[s[i]] = i
            else:
                stack[s[i]] = float("inf")
        ans = min(stack.values())
        if ans != float("inf"):
            return ans
        else:
            return -1

    # 方法二:队列+哈希表
    def firstUniqChar2(self, s: str) -> int:
        position = dict()
        q = collections.deque()
        n = len(s)
        for i, ch in enumerate(s):
            if ch not in position:
                position[ch] = i
                q.append((s[i], i))
            else:
                position[ch] = -1
                while q and position[q[0][0]] == -1:  # 只要不干扰最终结果那么可以不删除,即只删除位于最开头的重复元素
                    q.popleft()
        return -1 if not q else q[0][1]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
