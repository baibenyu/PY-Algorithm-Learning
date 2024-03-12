year=input("请输入年份：")

while not year.isdigit():
    year=input("请输入阿拉伯数字")
temp=int(year)
if temp%4 == 0 and temp%100 != 0:
    print("是闰年")
else:
    if temp%400 ==0:
        print("是闰年")
    else:
        print("不是闰年")
