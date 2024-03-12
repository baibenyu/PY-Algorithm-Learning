# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/2 7:56'


# while True:
#     try:
#         print("{:}".format())
#     except BaseException as e:
#         print(e)

def an(n):  # 看清题目求表达式不是算结果
    for i in range(1, n + 1):
        print('sin(', end = '')
        print(i, end = '')
        if i != n:
            if i % 2 != 0:
                print('-', end = '')
            else:
                print('+', end = '')
    for i in range(1, n + 1):
        print(')', end = '')
    return ''


def sn(n):
    for i in range(1, n):
        print('(', end = '')
    for i in range(1, n + 1):
        print(an(i), end = '')
        print('+', end = '')
        print(n - i + 1, end = '')
        if i != n:
            print(')', end = '')


n = int(input())
sn(n)
