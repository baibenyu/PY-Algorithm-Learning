# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/25 8:50'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    modern = input()
    string = input()
    ans = []
    i = 0
    if modern == "C":
        while i < len(string):
            j = 0
            while i + j < len(string) and string[i] == string[i + j]:
                j += 1
            ans.append(str(j) if j != 1 else "")
            ans.append(string[i])
            i += j
        print("".join(ans))
    else:
        while i < len(string):
            j = 0
            while i + j < len(string) and string[i + j].isdigit():
                j += 1
            ans.append(int(string[i:i + j]) * string[i + j] if j != 0 else string[i + j])
            i += j + 1
        print("".join(ans))

    end = time.perf_counter()
    print(end - start)
