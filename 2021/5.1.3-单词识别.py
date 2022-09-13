#功能不全,没用字典树做
key_dict = {'mo':'Monday','tu':'Tuesday','we':'Wednesday','th':'Thursday','fr':'Friday','sa':'Saturday','su':'Sunday'}
key_dict2 = {'m':'Monday','t':"'Tuesday','Thursday'",'w':'Wednesday','f':'Friday','s':"'Saturday','Sunday'"}
temp = input('输入两个字母')
try:
    try:
        print(key_dict[temp])
    except:
        print(key_dict2[temp])
except:
    pass