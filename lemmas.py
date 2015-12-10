__author__ = 'IrinaPavlova'

import os, codecs
from math import log
from pymystem3 import Mystem


mystem = Mystem()


def f(file):
    newtext = list()
    o = codecs.open('./texts/'+file, 'r', encoding='cp1251')
    o = o.read()
    text = o.split()
    for i in text:
        if i not in r'.?!()".-':
            i = mystem.lemmatize(i)[0]
            newtext.append(i)
            n = codecs.open('./newtexts/'+file, 'w', encoding='utf-8')
            texttw = ' '.join(newtext)
            n.write(texttw)
    return newtext

unique = []

for root, dirs, files in os.walk('./texts'):
    N = len(files)
    for name in files:
        if name.endswith('.txt'):
            f(name)


for root, dirs, files in os.walk('./newtexts'):
    N = len(files)
    for name in files:
        t = codecs.open('./newtexts/'+name, 'r', encoding='utf-8')
        t = t.read()
        t = t.split()
        for el in t:
            if el not in unique:
                unique.append(el)


idf = {}
for lemm in unique:
    df = 0
    for root, dirs, files in os.walk('./newtexts'):
        for name in files:
            o = codecs.open('./newtexts/'+name, 'r', encoding='utf-8')
            o = o.read()
            if lemm in o:
                df += 1
    if df is not 0:
        idf[lemm] = log(N/df)

# print(idf)

tfidf = {}
for lemm in idf:
    for root, dirs, files in os.walk('./newtexts'):
        for name in files:
            q = codecs.open('./newtexts/'+name, 'r', encoding='utf-8')
            q = q.read()
            q = q.split()
            s = q.count(lemm)
            #print(s)
            tfidf[lemm+ '_'+name] = s*idf[lemm]


print(sorted(tfidf, key=tfidf.get, reverse=True)[10])
