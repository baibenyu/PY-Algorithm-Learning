# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/30 18:29'

while True:
    try:
        string = input().strip()
        print(int(string, base = 16))
    except BaseException as e:
        print(e)
