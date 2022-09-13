def f(num=''):
    if num < 1:
        print('输入有误')
        return None
    elif num == 1 or num == 2:
        return 1
    else:
        return f(num-1) + f(num-2)
n = 12
if f(n) != None:
    print('%d对应的斐波那契数列为%d' % (n,f(n)))

#参考资料 小甲鱼零基础入门学习Python