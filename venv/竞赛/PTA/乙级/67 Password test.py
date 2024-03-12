# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/22 15:20'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    password, count = input().split()
    count = int(count)
    flag = 0
    while count > 0:
        temp = input()
        if temp == "#":
            break
        elif temp != password:
            print(f"Wrong password: {temp}")
            count -= 1
        else:
            flag = 1
            print("Welcome in")
            break
    if not flag and count == 0:
        print("Account locked")

    end = time.perf_counter()
    print(end - start)
