passward=input("请输入新密码：")
length=len(passward)
if (passward.isnumeric() or passward.isalpha()) or length < 9:
    print("您的安全等级为：低\n"
        """1.
2.
3.""")
elif passward.isalnum() and length>8:
    print("您的安全等级为：中\n"
        """ 1.
2.
3.""")
elif passward[0].isalpha() and length>16:
    print("您的安全等级为：高"
              "请继续保持")

        
