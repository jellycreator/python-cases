num = '2021114qwq'
tuple_num = ('零','壹','贰','叁','肆','伍','陆','柒','捌','玖')
for i in num:
    try:
        num = num.replace(i,tuple_num[int(i)])
    except ValueError:
        pass
print(num)