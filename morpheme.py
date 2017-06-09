# -*- coding: utf-8 -*-
import glob
import os
'''
1. 현재 폴더에 있는 모든 텍스트 파일(*.txt)에 대해

1) 각 파일들에 대해 "파일명 -- 문자수/단어수/라인수" 출력

2) 최종적으로 모든 파일에 대해 "Total -- 문자수/단어수/라인수" 출력

3) 현재 폴더명에 대해서는 그 폴더에 있는 각 파일들에 대해 "파일명 -- 문자수/단어수/라인수"를 출력하고,
   또한 "폴더명 --  문자수/단어수/라인수" 출력

2. 현재 폴더 및 각 sub 폴더에 있는 모든 *.txt 파일들을 하나의 파일, all.txt로 출력하는 프로그램 작성하는데 이 때 한 라인에 word를 하나씩 출력하도록 하시오.
'''
t_char = 0
t_word = 0
t_line = 0

# 텍스트 파일의 문자/단어/라인 count하는 프로그램
# 문자 카운트
def charcount(filename):
    f = open(filename)
    text = f.read()
    f.close()
    return len(text)  # string length

# 단어 카운트
def wordcount(filename):
    f = open(filename)
    text = f.read()
    f.close()
    a = text.split()
    return len(a)

# 라인 카운트
def linecount(filename):
    f = open(filename)
    lines = f.readlines()
    n = 0
    for line in lines:
        n = n + 1
    f.close()
    return n

# 파일 서치
def search(dirname):
    flist = os.listdir(dirname)
    for f in flist:
        next = os.path.join(dirname, f)
        if os.path.isdir(next):
            search(next)
        else:
            doFileWork(next)

def doFileWork(filename):
    ext = os.path.splitext(filename)[-1]
    if ext == '.txt':
        print("-----", filename, "-----")
        print("char :", charcount(filename))
        print("word :", wordcount(filename))
        print("line :", linecount(filename))
        global t_char, t_word, t_line
        t_char += charcount(filename)
        t_word += wordcount(filename)
        t_line += linecount(filename)

search(os.getcwd() + "\KLT2010-TestVersion-2017\EXE")

'''
path = 'C:\sdks/*.txt'
files=glob.glob(path)
for file in files:
    #f=open(file, 'r')
    print("-----",file,"-----")
    print("char :", charcount(file))
    print("word :", wordcount(file))
    print("line :", linecount(file))
    t_char += charcount(file)
    t_word += wordcount(file)
    t_line += linecount(file)
    #print '%s' % f.readlines()
    #f.close()
'''
#print("-----Total-----")
#print("Total char :", t_char)
#print("Total word :", t_word)
#print("Total line :", t_line)