def hanoi(n,a,b,c):
    if n == 1:
        print(a,'-->',c)    #如果只有一层,只需将盘从A移到C
    else:
        hanoi(n-1,a,c,b)    #将前n-1个盘子从A移动到B上
        print(a, '-->', c)  #将最底下的第64个盘子从A移到C上
        hanoi(n-1,b,a,c)    #将B上的63个盘子移动到C上
n = int(input('请输入汉诺塔层数:'))
hanoi(n,'A','B','C')

#参考资料 小甲鱼零基础入门学习Python