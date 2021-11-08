dict_arbook = {}
while True:
    print('\
=============\n\
欢迎使用通讯录\n\
1.添加联系人\n\
2.查看联系人\n\
3.删除联系人\n\
4.修改联系人\n\
5.查找联系人\n\
6.退出\n\
=============\
    ')
    choice = input('您的操作是:')


    if choice == '1':
        print('\
------------------------------')
        name = input('请输入联系人的姓名:')
        phonenum = input('请输入联系人的手机号:')
        email = input('请输入联系人的邮箱:')
        address = input('请输入联系人的地址:')
        print('\
------------------------------')
        if name == '' and phonenum == '' and email == '' and address == '':
            print('请输入正确信息')
        elif name != '' or phonenum != '' or email != '' or address != '':
            dict_arbook[name] = [phonenum, email, address]
            print('保存成功')
        else:
            print('未知错误1')


    elif choice == '2':
        print('\
-------------------------------------------------------')
        if dict_arbook != {}:
            print('姓名--电话号码--邮箱--地址')
            for i in dict_arbook.keys():
                print(i , end='     ')
                for j in dict_arbook[i]:
                    print(j,end='     ')
                print()
        elif dict_arbook == {}:
            print('通讯录无信息')
        else:
            print('未知错误2')
        print('\
-------------------------------------------------------')


    elif choice == '3':
        print('\
------------------------------')
        temp = input('请输入你要删除的联系人:')
        try:
            dict_arbook.pop(temp)
        except:
            if dict_arbook == {}:
                print('通讯录无信息')
            elif temp not in dict_arbook:
                print('该联系人不在通讯录中')
            else:
                print('未知错误3')


    elif choice == '4':
        print('\
------------------------------')
        temp = input('请输入你要修改的联系人:')
        if temp not in dict_arbook.keys():
            print('不存在该联系人')
        else:
            name = input('请输入新的姓名:')
            phonenum = input('请输入新的手机号:')
            email = input('请输入新的邮箱:')
            address = input('请输入新的地址:')

            if dict_arbook == {}:
                print('通讯录无信息')
            #1.不存在新姓名,沿用原有键
            elif name == '':
                count = 0
                for i in [phonenum , email , address]:
                    if i != '':
                        dict_arbook[temp][count] = i
                        count += 1
                        continue
                    elif i == '':
                        count += 1
                        continue
                    else:
                        print('未知错误4')
            #2.存在新姓名,对原键值克隆都新键上,并将原键值删去
            elif name != '':
                #依据temp寻找键值,原键所对应的列表
                dict_arbook[name] = dict_arbook[temp]
                count = 0
                for i in [phonenum , email , address]:
                    if i != '':
                        dict_arbook[name][count] = i
                        count += 1
                        continue
                    elif i == '':
                        count += 1
                        continue
                    else:
                        print('未知错误5')
                dict_arbook.pop(temp)
            else:
                print('未知错误6')
            print('修改成功')
        print('\
------------------------------')


    elif choice == '5':
        temp = input('请输入要查找的联系人姓名:')
        if dict_arbook == {}:
            print('通讯录无信息')
        elif temp not in dict_arbook.keys():
            print('该联系人不在该通讯录中')
        elif temp in dict_arbook.keys():
            print('\
-------------------------------------------------------')
            print('姓名--电话号码--邮箱--地址')
            print(temp , end='     ')
            for i in dict_arbook[temp]:
                print(i , end='     ')
            print()
            print('\
-------------------------------------------------------')
        else:
            print('未知错误7')
    elif choice == '6':
        break
    else:
        pass