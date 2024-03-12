# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/1 8:18'

while True:
    try:
        time = int(input())
        h, m, s = time // 3600, time % 3600 // 60, time % 60
        print("{0}:{1}:{2}".format(h, m, s))
    except BaseException as e:
        print(e)
