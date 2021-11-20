import random
#bug
"""
Exception ignored in: <function Bank.__del__ at 0x000001F474FD16C0>
TypeError: Bank.__del__() missing 1 required positional argument: 'del_options'
"""


class Bank():
    #类属性   
    __ad_account = 'admin'      #管理员账号
    __ad_password = '123456'    #管理员密码
    li_name = []                #名字-字符串
    li_id_number =[]            #身份证-字符串
    li_phonenumber = []         #电话号码-字符串
    li_account = []             #账号-字符串
    li_password = []            #密码-字符串
    li_money = []               #钱-整型
    __count = 2                 #定义私有属性账户密码容错次数
    __freeze_dict = {}          #定义私有属性账户冻结计数字典{账号:密码错误次数}




    # 对象被释放时的显示
    def __del__(self, del_options=''):
        self.del_options = del_options
        if self.del_options == False:
            print('管理员密码错误,进入系统失败')
        else:
            print('系统已退出')
    
    # 对象创建时的操作
    def __init__(self, ad_account='', ad_password=''):
        self.ad_account = ad_account
        self.ad_password = ad_password
        if self.ad_account == self.__ad_account and self.ad_password == self.__ad_password:
            self.switch = True
            print('进入系统成功')
        else:
            self.switch = False
            self.__del__(del_options=False)

    # 开户方法
    def open_account(self,name='',id_number='', phonenumber='', money='', password=''):
        #当任何一个信息缺少时都不可开户
        if name == '' or id_number == '' or phonenumber == '' or money == '' or password == '':
            print('请输入完整的信息')
        else:
            self.li_name.append(name)                   #存名字
            self.li_id_number.append(id_number)         #存身份证
            self.li_phonenumber.append(phonenumber)     #存电话号码
            self.li_password.append(password)           #存密码
            self.li_money.append(money)                 #预存的钱

            while True:
                #生成随机的6位数整数
                temp_account = str(random.randint(100000,999999))
                #如果这个6位数的账户不在账号列表中
                if temp_account not in self.li_account:
                    #向账号列表写入该账号
                    self.li_account.append(temp_account)
                    print('您的账户是:%s' % temp_account)
                    #写入完成后退出循环
                    break
                #生成6位数的账号在账号列表中已存在
                else:
                    #继续执行循环获取6位数的账号
                    continue

    # 冻结计数方法
    def freeze(self, inquiry_account='', inquiry_password=''):
        #判断账号是否在账号列表中
        if inquiry_account not in self.li_account:
            print('该账户不存在')
        else:
            # 获取账户的账号索引
            inquiry_account_index = self.li_account.index(inquiry_account)
            # 当账户处在冻结字典中
            if self.li_account[inquiry_account_index] in self.__freeze_dict.keys():
                #如果该账户冻结计数为零,则进行下面的操作
                if self.__freeze_dict[inquiry_account] == 1:
                    print('错误次数过多,账户%s已冻结' % inquiry_account)
                # 冻结字典中已存在该账户,且未冻结
                else:
                    self.__freeze_dict[inquiry_account] -= 1
                    print('密码错误,还有%d次机会' % self.__freeze_dict[inquiry_account])
            # 当账号和密码都对上时
            elif inquiry_password == self.li_password[inquiry_account_index]:
                # 当该账户存在冻结次数且未被冻结时
                if self.li_account[inquiry_account_index] in self.__freeze_dict.keys() and self.__freeze_dict[inquiry_account] > 0:
                    # 从冻结字典中删除该成功进入的账户
                    self.__freeze_dict.pop(inquiry_account)
                    # 返回真值
                    return True
                else:
                    return True
            # 账号对不上密码时,触发账号冻结计数,若该输错密码的账号不在冻结计数字典内,则向字典中添加
            elif self.li_account[inquiry_account_index] not in self.__freeze_dict.keys():
                self.__freeze_dict[inquiry_account] = self.__count
                print('密码错误,还有%d次机会' % self.__freeze_dict[inquiry_account])
            # 容错
            else:
                pass

    # 查询
    def inquiry(self, inquiry_account=''):
        # 获取账户的账号索引
        inquiry_account_index = self.li_account.index(inquiry_account)
        print('账户%s还有%s元' % (self.li_account[inquiry_account_index],self.li_money[inquiry_account_index]))

    # 取款
    def withdraw(self, inquiry_account='', withdraw_money=''):
        # 获取账户的账号索引
        inquiry_account_index = self.li_account.index(inquiry_account)
        if self.li_money[inquiry_account_index] >= withdraw_money:
            self.li_money[inquiry_account_index] -= withdraw_money
            print('取款成功,账户%s余额有%d元' % (self.li_account[inquiry_account_index], self.li_money[inquiry_account_index]))
        else:
            print('余额不足')

    # 存款
    def deposit(self, inquiry_account='', deposit_money=''):
        # 获取账户的账号索引
        inquiry_account_index = self.li_account.index(inquiry_account)
        self.li_money[inquiry_account_index] += deposit_money
        print('存款成功,账户%s余额有%d元' % (self.li_account[inquiry_account_index], self.li_money[inquiry_account_index]))

    # 转账
    def transfer(self, inquiry_account='', receive_account='', transfer_money=''):
        # 获取账户的账号索引
        inquiry_account_index = self.li_account.index(inquiry_account)
        receive_account_index = self.li_account.index(receive_account)
        if transfer_money <= self.li_money[inquiry_account_index]:
            # 第一步,从转出账户扣除转账金额
            self.li_money[inquiry_account_index] -= transfer_money
            # 第二步,向转入账户增加转账金额
            self.li_money[receive_account_index] += transfer_money
            print('转账成功,转出账户%s剩余%d元' % (self.li_account[inquiry_account_index], self.li_money[inquiry_account_index]))
        else:
            print('账户%s余额不足' % self.li_account[inquiry_account_index])

    #锁定
    def lock(self, inquiry_account='',inquiry_password=''):
        #判断账号是否在账号列表中
        if inquiry_account not in self.li_account:
            print('该账户不存在')
        else:
            # 获取账户的账号索引
            inquiry_account_index = self.li_account.index(inquiry_account)
            if inquiry_password == self.li_password[inquiry_account_index]:
                self.__freeze_dict[inquiry_account] = 1
                print('账户%s已冻结' % inquiry_account)
            else:
                print('密码不正确')
                
    #解锁
    def unlock(self, inquiry_account='', inquiry_password=''):
        #判断账号是否在账号列表中
        if inquiry_account not in self.li_account:
            print('该账户不存在')
        else:
            # 获取账户的账号索引
            inquiry_account_index = self.li_account.index(inquiry_account)
            if inquiry_password == self.li_password[inquiry_account_index]:
                if inquiry_account not in self.__freeze_dict.keys():
                    print('该账户未被冻结')
                else:
                    if self.__freeze_dict[inquiry_account] != 1:
                        self.__freeze_dict.pop(inquiry_account)
                        print('账户%s的密码错误次数已重置' % inquiry_account)
                    else:
                        self.__freeze_dict.pop(inquiry_account)
                        print('账户%s已解冻' % inquiry_account)
            else:
                print('密码不正确')

    #存盘
    def cunpan(self):
        pass

    #退出
    def bank_quit(self, ad_account='', ad_password=''):
        if ad_account == self.__ad_account and ad_password == self.__ad_password:
            return True
        else:
            return False
    
