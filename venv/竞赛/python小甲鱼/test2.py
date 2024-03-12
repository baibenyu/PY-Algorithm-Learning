import random
num = random.randint(0,10)
print(num)
guess =int(input("请输入数字："))
i = 0
while i < 3 :
    i += 1
    if num > guess :
        guess =int(input("猜小了，请重新猜："))
    elif num < guess :
        guess =int(input("猜大了，请重新猜："))
    else:
        print("恭喜你，猜对了,游戏结束.")
        break
if i == 3 :
    print("ok")
