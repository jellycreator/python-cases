for i in range(1,10):
    #print(i) 调试使用
    for j in range(i):
        j += 1 #range(1)时,指range(0,1),所以j是从0开始的,所以放进乘法表时要用j+1
        #print(j) 调试使用
        result = i * j
        print(j , "*" , i , '=' , result , end='    ')
    print()