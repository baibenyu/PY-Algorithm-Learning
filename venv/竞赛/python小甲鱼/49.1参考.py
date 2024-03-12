import math


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def solve():
    total = 2
    for next_prime in get_primes(3):  # 2是第一个素数，3是第二个素数，接下来靠+1往上走，靠素数判断方法判断是不是素数，是的话就累加
        if next_prime < 20000:
            total += next_prime
        else:
            print(total)
            return


if __name__ == '__main__':
    solve()
