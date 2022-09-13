list_one = []
for i in range(1,101):
    if i % 7 == 0:
        list_one.append(i)
        continue
    else:
        continue
print("100以内需要拍手的数字为",list_one)