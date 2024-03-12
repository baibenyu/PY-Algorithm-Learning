# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/29 17:43'

while True:
    try:
        number = int(input())
        print("{:.0f}".format((1 + number) * number / 2))
    except:
        break
