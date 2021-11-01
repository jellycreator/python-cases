#价格数组
list_price = [[1, 399], [2, 4369], [3, 539], [4, 288], [5, 109], [6, 749], [7, 235], [8, 190], [9, 99], [10, 1000]]

max_price = input("请输入最大价格:")
min_price = input("请输入最小价格:")
sort_price = input("输入排序方式(价格升序:1;价格降序:2):")


def sort_ad(max_price,min_price,sort_price):
    #最大值是否可以转整型的判断
    try:
        float(max_price)
        max_price = int(max_price)
    except ValueError:
        max_price = 10000000

    #最小值是否可以转整型的判断
    try:
        float(min_price)
        min_price = int(min_price)
    except ValueError:
        min_price = 0

    list_1 = [] #价格列表
    for i in list_price:
        list_1.append(i[1])
    
    ascending_sort = sorted(list_1) #升序排列列表
    
    #升序选择
    if sort_price == "1":
        list_2 = []
        for i in ascending_sort:
            for j in list_price:
                if  j[1] == i and j[1] <= max_price and j[1] >= min_price:
                    list_2.append(j)
                else:
                    continue
        print("升序排列")
        for i in range(len(list_2)):
            print(list_2[i])

    decending_sort = ascending_sort #降序列表克隆
    decending_sort.reverse() #对降序列表元素反转
    
    #降序选择
    if sort_price == "2":
        list_3 = []
        for i in decending_sort:
            for j in list_price:
                if  j[1] == i and j[1] <= max_price and j[1] >= min_price:
                    list_3.append(j)
                else:
                    continue
        print("降序排列")
        for i in range(len(list_3)):
            print(list_3[i])
    
    else:
        pass

sort_ad(max_price,min_price,sort_price)