# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/27 19:44'
import math
import time

if __name__ == '__main__':
    start = time.perf_counter()

    def isprime(n):
        if n > 1:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        else:
            return False

    n = int(input())
    if isprime(n) and isprime(n - 6):
        print("Yes")
        print(n - 6)
    elif isprime(n) and isprime(n + 6):
        print("Yes")
        print(n + 6)
    else:
        print("No")
        while True:
            n += 1
            if isprime(n) and isprime(n - 6):
                print(n)
                break
            elif isprime(n) and isprime(n + 6):
                print(n)
                break

    end = time.perf_counter()
    print(end - start)
