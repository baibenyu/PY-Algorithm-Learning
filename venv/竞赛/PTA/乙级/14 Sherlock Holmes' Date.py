# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/14 15:20'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    a = input()
    b = input()
    c = input()
    d = input()
    i = 0
    day = []
    table = True
    while i < len(a) and i < len(b):
        if a[i] == b[i] and table:
            if 'A' <= a[i] <= 'G':  # 只在星期一到星期日
                day.append(ord(a[i]) - 65)
                table = False
                i = i + 1
        if a[i] == b[i] and not table:
            if 'A' <= a[i] <= 'N':  # 题目限制
                day.append(ord(a[i]) - 65 + 10)
                break
            elif '0' <= a[i] <= '9':
                day.append(ord(a[i]) - 48)
                break
        i = i + 1
    j = 0
    while j < len(c) and j < len(d):
        if c[j] == d[j] and c[j].isalpha():
            time = j
            break
        j = j + 1
    day1 = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    print(day1[day[0]], f"{day[1]:02}:{time:02}")

    end = time.perf_counter()
    print(end - start)
