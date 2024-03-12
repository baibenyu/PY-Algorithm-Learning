# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/20 9:22'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    a, b = input().split()
    dict1 = [str(i) for i in range(10)] + ["J", "Q", "K"]
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    else:
        a = '0' * (len(b) - len(a)) + a
    a, b = list(a), list(b)
    a.reverse()
    b.reverse()
    i = 0
    ans = []

    while i < len(a) and i < len(b):
        if (i + 1) % 2:
            ans.append(dict1[(int(a[i]) + int(b[i])) % 13])
        else:
            temp = int(b[i]) - int(a[i])
            if temp < 0:
                temp += 10
            ans.append(dict1[temp])
        i += 1
    ans.reverse()
    print("".join(ans))

    end = time.perf_counter()
    print(end - start)
