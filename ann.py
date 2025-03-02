import numpy as np
import json
import spacy
import os
from datetime import datetime
import pickle
import time
class Word:
    def key_words(prompt:str):
        doc = nlp(prompt)

        key_words = []
        for token in doc:
            if token.pos_ in ['NOUN', 'VERB', 'ADJ', 'PRON', 'ADV', 'NUM', 'AUX', 'MODAL']:
                key_words.append(token.text)
        return key_words

    def words_in_vector(key_words):
        list_vector = []
        for i in key_words:
            vector_key = nlp(i).vector
            list_vector.append(vector_key)
        return list_vector

class VIP(Word):
    def pad_array(arr):
        arr = np.array(arr)
        #assert np.shape(arr)==(None, 96)
        mean_value = np.mean(arr)
        padded_arr = np.hstack([arr, mean_value * np.ones((arr.shape[0], 4))])
        return padded_arr

nlp = spacy.load('en_core_web_sm')
dir = '/home/evstigneva/rar/evstigneva/annotations/'
listing = np.empty(2000000, dtype = object)
a1 = 0

np.save('ann_all.npy', listing)
for i in os.listdir(dir):
    print(i)
    if 'json' in i:
        dict = json.load(open(f'{dir}{i}'))
        for r in dict:
            if r=='annotations':
                for i in dict['annotations']:
                    for d in i:
                        if d=='caption':
                            a1+=1
                            now = datetime.now()
                            print(f'Итерация номер: {a1}')
                            #caption = Word.key_words(i['caption'])
                            #caption = Word.words_in_vector(caption)
                            #array[i['image_id']] = VIP.pad_array(caption)
                            #if i['caption'] not in listing:
                            #    listing[i['image_id']] = i['caption']
                            listing[a1] = i['caption']

                            print(f'Время перевода в вектор: {datetime.now()-now}')
#np.save('ann_all.npy', array)
np.save('ann_all.npy', listing)

ann = np.load('/home/evstigneva/proda/ann_all.npy', allow_pickle=True)

print(np.shape(ann))