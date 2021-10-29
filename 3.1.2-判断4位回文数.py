#palindrome number:回文数

#检测值是否可以转成整型，可以直接转为temp，不可以返回False
def int_test(temp): 
    try:
        temp = int(temp)
        return temp    
    except:
        return False

#回文数的判断
def panum_print(num = ''): #panum:abbr[palindrome number]
        string = str(num)
        if string[0] == string[-1] and string[1] == string[-2]:
            print(num,'是回文数')
        else:
            print(num,'不是回文数')

def panum_return(num = ''): #panum:abbr[palindrome number]
        string = str(num)
        if string[0] == string[-1] and string[1] == string[-2]:
            return int(string)
        else:
            pass

#输出指定区间的回文数列表
def panum_range(num_one = '',num_two = ''): 
    li_one = []
    li_two = []
    for i in range(1000,10001):
        li_one.append(i)
    for j in li_one:
        while panum_return(j) != None:
            li_two.append(j)
            break
    print(li_two)
#panum_range(1000,10001)

#通过True和None来控制交互循环是否运行
while None:
    num = input('请输入四位回文数:')
    #数据类型判断
    while int_test(num) == False:
        num = input('请输入纯数字四位回文数:')
    panum_print(num)


