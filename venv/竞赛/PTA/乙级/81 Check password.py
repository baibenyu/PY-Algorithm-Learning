# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/25 9:47'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    for i in range(n):
        pw = input()
        letter = 0
        digit = 0
        if len(pw) < 6:
            print("Your password is tai duan le.")
        else:
            for each in pw:
                if each.isdigit():
                    digit = 1
                elif each.isalpha():
                    letter = 1
                elif each == ".":
                    pass
                else:
                    print("Your password is tai luan le.")
                    break
            else:
                if digit and letter:
                    print("Your password is wan mei.")
                elif not digit:
                    print("Your password needs shu zi.")
                elif not letter:
                    print("Your password needs zi mu.")

    end = time.perf_counter()
    print(end - start)
