# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/24 9:37'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    ans = ""
    for i in range(n):
        temp = input().split()
        for each in temp:
            if each[2] == "T":
                ans += str(ord(each[0]) - 64)
    print(ans)

    end = time.perf_counter()
    print(end - start)
