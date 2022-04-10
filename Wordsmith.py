from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import os
import phonetics as ph

#
# with open(f"{cwd}\inspiration\{dataroot[0]}").read().replace('\n', '. ') as file:
#     print(file)
cwd = os.getcwd()
dataroot = os.listdir(cwd + "\inspiration")

sentData = []

for i in range(0, len(dataroot)):
    data2 = open(f"{cwd}\inspiration\{dataroot[i]}").read().replace('\n', '. ')
    sentData.append(sent_tokenize(data2))

print(sentData[2])
print("test: ", ph.dmetaphone("Take"))
print("test2: ", ph.dmetaphone("Bake"))