#交互操作,以下部分以后可以用GUI界面代替
while True:
    ad_account = input('请输入管理员账户:')
    ad_password = input('请输入管理员密码:')
    bank = Bank(ad_account=ad_account, ad_password=ad_password)   #实例化对象
    break

while bank.switch:
    print('1.开户')
    print('2.查询')
    print('3.取款')
    print('4.存款')
    print('5.转账')
    print('6.锁定')
    print('7.解锁')
    print('8.存盘')
    print('9.退出')
    choice = input('请输入操作:')

    #开户
    if choice == '1':
        print('进入开户系统,输入/b退出')
        while True:
            quit_temp = 0
            name = input('请输入姓名:')
            if name == '/b':
                break
            id_number = input('请输入身份证号:')
            if id_number == '/b':
                break
            phonenumber = input('请输入电话号码:')
            if phonenumber == '/b':
                break
            money = input('请输入预存金额:')
            if money == '/b':
                break
            else:
                try:
                    money = int(money)
                    if money >= 0:
                        continue
                    else:
                        print('金额不能为负')
                        quit_temp = 1
                except:
                    print('金额只能为阿拉伯数字')
                    quit_temp = 1
            password = input('请输入密码:')
            if password == '/b':
                break
            if quit_temp != 1:
                bank.open_account(name=name, id_number=id_number, phonenumber=phonenumber, money=money, password=password)
            else:
                pass

    #查询
    elif choice == '2':
        print('进入查询系统,输入/b退出')
        while True:
            inquiry_account = input('请输入卡号:')
            if inquiry_account == '/b':
                break
            inquiry_password = input('请输入密码:')
            if inquiry_password == '/b':
                break
            if bank.freeze(inquiry_account=inquiry_account, inquiry_password=inquiry_password) == True:
                bank.inquiry(inquiry_account=inquiry_account)
            else:
                continue

    # 取款
    elif choice == '3':
        print('进入取款系统,输入/b退出')
        while True:
            inquiry_account = input('请输入卡号:')
            if inquiry_account == '/b':
                break
            inquiry_password = input('请输入密码:')
            if inquiry_password == '/b':
                break
            # 取款操作页面
            while bank.freeze(inquiry_account=inquiry_account, inquiry_password=inquiry_password) == True:
                inquiry_account_index = bank.li_account.index(inquiry_account)
                print('进入取款页面,输入/b返回上一步')
                print('账户%s余额有%d元' % (bank.li_account[inquiry_account_index], bank.li_money[inquiry_account_index]))
                withdraw_money = input('请输入取款金额:')
                if withdraw_money == '/b':
                    break
                else:
                    # 在这里加入对取款金额是否可以转为整型的判断
                    try:
                        withdraw_money = int(withdraw_money)
                        bank.withdraw(inquiry_account=inquiry_account, withdraw_money=withdraw_money)
                    except:
                        print('请输入正确的取款金额(仅含阿拉伯数字)')
            else:
                continue

    # 存款
    elif choice == '4':
        print('进入存款系统,输入/b退出')
        while True:
            inquiry_account = input('请输入卡号:')
            if inquiry_account == '/b':
                break
            inquiry_password = input('请输入密码:')
            if inquiry_password == '/b':
                break
            # 存款操作页面
            while bank.freeze(inquiry_account=inquiry_account, inquiry_password=inquiry_password) == True:
                inquiry_account_index = bank.li_account.index(inquiry_account)
                print('进入存款页面,输入/b返回上一步')
                print('账户%s余额有%d元' % (bank.li_account[inquiry_account_index], bank.li_money[inquiry_account_index]))
                deposit_money = input('请输入存款金额:')
                if deposit_money == '/b':
                    break
                else:
                    # 在这里加入对存款金额是否可以转为整型的判断
                    try:
                        deposit_money = int(deposit_money)
                        bank.deposit(inquiry_account=inquiry_account, deposit_money=deposit_money)
                    except:
                        print('请输入正确的存款金额(仅含阿拉伯数字)')
            else:
                continue

    # 转账
    elif choice == '5':
        print('进入转账系统,输入/b退出')
        while True:
            inquiry_account = input('请输入卡号:')
            if inquiry_account == '/b':
                break
            inquiry_password = input('请输入密码:')
            if inquiry_password == '/b':
                break
            # 转账操作页面
            while bank.freeze(inquiry_account=inquiry_account, inquiry_password=inquiry_password) == True:
                    inquiry_account_index = bank.li_account.index(inquiry_account)
                    print('进入转账页面,输入/b返回上一步')
                    print('账户%s余额有%d元' % (bank.li_account[inquiry_account_index], bank.li_money[inquiry_account_index]))
                    receive_account = input('请输入转入卡号:')
                    if receive_account == '/b':
                        break
                    elif receive_account not in bank.li_account():
                        print('转入账号不存在')
                        continue
                    else:
                        print('进入转账操作,输入/b返回上一步')
                        while True:
                            transfer_money = input('请输入转账金额:')
                            if transfer_money == '/b':
                                break
                            else:
                                try:
                                    transfer_money = int(transfer_money)
                                    bank.transfer(inquiry_account=inquiry_account, receive_account=receive_account, transfer_money=transfer_money)
                                except:
                                    print('请输入正确的转账金额(仅含阿拉伯数字)')
                                    continue
            else:
                continue

    # 锁定
    elif choice == '6':
        print('进入锁定系统,输入/b退出')
        while True:
            inquiry_account = input('请输入卡号:')
            if inquiry_account == '/b':
                break
            inquiry_password = input('请输入密码:')
            if inquiry_password == '/b':
                break
            bank.lock(inquiry_account=inquiry_account,inquiry_password=inquiry_password)
    
    # 解锁
    elif choice == '7':
        print('进入解锁系统,输入/b退出')
        while True:
            inquiry_account = input('请输入卡号:')
            if inquiry_account == '/b':
                break
            inquiry_password = input('请输入密码:')
            if inquiry_password == '/b':
                break
            bank.unlock(inquiry_account=inquiry_account,inquiry_password=inquiry_password)

    # 存盘
    elif choice == '8':
        bank.cunpan()

    #退出
    elif choice == '9':
        ad_account = input('请输入管理员账户:')
        ad_password = input('请输入管理员密码:')
        back_value = bank.bank_quit(ad_account=ad_account, ad_password=ad_password)
        if back_value == True:
            break
        elif back_value == False:
            continue

    #容错
    else:
        pass