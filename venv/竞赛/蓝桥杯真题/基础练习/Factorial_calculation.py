# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/1 7:57'

while True:
    try:
        n = int(input())
        mul = 1
        for i in range(1, n+1):
            mul *= i
        print("{0}".format(mul))
    except BaseException as e:
        print(e)
