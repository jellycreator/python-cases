def test(username="",password=""):
    if username == 5201314 and password == 123456:
        return True
    else:
        False
num = 1
while num <= 3:
    username = int(input("请输入账号/用户名:"))
    password = int(input("请输入密码:"))
    if test(username=username, password=password) == True:
        print("登录成功")
        break
    elif num == 3:
        print("输入错误次数过多,请稍后再试")
        break
    else:
        print("账号/密码错误,请重试")
        num += 1
