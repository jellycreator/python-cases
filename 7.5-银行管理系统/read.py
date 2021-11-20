import os,sys

freeze_dict = {'8888':1 ,'7777':2}
p = sys.path[0]
# os.sep 是系统分隔符
with open(p + os.sep + 'freeze_dict_keys.txt', 'w', encoding='utf-8') as file:
    for i in freeze_dict.keys():
        file.write(i+'\n')
with open(p + os.sep + 'freeze_dict_values.txt', 'w', encoding='utf-8') as file:
    for i in freeze_dict.values():
        file.write(str(i)+'\n')


with open(p + os.sep + 'freeze_dict_keys.txt', 'r', encoding='utf-8') as file:
    freeze_dict_keys = []
    for line in file.readlines():
        line = line.replace('\n','')
        if line != '':
            freeze_dict_keys.append(line)
        else:
            continue
    print(freeze_dict_keys)

with open(p + os.sep + 'freeze_dict_values.txt', 'r', encoding='utf-8') as file:
    freeze_dict_values = []
    for line in file.readlines():
        line = line.replace('\n','')
        if line != '':
            freeze_dict_values.append(int(line))
        else:
            continue
    print(freeze_dict_values)

index = 0
while True:
    try:
        freeze_dict[freeze_dict_keys[index]] = freeze_dict_values[index]
        index += 1
    except:
        break
