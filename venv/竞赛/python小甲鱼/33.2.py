def int_input():
    temp = input('请输入一个整数：')
    try:
        temp = int(temp)
    except ValueError:
        print('出错您输入的不是整数')

    while type(temp) != int:
        temp = input('请输入一个整数：')
        try:
            temp = int(temp)
        except ValueError:
            print('出错您输入的不是整数')
int_input()