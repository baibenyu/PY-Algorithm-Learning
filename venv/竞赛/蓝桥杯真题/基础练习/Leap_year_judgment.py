# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/29 18:49'

while True:
    try:
        n = int(input())
        if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
            print("yes")
        else:
            print("no")
    except BaseException as e:
        print(e)
