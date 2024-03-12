print('---------------我爱白羽工作室--------------')

temp = input("不妨猜一下白羽现在心里想的是哪个数字:")
try:
    guess = int(temp)
except (ValueError,EOFError,KeyboardInterrupt):
    print('输入的不是整数，请重新输入')
if guess == 3:
    print("我草,你是白羽心里的蛔虫吗?!")
    print("切,猜中了，就奖励你一点好感度吧!")
else:
    print("居然猜错了,好感度降低100!")

print("游戏结束了,下次再玩吧ヾ(￣▽￣)Bye~Bye~")
