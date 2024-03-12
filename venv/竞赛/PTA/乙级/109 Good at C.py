# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/29 21:47'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    alpha = [[input() for j in range(7)] for i in range(26)]
    word = input()
    ci = ""
    cnt = 0
    vab = []

    for k in range(len(word)):
        # 要考虑最后以大写字母结尾，要注意不要少输出
        if 'A' <= word[k] <= 'Z' and k != len(word) - 1:
            ci += word[k]
        else:
            if 'A' <= word[k] <= 'Z':
                ci += word[k]
            if ci != '':
                vab.append(ci)
                cnt += 1
            ci = ""

    for k in range(cnt):
        for i in range(7):
            for j in range(len(vab[k])):
                print(alpha[(ord(vab[k][j]) - ord('A'))][i], end = "")
                if j != len(vab[k]) - 1:
                    print(" ", end = "")
            print()
        if k != cnt - 1:
            print()

    end = time.perf_counter()
    print(end - start)
