# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/30 10:16'

while True:
    try:
        n = int(input())
        seq = list(map(int, input().strip().split()))
        target = int(input())
        if target in seq:
            print(seq.index(target)+1)
        else:
            print(-1)
    except BaseException as e:
        print(e)
