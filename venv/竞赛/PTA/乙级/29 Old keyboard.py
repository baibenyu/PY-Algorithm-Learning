# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/17 15:18'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    should = input().upper()
    now = input().upper()
    ans = list()

    i, j = 0, 0
    while i < len(should) and j < len(now):
        while should[i] != now[j]:
            if should[i] not in ans:
                ans.append(should[i])
            i += 1

        i += 1
        j += 1

    while i < len(should):
        if should[i] not in ans:
            ans.append(should[i])
        i += 1

    for each in ans:
        print(each, end = "")

    end = time.perf_counter()
    print(end - start)
