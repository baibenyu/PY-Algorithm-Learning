import easygui as e
import sys
import random

secret = random.randint(1,10)
e.msgbox('---------------我爱白羽工作室--------------')
guess = e.integerbox("不妨猜一下白羽现在心里想的是哪个整数:(1:10)",'猜数字小游戏')
if guess == secret:
    e.msgbox("""天啊,你是白羽心里的蛔虫吗?!\n猜中了，就奖励你一点好感度吧!""")
else:
    e.msgbox("居然猜错了,好感度降低100!")
    if guess>secret:
        e.msgbox("哼，我才不会告诉你，猜大了呢")
    else:
        e.msgbox("啊~啊，猜小了呀")
number=1
while guess !=secret and number<3:
    guess = e.integerbox("再试一次呗",'猜数字小游戏')
    number=number+1
    if guess == secret:
        e.msgbox("""天啊,你是白羽心里的蛔虫吗?!\n猜中了，就奖励你一点好感度吧!""")
    else:
        e.msgbox("居然猜错了,好感度降低100!")
        if guess > secret:
            e.msgbox("哼，我才不会告诉你，猜大了呢")
        else:
            e.msgbox("啊~啊，猜小了呀")
if number>3 and guess!=secret:
    e.msgbox("没救了ヽ(ｏ`皿′ｏ)ﾉ")
else:
    e.msgbox("游戏结束了,下次再玩吧ヾ(￣▽￣)Bye~Bye~")



