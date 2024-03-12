# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/23 9:00'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    m, n, s = map(int, input().split())
    ans = []
    string = []
    cur = -1
    for i in range(m):
        string.append(input())
    i = s - 1
    while i < len(string):
        if string[i] not in ans:
            ans.append(string[i])
            i += n
        else:
            i += 1
    if not ans:
        print("Keep going...")
    else:
        for each in ans:
            print(each)

    end = time.perf_counter()
    print(end - start)
