# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/19 9:19'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    string = input().lower()
    ans = [0 for i in range(26)]

    for each in string:
        if "a" <= each <= "z":
            ans[ord(each) - 97] += 1

    print(chr(97 + ans.index(max(ans))), max(ans))

    end = time.perf_counter()
    print(end - start)
