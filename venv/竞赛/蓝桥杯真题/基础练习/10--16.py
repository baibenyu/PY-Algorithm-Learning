# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/30 18:32'

while True:
    try:
        string = hex(int(input().strip()))
        print(string[2:].upper())
    except BaseException as e:
        print(e)
