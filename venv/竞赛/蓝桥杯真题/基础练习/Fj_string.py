# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/2 19:11'

while True:
    try:
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 难点在于找到规律,找不到就想死也想不出来
        l = "A"
        n = eval(input())
        for i in range(1, n):
            l = l + s[i] + l
        print(l)
    except BaseException as e:
        print(e)
