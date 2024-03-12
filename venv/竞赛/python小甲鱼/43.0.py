class C:
    def __init__(self, *args):
        if not args:
            print("并没有传入参数")
        else:
            print("传入了%d个参数，分别是：" % len(args), end=' ')
            for each in args:
                print(each, end=' ')


a = C(1,5,6,8,3,7)