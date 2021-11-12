stu_dict = {'gg':'love'} #全局变量

#查找函数
def stu_search(name=''):
    if stu_dict == {}:
        print('系统无信息')
    else:
        for i in stu_dict.items():
            if i[0] == name:
                print(i)
            else:
                pass

#修改函数
def stu_modify(name='', information=''):
    global stu_dict
    if stu_dict == {}:
        print('系统无信息')
    elif name not in stu_dict.keys():
        print('该学生不在系统中')
    else:
        stu_dict[name] = information
        print('修改成功')

#添加函数
def stu_add(name='', information=''):
    global stu_dict
    stu_dict[name] = information
    print('添加成功')

#删除函数
def stu_remove(remove=''):
    global stu_dict
    if stu_dict == {}:
        print('系统无信息')
    else:
        try:
            stu_dict.pop(remove)
            print('删除成功')
        except:
            print('该学生不在系统中')

while True:
    print('======================')
    print('欢迎使用学生信息管理系统')
    print('1.查找学生')
    print('2.修改学生')
    print('3.增加学生')
    print('4.删除学生')
    print('5.退出系统')
    print('======================')
    temp = input('请输入操作:')
    if temp == '1':
        stu_search(name=input('请输入要查找的学生姓名'))
    elif temp == '2':
        stu_modify(name=input('请输入要修改的学生姓名'), information=input('请输入要修改的学生信息'))
    elif temp == '3':
        stu_add(name=input('请输入要添加的学生姓名'), information=input('请输入要添加的学生信息'))
    elif temp == '4':
        stu_remove(remove=input('请输入要删除的学生姓名'))
    elif temp == '5':
        break
    else:
        pass
