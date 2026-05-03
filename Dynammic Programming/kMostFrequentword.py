words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
wordandcount = {}
for i in range(len(words)):
    if words[i] in wordandcount:
        wordandcount[words[i]] += 1
    else :
        wordandcount[words[i]] = 1

for i in wordandcount:
    pass #code is half done only : complete the code asap