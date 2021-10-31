import random
area_list = ["一等奖","二等奖","三等奖","谢谢惠顾"]
index = random.randint(0,4)
input("从1~4中抽一个幸运数吧:")
#用户所输入的数字与奖品没有关系^_^
print("你获得",area_list[index])