# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/30 10:33'

while True:
    try:
        dict1 = {}
        n = int(input())
        for a in range(n):
            for b in range(a + 1):
                if b == 0 or b == a:
                    dict1[(a, b)] = 1
                else:
                    dict1[(a, b)] = dict1[(a - 1, b - 1)] + dict1[(a - 1, b)]
                print(dict1[(a, b)], end = " ")
            print()
    except BaseException as e:
        print(e)
