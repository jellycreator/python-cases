#回文判断
def palindrome(string = ''): #panum:abbr[palindrome number]
    string = str(string)
    cycle_num = len(string) // 2
    temp = True
    for i in range(cycle_num):
        #print(i)
        temp = temp and string[i] == string[(-1)*(i+1)]
        #print(temp)
    if temp == True:
        print(string,'is palindrome')
    else:
        print(string,'is not palindrome')

while True:
    temp = input('输入内容判断是否回文(/b可退出程序):')
    if temp == '/b':
        break
    else:
        palindrome(temp)
