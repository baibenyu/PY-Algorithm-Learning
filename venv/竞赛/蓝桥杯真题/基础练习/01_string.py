# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/29 18:55'

while True:
    try:
        n = 0b0
        for x in range(32):
            print("{:0>5b}".format(n))
            n += 1
    except BaseException as e:
        print(e)
