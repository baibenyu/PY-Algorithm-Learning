def pla(temp):
    length=len(temp)
    i = 0
    while i < length//2:
        if temp[i] == temp[length-i-1]:
            i += 1
        else:
            print("不是回文联")
            break
    if i == length//2:
            print('是回文联')
temp=input("请输入一句话：")
pla(temp)
#可以用revese方法赋值另一个变量，若两个变量相同则为回文联
