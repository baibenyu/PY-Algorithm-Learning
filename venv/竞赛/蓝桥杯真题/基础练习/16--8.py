# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/30 18:05'

while True:
    try:
        list1 = []
        n = int(input())
        for i in range(n):
            list1.extend(input().strip().split())
        for i in range(n):
            x = list1[i]
            y = oct(int(x, base = 16))
            print(y[2:])
    except BaseException as e:
        print(e)
