import random

dict_words = {
'happy':'开心',
'sad':'伤心',
'dictionary':'字典',
'China':'中国'
    }

while True:
    print('\
=============\n\
1.查看生词表\n\
2.背单词\n\
3.添加新单词\n\
4.删除单词\n\
5.清空单词表\n\
6.退出单词本\n\
=============')

    temp = input("您的操作是:")

    if temp =='1':
        if dict_words == {}:
            print('生词本内容为空')
        else:
            for word in dict_words.items():
                print(word)

    elif temp =='2':
        if dict_words == {}:
            print('生词本内容为空')
        else:
            print('进入背单词功能,退出请输入/b')
            while True:
                index = random.randint(0,len(list(dict_words.keys()))-1)
                word = list(dict_words.keys())[index]
                while True:
                    word_cn = input('%s的中文意思是:' % word)
                    if word_cn == '/b':
                        break
                    elif word_cn == dict_words[word]:
                        print('太棒了')
                        break
                    else:
                        print('再想想')
                        continue
                if word_cn == '/b':
                    break
    
    elif temp =='3':
        print('进入添加单词功能,退出请输入/b')
        while True:
            new_word = input('请输入要添加的单词:')
            if new_word == '/b':
                break
            elif new_word == '':
                print('请输入单词')
            elif new_word in list(dict_words.keys()):
                print('该单词已存在')
            else:
                transword = input('请输入该单词的意思:')
                dict_words[new_word] = transword
                print('添加成功')
 
    elif temp =='4':
        print('进入添加单词功能,退出请输入/b')
        while True:
            for word in dict_words.items():
                print(word)
            del_word = input('请输入要删除的单词:')
            if del_word == '/b':
                break
            elif del_word not in list(dict_words.keys()):
                print('删除的单词不存在')
            else:
                dict_words.pop(del_word)
                print('删除成功')

    elif temp =='5':
        try:
            dict_words.clear()
            print('生词本已清空')
        except:
            print('生词本为空')

    elif temp =='6':
        break

    else:
        pass