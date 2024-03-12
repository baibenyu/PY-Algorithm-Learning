# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/19 8:55'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    string = input()

    p, t = [0], [0]
    length = len(string)
    for i in range(length):
        if string[i] == "P":
            p.append(p[-1] + 1)
        else:
            p.append(p[-1])
        if string[length - i - 1] == "T":
            t.append(t[-1] + 1)
        else:
            t.append(t[-1])
    ans = 0
    for j in range(length):
        if string[j] == "A":
            ans += p[j] * t[length - j - 1]

    print(ans % 1000000007)

    end = time.perf_counter()
    print(end - start)
