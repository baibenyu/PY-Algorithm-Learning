def register():
    print('|--- 新建用户：N/n ---|')
    print('|--- 登录账号：E/e ---|')
    print('|--- 退出程序：Q/q ---|')
    order = input('|---请输入指令代码：')
    database = {'猫':'墨染希'}
    while True:
        if order in ['N','n']:
            username = input('请输入用户名：')
            while username in database:
                username = input('此用户名已被使用，请重新输入：')
            passwd = input('请输入密码：')
            database = dict(zip([username],[passwd]))
            print('注册成功，登录试试吧')
            order = input('|---请输入指令代码：')
        if order in ['E','e'] :
            username = input('请输入用户名：')
            while username not in database:
                username = input('用户名不存在，请重新输入：')
            passwd = input('请输入密码：')
            num = 1
            while passwd != database[username] and num<3:
                passwd = input('密码错误，请重试：')
                num += 1
            if passwd == database[username]:
                print('登录成功！')
            else:
                print('账户已被锁定，十五分钟后再试')
            break
        if order in ['Q','q']:
            break
                
        
