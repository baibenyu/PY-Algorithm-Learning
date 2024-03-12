# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/26 21:14'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    a, b = input(), input()
    ans = []
    for each in a:
        if each not in ans:
            ans.append(each)
    for each in b:
        if each not in ans:
            ans.append(each)
    print("".join(ans))

    end = time.perf_counter()
    print(end - start)
