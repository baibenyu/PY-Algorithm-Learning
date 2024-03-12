# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/5 11:32'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    def dfs(start, index):
        global times, temp, cur
        if cur == n:
            times += 1
            if times % 4 == 0 or index == n-1:
                print(f"{n}=" + "".join(temp))
            else:
                print(f"{n}=" + "".join(temp), end = ";")
        else:
            for i in range(start, n + 1):
                if cur + i <= n:
                    cur += i
                    if index == n:
                        temp.append(f"{i}")
                    else:
                        temp.append(f"+{i}")
                    dfs(i, index - 1)
                    cur -= i
                    temp.pop()
                else:
                    break


    n = int(input())
    temp = []
    cur = 0
    times = 0
    dfs(1, n)

    end = time.perf_counter()
    print(end - start)
