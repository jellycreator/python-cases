import random

while True:
    dict_words = {
        'happy':'开心',
        'sad':'伤心',
        'dictionary':'字典',
        'China':'中国'
    }
    print('\
=============\n\
1.查看生词表\n\
2.背单词\n\
3.添加新单词\n\
4.删除单词\n\
5.清空单词表\n\
6.退出单词本\n\
=============')

    temp = input("")

    if temp =='1':
        if dict_words == {}:
            print('生词本内容为空')
        else:
            for word in dict_words.items():
                print(word)
    elif temp =='2':
        print('进入背单词功能,退出请输入/b')
        while True:
            index = random.randint(0,len(list(dict_words.keys()))-1)
            print(index)
            print(type(index))
            word_cn = input('%s的中文意思是:' % list(dict_words.keys())[index])
            if word_cn == '/b':
                break
            else:
                while True:
                    if word_cn == '/b':
                        break
                    elif word_cn == dict_words[list(dict_words.keys())[index]]:
                        print('太棒了')
                        break
                    else:
                        print('再想想')
                        word_cn = input('%s的中文意思是:' % list(dict_words.keys())[index])
    elif temp =='3':
        pass
    elif temp =='4':
        pass
    elif temp =='5':
        pass
    elif temp =='6':
        break
    else:
        pass
