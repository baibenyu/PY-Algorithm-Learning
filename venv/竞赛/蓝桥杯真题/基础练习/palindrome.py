# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/30 11:07'

# while True:
try:
    for x in range(1000, 10000):
        string = str(x)
        length = len(string)
        flag = True
        for y in range(length // 2):
            if string[y] != string[length - y - 1]:
                flag = False
        if flag:
            print(x)
except BaseException as e:
        print(e)
