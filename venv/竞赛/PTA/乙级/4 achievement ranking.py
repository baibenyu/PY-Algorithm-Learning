# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/13 19:16'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    minnum = []
    maxnum = []
    for i in range(n):
        name, ID, grade = input().split()
        grade = int(grade)
        if not minnum:
            minnum.append((name, ID, grade))
            maxnum.append((name, ID, grade))
        else:
            if grade < minnum[0][2]:
                minnum[0] = (name, ID, grade)
            if grade > maxnum[0][2]:
                maxnum[0] = (name, ID, grade)
    print(maxnum[0][0], maxnum[0][1])
    print(minnum[0][0], minnum[0][1])

    end = time.perf_counter()
    print(end - start)
