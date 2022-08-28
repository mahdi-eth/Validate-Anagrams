def validator(*word):
    state = 1
    result = []
    for item in word:
        if(sorted(word[state - 1].lower()) != sorted(word[state].lower())):
            result = False
        else:
            result.append([word[state-1],word[state]])
        if state < word.count(item):
            state += 1
        else:
            state = 0
    print(result)


validator("hamid", "HAdim", "MAHDI")
validator("man", "woman")
validator("hi", "ih")
validator("man", "nam", "amn","nma","anm","mna")
validator("mmd", "mammad","jack")






# def validator2(word1, word2):
#     return sorted(word1.lower()) == sorted(word2.lower())

# print(validator2("HAdim", "MAHDI"))
