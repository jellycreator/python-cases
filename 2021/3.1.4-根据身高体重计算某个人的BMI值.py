def bmi(height='',weight=''):
    bmi = weight / height**2
    if bmi < 18.5:
        return '过轻'
    elif 18.5 <= bmi <= 23.9:
        return '正常'
    elif 24 <= bmi <= 27:
        return '过重'
    elif 28 <= bmi <= 32:
        return '肥胖'
    elif bmi < 32:
        return '非常肥胖'
print('您',bmi(182,62))