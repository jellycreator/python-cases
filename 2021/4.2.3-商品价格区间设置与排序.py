#完善代码在4.2.3-商品价格区间设置与排序-plus.py
#生成价格与序号的一维数组
"""
list = [399,4369,539,288,109,749,235,190,99,1000]
list2 = []
num = 1
for i in list:
    list2.append([num,i])
    num += 1
print(list2)
"""
#价格数组
list_price = [[1, 399], [2, 4369], [3, 539], [4, 288], [5, 109], [6, 749], [7, 235], [8, 190], [9, 99], [10, 1000]]
#价格列表
list = []
for i in list_price:
    list.append(i[1])
#print(list)

#这里的max和min只能输入数字,若输入其他类型则会报错
max = int(float(input("请输入最大价格:")))
min = int(float(input("请输入最小价格:")))

#升序排列
ascending_sort = sorted(list)
#print(ascending_sort)
list_3 = []
for i in ascending_sort: #这部分可以封装到函数中
    for j in list_price:
        if  j[1] == i and j[1] <= max and j[1] >= min:
            list_3.append(j)
        else:
            continue

#降序排列
decending_sort = ascending_sort
decending_sort.reverse()
list_4 = []
for i in decending_sort:
    for j in list_price:
        if  j[1] == i and j[1] <= max and j[1] >= min:
            list_4.append(j)
        else:
            continue

temp = input("输入排序方式(价格升序:1;价格降序:2)")
if temp == "1":
    print("升序排列")
    for i in range(len(list_3)):
        print(list_3[i])
elif temp == "2":
    print("降序排列")
    for i in range(len(list_4)):
        print(list_4[i])
else:
    pass