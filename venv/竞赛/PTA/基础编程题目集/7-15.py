# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/3 9:38'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    limit = float(input())
    ans = 1 + 1 / 3
    up, down = 1, 3
    step = 1
    t_up, t_down = up, down
    while t_up / t_down >= limit:
        t_up = t_up * (up + step)
        t_down = t_down * (down + step * 2)
        ans += t_up / t_down
        step += 1

    print(f"{ans * 2:.6f}")

    end = time.perf_counter()
    print(end - start)
