#字符转ASCII ord()
#ASCII转字符 chr()
password = '123456'
#第一步
list_asc = []
for i in range(0, len(password)):
    for j in password[i]:
        list_asc.append(ord(j))
print(password,"中每个数字的ASCII码值分别为",list_asc)

#第二步
total_asc = 0
for i in list_asc:
    total_asc += i
print("所有数字的ASCII码值的和为",total_asc)

#第三步
str_asc = ""
list_asc_reverse = []
for i in list_asc:
    str_asc += str(i)
print("ASCII顺序拼接为",str_asc)

for i in range(0, len(str_asc)):
    list_asc_reverse.append(str_asc[i])
list_asc_reverse.reverse()

str_asc_revese = ""
for i in list_asc_reverse:
    str_asc_revese += str(i)
print("ASCII倒序排列为",str_asc_revese)

#第四步
encrypted_password = int(str_asc_revese) + total_asc
print("加密后的密码为",encrypted_password)