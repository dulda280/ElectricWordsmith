from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import os

#
# with open(f"{cwd}\inspiration\{dataroot[0]}").read().replace('\n', '. ') as file:
#     print(file)
cwd = os.getcwd()
dataroot = os.listdir(cwd + "\inspiration")


for i in range(0, len(dataroot)):
    data2 = open(f"{cwd}\inspiration\{dataroot[i]}").read().replace('\n', '. ')
    print(data2)
    print(sent_tokenize(data2))


