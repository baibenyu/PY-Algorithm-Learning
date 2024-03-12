# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/26 9:25'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    dict1 = dict()
    for i in range(n):
        ID, score, school = input().split()
        school = school.lower()
        if ID[0] == "B":
            score = int(score) / 1.5
        elif ID[0] == "A":
            score = int(score)
        else:
            score = int(score) * 1.5
        if school not in dict1:
            dict1[school] = [score, 1]
        else:
            dict1[school][0] += score
            dict1[school][1] += 1
    ans = []
    for key, value in dict1.items():
        ans.append([key, int(value[0]), value[1]])
    ans.sort(key = lambda x: (x[2], x[0]))
    ans.sort(reverse = True, key = lambda x: x[1])
    print(len(ans))
    j = 0
    k = 1
    while j < len(ans):
        print(f"{j + 1}", ans[j][0], ans[j][1], ans[j][2])
        while j + k < len(ans) and ans[j][1] == ans[j + k][1]:
            print(f"{j + 1}", ans[j + k][0], ans[j + k][1], ans[j + k][2])
            k += 1
        j += k
        k = 1

    end = time.perf_counter()
    print(end - start)
