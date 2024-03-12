# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 15:47'

import time
from bisect import bisect


class ExamRoom(object):
    # 方法一:模拟
    def __init__(self, N):
        self.N = N
        self.students = []

    def seat(self):
        if not self.students:  # 空教室
            student = 0
        else:
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):  # 遍历两个人,取最大距离
                if i:
                    prev = self.students[i - 1]
                    d = (s - prev) // 2
                    if d > dist:
                        dist, student = d, prev + d

            d = self.N - 1 - self.students[-1]  # 只坐了一个人
            if d > dist:
                student = self.N - 1

        # Add the student to our sorted list of positions.
        bisect.insort(self.students, student)
        return student

    def leave(self, p):
        self.students.remove(p)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
