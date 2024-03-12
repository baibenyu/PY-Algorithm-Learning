# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/29 17:58'


while True:
    try:
        num = int(input())
        f1, f2 = 1, 1
        for x in range(3, num + 1):
            f1, f2 = f2 % 10007, (f1 + f2) % 10007  # 大数难题,一个数的余数与取余后数的余数相同
        print("{:.0f}".format(f2))
    except BaseException as e:
        print(e)
