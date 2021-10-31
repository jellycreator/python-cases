#生成价格与序号的嵌套列表
"""
list = [399,4369,539,288,109,749,235,190,99,1000]
list2 = []
num = 1
for i in list:
    list2.append([num,i])
    num += 1
print(list2)
"""

list_price = [[1, 399], [2, 4369], [3, 539], [4, 288], [5, 109], [6, 749], [7, 235], [8, 190], [9, 99], [10, 1000]]
list = []
for i in list_price:
    list.append(i[1])
ascending_sort = sorted(list)

#升序排列
list_3 = []
for i in ascending_sort: #这部分可以封装到函数中
    for j in list_price:
        if  j[1] == i:
            list_3.append(j)
        else:
            continue

decending_sort = ascending_sort
decending_sort.reverse()

#降序排列
list_4 = []
for i in decending_sort:
    for j in list_price:
        if  j[1] == i:
            list_4.append(j)
        else:
            continue

temp = input("输入排序方式(价格升序:1;价格降序:2)")
if temp == "1":
    print("升序排列")
    for i in range(10):
        print(list_3[i])
elif temp == "2":
    print("降序排列")
    for i in range(10):
        print(list_4[i])
else:
    pass