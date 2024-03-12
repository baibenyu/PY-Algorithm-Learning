# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/22 14:38'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    cp = list()
    for i in range(n):
        cp.append(input().split())
    input()
    dog = input().split()
    dog = set(dog)
    for c in cp:
        if c[0] in dog and c[1] in dog:
            dog.remove(c[0])
            dog.remove(c[1])
    dog = list(dog)
    dog.sort()
    print(len(dog))
    if len(dog) != 0:
        print(' '.join(dog))

    end = time.perf_counter()
    print(end - start)
