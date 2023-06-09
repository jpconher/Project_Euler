# Problem 59

import pandas as pd

cipher = pd.read_csv(".../0059_cipher.txt", sep=",", header=None).values[0].tolist()

# list of very common English words
english_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'it', 'for']

message = {'message':"", 'count_common_words':0}
for st in range(97,122): #ASCII code for a-z
    for nd in range(97,122):
        for rd in range(97,122):
            encription_key = [st,nd,rd]
            i = 0
            candidate = "" 
            for character in cipher:
                candidate += chr(character ^ encription_key[i])
                i += 1
                if i == 3:
                    i = 0
            common_words_n = 0
            for word in candidate.split():
                if word in english_words:
                    common_words_n += 1
            if common_words_n > message['count_common_words']:
                message['message'] = candidate
                message['count_common_words'] = common_words_n

sum_ascii = 0
for c in message['message']:
    sum_ascii += ord(c)