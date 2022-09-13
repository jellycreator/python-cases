"""
生词对应
水仙花数:narcissistic number
个位数:units digit
十位数:ten digit
百位数:hundreds digit

收获
python内置函数pow(底数,指数)
for循环遵循<for 临时变量 in 可迭代对象>的形式,
其中整型数据如100不是可迭代对象,需要用range(100)转换成可迭代对象,
列表是可迭代对象,通过函数生成的列表需要用return返回,否则在for循环中返回None或者报错
举个栗子
def cutstr(temp = ''):
    string = str(temp)
    str_list = []
    control = 0
    while control < len(string):
        str_list.append(string[control])
        control += 1
    print(str_list)
cutstr(153)
此时函数只会打印一个[1,5,3]的列表,但不会返回这个列表
所以在运行
for i in cutstr(153):
时会报错,用type查看这里的cutstr(153)发现其是NoneType的对象,而非我们要的列表
因此在函数后面要加上return str_list来返回这个列表对象,cutstr(153)才能直接做列表(可迭代对象)使用.
"""
#----------------------------------------------------------------------------------#
print('第一种方法')
#索引切片
num = '153'
#nlist = [num[0],num[1],num[2]] 先列表会让运算过程变繁琐
#通过索引获取字符串的个十百位字符
hundreds_digit = int(num[0])
ten_digit = int(num[1])
units_digit = int(num[2])
narcissistic_number = hundreds_digit ** 3 + ten_digit ** 3 + units_digit ** 3
#与原数比较
if narcissistic_number == int(num):
    print(num,'是水仙花数')
else:
    print(num,'不是水仙花数')

#----------------------------------------------------------------------------------#
print('第二种方法')
#数学计算
num = 370
#获取百位数
hundreds_digit = num // 100 
#print(hundreds_digit)
#获取十位数
ten_digit = num // 10 - hundreds_digit * 10 
#print(ten_digit)
#获取个位数
units_digit = num % 10 
#print(units_digit)
#计算水仙花数
narcissistic_number = pow(units_digit,3) + pow(ten_digit,3) + pow(hundreds_digit,3)
#与原数比较
if narcissistic_number == num:
    print(num,'是水仙花数')
else:
    print(num,'不是水仙花数')

#----------------------------------------------------------------------------------#
print('第三种方法')
#因为.split() 这个方法不适用于没有分隔符的字符串,所以自己写个函数cutstr()替代
#字符串切分函数
def cutstr(temp = ''):
    string = str(temp)
    str_list = []
    control = 0
    #while control <= len(string): 由于字符串不能越界,否则会报错,因此不加等于
    while control < len(string):
        str_list.append(string[control])
        control += 1
    #print(str_list)
    return str_list
cutstr()

narcissistic_number = 0
list_one = []
num = 407
for i in cutstr(num): 
    list_one.append(int(i))
#print(list_one)
for i in list_one:
    narcissistic_number += pow(i,3)
#print(narcissistic_number)
if narcissistic_number == num:
    print(num,'是水仙花数')
else:
    print(num,'不是水仙花数')

#----------------------------------------------------------------------------------#
print('第四种方法')
#列表100~999的生成
list_one = []
for i in range(100,1000):
    list_one.append(i)

#水仙花数列表的计算生成
list_two = []
for num in list_one:
    hundreds_digit = num // 100 
    ten_digit = num // 10 - hundreds_digit * 10
    units_digit = num % 10
    narcissistic_number = pow(units_digit,3) + pow(ten_digit,3) + pow(hundreds_digit,3)
    if narcissistic_number == num:
        list_two.append(num)
    else:
        continue
print('水仙花数有',list_two)