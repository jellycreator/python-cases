# 1
print('{0:#^20}'.format(input()))

# 数字检测
def isNumber(value):
    import re

    matchList = []
    matchList = re.findall(r'\d+\.?\d+', value)
    if matchList == []:
        return {'error': '数字缺失'}
    elif len(matchList) == 1:
        string = matchList[0]
        if len(value) == len(string):
            if '.' in string:
                return {
                    'ok': {
                        'type': 'float',
                        'value': float(value)
                    }
                }
            else:
                return {
                    'ok': {
                        'type': 'integer',
                        'value': int(value)
                    }
                }
        else:
            return {'error': '非可转换数字类型'}
            
    else:
        return {'error': '数字过多'}

# 2
while True:
    while True:
        hourSalary = input("时薪:")
        res = isNumber(hourSalary)
        if 'error' in res:
            print(res['error'])
            continue
        hourSalary = res['ok']['value']
        if (hourSalary < 0.0):
            print("时薪不得小于零")
            continue
        break

    while True:
        weekWorkTime = input("一周正常工作时长:")
        res = isNumber(weekWorkTime)
        if 'error' in res:
            print(res['error'])
            continue
        weekWorkTime = res['ok']['value']
        if (weekWorkTime > 40.0) | (weekWorkTime < 0.0):
            continue
        break

    while True:
        extraTime = input("加班时长:")
        res = isNumber(extraTime)
        if 'error' in res:
            print(res['error'])
            continue
        extraTime = res['ok']['value']
        if (extraTime < 0.0) | ():
            continue
        break

    Salary = hourSalary*weekWorkTime+(extraTime*hourSalary)*1.5
    t = extraTime +weekWorkTime
    if (48.0 <= t < 60.0):
        print(Salary*1.2)
    elif (60.0 <= t < 80.0):
        print(Salary*2)
    elif (80.0 <= t):
        print(Salary*3)
    else:
        print(Salary)



