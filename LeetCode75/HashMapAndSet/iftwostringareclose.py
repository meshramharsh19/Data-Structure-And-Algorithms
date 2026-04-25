word1 = "abccc"
word2 = "bcaaa"

word11 = list(word1)
word12 = list(word2)
print(word11)


word1hash = {}
word2hash = {}

if len(word11) != len(word12):
    print(False)
else:
    
    for alphrange in range(len(word11)):
        if word11[alphrange] in word1hash:
            word1hash[word11[alphrange]] += 1
        else:
            word1hash[word11[alphrange]] = 1
        if word12[alphrange] in word2hash:
            word2hash[word12[alphrange]] += 1
        else:
            word2hash[word12[alphrange]] = 1

    if set(word1hash.keys()) == set(word2hash.keys()) and sorted(word1hash.values()) == sorted(word2hash.values()):
        print(True)
    else :
        print(False)