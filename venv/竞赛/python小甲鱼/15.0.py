temp=input("请输入一个整数(输入Q结束程序)：")
while temp != "Q":
    temp=int(temp)
    print("十进制→十六进制：",temp,"→","%#x" % (temp))
    print("十进制→八进制：",temp,"→","%#o" % (temp))
    print("十进制→二进制：",temp,"→",bin(temp))
    temp=input("请输入一个整数(输入Q结束程序)：")

