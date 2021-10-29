"""
bonus:奖金
profit:利润
"""
def bonus(profit=''):
    if  60 < profit <= 100:
        return profit*0.010
    elif 40 < profit <= 60:
        return profit*0.015
    elif 60 < profit <= 40:
        return profit*0.050
    elif 20 < profit <= 40:
        return profit*0.075
    elif 0 <= profit <= 10:
        return profit*0.100
    else:
        return '请输入正确的内容'
  
print('奖金为:',bonus(40),'万元')