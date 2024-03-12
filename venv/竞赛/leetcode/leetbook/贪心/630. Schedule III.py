# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/13 9:13'
import heapq
import time
from typing import List


class Solution:
    # 方法一:贪心--优先学习结束时间早的课程,如果当前时间超出结束时间,尝试更换之前安排的学习项目为时间更短结束时间更晚的课程
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda c: c[1])

        q = list()
        # 优先队列中所有课程的总时间
        total = 0

        for ti, di in courses:
            if total + ti <= di:
                total += ti
                # Python 默认是小根堆
                heapq.heappush(q, -ti)
            elif q and -q[0] > ti:
                total -= -q[0] - ti
                heapq.heappop(q)
                heapq.heappush(q, -ti)

        return len(q)


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
