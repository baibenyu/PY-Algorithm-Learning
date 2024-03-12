# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/25 9:08'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    def IsPalindrome(string, length):
        for i in range(length // 2):
            if string[i] != string[length - i - 1]:
                return False
        return True


    a = input()
    i = 0
    while i < 10:
        if IsPalindrome(a, len(a)):
            print(f"{a} is a palindromic number.")
            break
        else:
            b = int("".join(reversed(a)))
            a = int(a)
            print(f"{a} + {b} = {a + b}")
            a = str(a + b)
        i += 1
    else:
        print("Not found in 10 iterations.")

    end = time.perf_counter()
    print(end - start)
