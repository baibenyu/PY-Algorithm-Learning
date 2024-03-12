# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/5 9:06'

def gcd(a, b):
    while b != 0:
        b, a = a % b, b
    return a


def two(op1, op2):
    a1, b1 = map(int, op1.split("/"))
    a2, b2 = map(int, op2.split("/"))
    b = b1 * b2 // gcd(b1, b2)
    a1 = a1 * b // b1
    a2 = a2 * b // b2
    a = a1 + a2
    return a, b


while True:
    k = int(input())
    list1 = input().split()
    if len(list1) > 1:
        for i in range(len(list1) - 1):
            a, b = two(list1[i], list1[i + 1])
            list1[i + 1] = f"{a}/{b}"
        b *= len(list1)
        m = gcd(a, b)
        if b // m != 1:
            print(f"{a // m}/{b // m}")
        else:
            print(f"{a // m}")
    else:
        a, b = map(int, list1[0].split("/"))
        m = gcd(a, b)
        if b // m != 1:
            print(f"{a // m}/{b // m}")
        else:
            print(f"{a // m}")
