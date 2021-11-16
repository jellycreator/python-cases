infordict =  open(r"7.5-银行管理系统\bank_information_dict.py", mode='r', encoding='utf-8')
a = infordict.read()
print(type(a))
infordict.close()