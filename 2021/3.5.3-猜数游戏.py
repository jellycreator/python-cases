import random

temp = random.randint(1,100) #生成1~100的一个随机整数
num = int(float(input("猜下我现在想的是多少(1~100):")))
print(temp)
times = 4
while times > 0:
    if num == temp:
        print("恭喜,猜对了!")
        break
    elif num < temp:
        num = int(float(input("小了~小了~再试下吧(还有%d次机会):" % times)))
        times -= 1
        continue
    elif num > temp:
        num = int(float(input("大了~大了~再试下吧(还有%d次机会)" % times)))
        times -= 1
        continue
    else:
        num = int(float(input("请输入正确的数据(还有%d次机会)" % times)))
        times -= 1
        continue
while times == 0:
    print("错误次数过多,请稍后再试")
    break
input()