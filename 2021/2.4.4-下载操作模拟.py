#simulation:模拟

#非循环
temp = input('是否下载文件:')

if temp == 'y' or temp == 'Y':
    print('执行下载任务')
elif temp == 'n' or temp == 'N':
    print('退出下载任务')
else:
    print('请输入y,Y或n,N')


#循环
while True:
    temp = input('是否下载文件:')

    if temp == 'y' or temp == 'Y':
        print('执行下载任务')
        break
    elif temp == 'n' or temp == 'N':
        print('退出下载任务')
        break
    else:
        print('请输入y,Y或n,N')
        continue