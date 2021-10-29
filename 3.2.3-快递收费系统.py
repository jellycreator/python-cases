num = input("请输入地区编号:")
weight = str(float(input("请输入重量(kg):")))

while num == "01":
    if float(weight) <= 2:
        money = 13
        break
    elif weight[2] != "0":
        money = 13 + ((int(float(weight)) - 2) + 1) * 3
        break
    elif weight[2] == "0":
        money = 13 + (int(float(weight)) - 2) * 3
        break

while num == "02":
    if float(weight) <= 2:
        money = 12
        break
    elif weight[2] != "0":
        money = 12 + ((int(float(weight)) - 2) + 1) * 2
        break
    elif weight[2] == "0":
        money = 12 + (int(float(weight)) - 2) * 2
        break

while num == "03":
    if float(weight) <= 2:
        money = 14
        break
    elif weight[2] != "0":
        money = 14 + ((int(float(weight)) - 2) + 1) * 4
        break
    elif weight[2] == "0":
        money = 14 + (int(float(weight)) - 2) * 4
        break
print("您所需付的邮费是:",money)