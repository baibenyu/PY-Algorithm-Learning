# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/30 11:19'

while True:
    try:
        n = int(input())
        for x in range(10000, 1000000):
            string = str(x)
            length = len(string)
            flag = True
            for y in range(length // 2):
                if string[y] != string[length - y - 1]:
                    flag = False
                    break
            if flag:
                sum_up = sum(map(int, list(string)))
                if sum_up != n:
                    flag = False
            if flag:
                print(x)
    except BaseException as e:
        print(e)
