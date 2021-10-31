ticket = input("是否有车票(y/n)")
if ticket == "y":
    print("请进行安检.")
    security = input("是否携带危险物品(y/n)")
    if security == "n":
        print("顺利进站.")
    else:
        print("携带危险物品,禁止进站.")
else:
    print("没有车票不允许进站.")

#将None该为True则持续运行 CTRL+C 可以退出循环
while None:
    ticket = input("是否有车票(y/n)")
    if ticket == "y":
        print("请进行安检.")
        security = input("是否携带危险物品(y/n)")
        if security == "n":
            print("顺利进站.")
        else:
            print("携带危险物品,禁止进站.")
    else:
        print("没有车票不允许进站.")