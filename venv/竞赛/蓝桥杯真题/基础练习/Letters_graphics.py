# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/29 19:25'

while True:
    try:
        n, m = map(int, input().strip().split())
        a = temp = 65
        for x in range(n):
            count = 0
            while temp > 65 and count < m:
                print(chr(temp), end = "")
                temp -= 1
                count += 1
            else:
                while count < m:
                    print(chr(temp), end = "")
                    temp += 1
                    count += 1
            a += 1
            temp = a
            print()
    except BaseException as e:
        print(e)
