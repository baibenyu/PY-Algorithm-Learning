# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/23 9:30'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    T, K = map(int, input().split())
    for i in range(K):
        n1, b, t, n2 = map(int, input().split())
        if t > T:
            print(f"Not enough tokens.  Total = {T}.")
        else:
            if n2 < n1 and b == 0 or n2 > n1 and b == 1:
                T += t
                print(f"Win {t}!  Total = {T}.")
            else:
                T -= t
                print(f"Lose {t}.  Total = {T}.")
        if T <= 0:
            print("Game Over.")
            break

    end = time.perf_counter()
    print(end - start)
