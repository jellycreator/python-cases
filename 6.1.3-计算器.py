import copy

temp = ''
ys_symbol = ['*', '/', '+', '-'] #ys_symbol是运算符列表

#取运算符左边的数
def left(default): #default是用index获取的索引值
    #num = default #将default拷贝给num,这是浅拷贝,num的改变会影响default,所以应该使用深度拷贝
    num = copy.deepcopy(default) #这里是深度拷贝,将num指向一个全新的值
    def left_sum(num):
        num -= 1
        if temp[num] in ys_symbol:
            if num <= 0:
                return temp[0:default]
            else:
                num += 1
                return temp[num:default]
        else:
            return left_sum(num)
    
    return left_sum(num)

#取运算符右边的数
def right(default):
    num = copy.deepcopy(default)
    def right_sum(num):
        num += 1
        try: #右边界超索引判断,并返回右端点的值
            if temp[num] in ys_symbol:
                return temp[default+1:num]
            else:
                return right_sum(num)
        except:
            return temp[default+1:len(temp)]
    return right_sum(num)

#运算函数
def total(left_num, right_num,operative_symbol):
    if operative_symbol == '*':
        return left_num * right_num
    elif operative_symbol == '/':
        return left_num / right_num
    elif operative_symbol == '+':
        return left_num + right_num
    elif operative_symbol == '-':
        return left_num - right_num
    else:
        return None

#匹配函数
def match(ma=''):
    global temp
    temp = ma
    for symbol in ys_symbol:
        while True:
            try:
                left_num = left(temp.index(symbol))
                right_num = right(temp.index(symbol))
                temp_replace = total(float(left_num),float(right_num),symbol)
                temp = temp.replace(str(left_num)+symbol+str(right_num),str(temp_replace))
                continue
            except:
                break
    print('结果为:',temp)

match(ma=input('四则运算:'))