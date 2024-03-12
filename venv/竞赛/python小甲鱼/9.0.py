temp=input("请输入密码：")
pin="独属于我的AI"
i=1
left=3
while pin != temp and i<3:
    if "*" in (temp):
        temp=input('密码中不能含有“*”，请重新输入，您还有'+str(left)+'次机会:')
    else:
        i += 1
        left -= 1
        temp=input('密码错误，请重新输入，您还有'+str(left)+'次机会:')
if temp == pin :
    print("密码正确，正在进入程序")
else:
    print("抱歉，您的账号已锁定，请等待15分钟后再试")
