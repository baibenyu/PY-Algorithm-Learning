# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/13 19:27'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    nums = list(map(int, input().split()))
    visited = set()
    for each in nums:
        if each not in visited:
            while each != 1:
                if each % 2:
                    each = (3 * each + 1) // 2
                else:
                    each /= 2
                visited.add(each)

    ans = []
    for each in nums:
        if each not in visited:
            ans.append(each)

    ans.sort(reverse = True)
    for each in ans:
        if each == ans[-1]:
            print(each)
        else:
            print(each, end = " ")

    end = time.perf_counter()
    print(end - start)
