num = input("请输入地区编号:")
weight = float(input("请输入重量(kg):"))

while num == "01":
    if weight <= 2:
        money = 13
        break
    else:
       money = 13 + (weight - 2) * 3
       break

while num == "02":
    if weight <= 2:
        money = 12
        break
    else:
       money = 12 + (weight - 2) * 2
       break

while num == "03":
    if weight <= 2:
        money = 14
        break
    else:
       money = 14 + (weight - 2) * 4
       break
print("您所需付的邮费是:",money)