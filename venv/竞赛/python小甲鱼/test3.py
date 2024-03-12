from collections import deque
from timeit import timeit


def dbl_linear1(n):
    h = 1
    cnt = 0
    q2, q3 = deque([]), deque([])
    while True:
        if cnt >= n:
            return h
        q2.append(2 * h + 1)
        q3.append(3 * h + 1)
        h = min(q2[0], q3[0])
        if h == q2[0]: h = q2.popleft()
        if h == q3[0]: h = q3.popleft()
        cnt += 1


a = dbl_linear1(10)
print(a)
# t = timeit("dlb_linear(100000)", 'from __main__ import dlb_linear', number = 1)
# print(t)
