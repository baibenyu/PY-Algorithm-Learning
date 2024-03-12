# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/30 17:53'

while True:
    try:
        n = int(input())
        list1 = list(map(int, input().strip().split()))
        list1.sort()
        for each in list1:
            print(each, end = " ")
    except BaseException as e:
        print(e)
