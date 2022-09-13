print("华东地区(01)  华南地区(02)  华北地区(03)")
adress = input("请输入地区编号:")
weight = input("请输入重量(kg):")

#判断重量是否是小数,是则返回True,否则返回False
def judgement(temp = ""):
    if float(temp) - int(float(temp)) != 0:
        return True
    else:
        return False

def fare(adress="", weight=""):
    if float(weight) <= 2:
        if adress == "01":
            return 13
        elif adress == "02":
            return 12
        elif adress == "03":
            return 14
        else:
            return "不存在这个地区或重量输入错误"
    else:
        if adress == "01":
            if judgement(weight) == True:
                return 13 + (int(float(weight)) - 1) * 3
            else:
                return 13 + (float(weight) - 2) * 3
        elif adress == "02":
            if judgement(weight) == True:
                return 12 + (int(float(weight)) - 1) * 2
            else:
                return 12 + (float(weight) - 2) * 2
        elif adress == "03":
            if judgement(weight) == True:
                return 14 + (int(float(weight)) - 1) * 4
            else:
                return 14 + (float(weight) - 2) * 4
        else:
            return "不存在这个地区或重量输入错误"
print("邮费为",fare(adress,weight),"元")