import copy
list_friend = []
while True:
    print("欢迎使用好友管理系统")
    print("1.添加好友")
    print("2.删除好友")
    print("3.备注好友")
    print("4.展示好友")
    print("5.退出")
    
    list_temp = copy.deepcopy(list_friend)
    for i in range(len(list_temp)):
        num = i + 1
        list_temp[i].insert(0,num)
    
    choice = input("请输入您的选项:")
    
    if choice == "1":
        temp = input("请输入你要添加的朋友:")
        list_friend.append([temp,""])
        continue
    elif choice == "2":
        temp = int(input("请输入你要删除的好友:"))
        del list_friend[temp-1]
        continue
    elif choice == "3":
        temp = int(input("请输入你要备注的好友:"))
        temp_2 = input("请输入要备注的信息:")
        list_friend[temp-1][1] = temp_2
        continue
    elif choice == "4":
        for j in list_temp:
            for k in j:
                print(k,end="   ")
            print()
            continue
        continue
    elif choice == "5":
        break
    else:
        pass