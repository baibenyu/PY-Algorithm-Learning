print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1:查询联系人资料 ---|')
print('|--- 2:插入新的联系人 ---|')
print('|--- 3:删除已有的联系人 ---|')
print('|--- 4:查看所有通讯录 ---|')
print('|--- 5:退出通讯录程序 ---|')

datebase = {'猫': '墨染希', '幼刀': '丛雨', '人偶': '艾莉丝'}

while True:
    temp = int(input("请输入对应数字来执行操作:"))

    if temp == 1:
        name = input("请输入要查询的联系人名称：")
        if name in datebase:
            print(datebase[name])
        else:
            print("联系人未存储")

    if temp == 2:
        insertionN = input("请输入要插入的联系人名称：")
        if insertionN in datebase:
            temp1 = input("是否要修改联系人资料：")
            if temp1 == '是':
                insertionP = input("请输入修改后的联系人电话：")
                datebase[insertionN] = insertionP
        else:
            insertionP = input("请输入要插入的联系人电话：")
            datebase[insertionN] = insertionP

    if temp == 3:
        delete = input("请输入要删除的联系人名称：")
        if delete not in datebase:
            print("您要删除的联系人不存在！")
        else:
            datebase.pop(delete)

    if temp == 4:
        print('姓名\t手机号码')
        for key, value in datebase.items():
            print(key, value)

    if temp == 5:
        print("程序结束")
        break
