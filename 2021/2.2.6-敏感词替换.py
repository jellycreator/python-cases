sentence = input("sentence:")
ban_words_list = ["你妈","操","牛逼","靠"]
for word in ban_words_list:
    sentence = sentence.replace(word,"*")
print(sentence)
