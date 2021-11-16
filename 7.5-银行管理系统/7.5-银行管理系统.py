import random

class Bank:
    def __init__(self):
        print('进入系统成功')
    #暂时先用类内部的列表
    #类属性
    li_name = []            #名字
    li_id_number =[]        #身份证
    li_phonenumber = []     #电话号码
    li_account = []         #账号
    li_password = []        #密码
    li_money = []           #钱
    __count = 0             #定义私有属性账户冻结计数
    
    def open_account(self,name='',id_number='', phonenumber='', money='', password=''):         #定义开户方法
        if name == '' or id_number == '' or phonenumber == '' or money == '' or password == '': #当任何一个信息缺少时都不可开户
            print('请输入完整的信息')
        else:
            self.li_name.append(name)                   #存名字
            self.li_id_number.append(id_number)         #存身份证
            self.li_phonenumber.append(phonenumber)     #存电话号码
            self.li_password.append(password)           #存密码
            self.li_money.append(money)                 #预存的钱

            self.li_id_number.index(id_number)                  #身份证是唯一的,用身份证获取索引
            while True:                                         #进入循环体
                temp_account = str(random.randint(100000,999999))    #生成随机的6位数整数
                if temp_account not in self.li_account:         #如果这个6位数的账户不在账号列表中
                    self.li_account.append(temp_account)        #向账号列表写入该账号
                    print('您的账户是:%s' % temp_account)
                    break                                       #写入完成后退出循环
                else:                                           #生成6位数的账号在账号列表中已存在
                    continue                                    #继续执行循环获取6位数的账号
    
    def inquiry(self,inquiry_account='', inquiry_password=''):  #定义查询功能方法
        if inquiry_account not in self.li_account:         #判断账号是否在账号列表中
            print('该账户不存在')
        else:
            inquiry_account_index = self.li_account.index(inquiry_account) #获取账户的账号索引
            if inquiry_account == self.li_account(inquiry_account_index) and inquiry_password == self.li_password(inquiry_account_index): #当账号和密码都对上时
                print('账户%s还有%s元' % self.li_account(inquiry_account_index),self.li_money(inquiry_account_index))
            
    def withdraw(self): #定义取款方法
        pass
    #存款
    #转账
    #锁定

    #解锁
    
    #存盘
    #退出
    def __del__(self):
        print('系统已退出')

#交互操作
bank = Bank()   #实例化对象
bank.open_account('a','b','c','200','123456')   #开户操作
bank.inquiry(input('请输入账户'),'123456')