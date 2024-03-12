import random
secret = random.randint(1,10)
print('---------------我爱白羽工作室--------------')
temp = input("不妨猜一下白羽现在心里想的是哪个整数:")
while not temp.isdigit():
    temp=input("请输入阿拉伯数字")
guess = int(temp)
if guess == secret:
    print("天啊,你是白羽心里的蛔虫吗?!")
    print("猜中了，就奖励你一点好感度吧!")
else:
    print("居然猜错了,好感度降低100!")
    if guess>secret:
        print("哼，我才不会告诉你，猜大了呢")
    else:
        print("啊~啊，猜小了呀")
number=1
while guess !=secret and number<3:
    temp = input("再试一次呗:")
    guess = int(temp)
    number=number+1
    if guess == secret:
        print("天啊,你是白羽心里的蛔虫吗?!")
        print("猜中了，就奖励你一点好感度吧!")
    else:
        print("居然猜错了,好感度降低100!")
        if guess>secret:
            print("哼，我才不会告诉你，猜大了呢")
        else:
            print("啊~啊，猜小了呀")
if number>3 and guess!=secret:
    print("没救了ヽ(ｏ`皿′ｏ)ﾉ")
else:
    print("游戏结束了,下次再玩吧ヾ(￣▽￣)Bye~Bye~")
print("Bye~Bye~")
