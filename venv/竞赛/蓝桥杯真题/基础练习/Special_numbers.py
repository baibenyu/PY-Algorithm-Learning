# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/30 10:57'

while True:
    try:
        for x in range(100, 1000):
            sum_up = 0
            temp = x
            while temp:
                y = temp % 10
                temp = temp // 10
                sum_up += y ** 3
            if sum_up == x:
                print(x)
    except BaseException as e:
        print(e)
