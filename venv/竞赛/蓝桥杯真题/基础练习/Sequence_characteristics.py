# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/30 10:09'

while True:
    try:
        n = int(input())
        seq = list(map(int, input().strip().split()))
        print(max(seq))
        print(min(seq))
        print(sum(seq))
    except BaseException as e:
        print(e)
