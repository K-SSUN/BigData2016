# -*- coding: utf-8 -*-
import os
import glob
import math
import numpy as np

def file_copy():
    i=1
    path = os.getcwd() + "\\ITnews\\"
    flist=glob.glob(path+"*.txt") # 파일 이름 포함 전체 경로
    os.system("mkdir docs")
    for fname in flist:
        # 모든 파일을 docs/i.txt로 복사
        os.system("copy " + fname + " "+ os.getcwd() +"\\docs\\" + "%d" %i + ".txt")
        i = i+1

def each_morpheme():
    path = os.getcwd() +"\\docs\\"
    flist = os.listdir(path)
    os.system("mkdir result")
    move_path = os.getcwd() + "\\result\\"

    num = 1
    for f in flist:
        os.system(os.getcwd() +"KLT2010-TestVersion-2017\\EXE\\index.exe -sw " + path + f + " TLIST_"
                  + str(num) + ".txt")
        os.system('move' + " TLIST_" + str(num) + ".txt " + move_path)
        num+=1

def wordcount_df():
    path = os.getcwd() + "\\result\\"
    flist = os.listdir(path)
    os.system("mkdir output")

    for fname in flist:
        os.system("wordcount.exe -new -1 " + path + fname +
                  " " + os.getcwd() + "\\output\\" + fname)

def wordcount_freq():
    os.system("mkdir freq")
    path = os.getcwd() +"\\docs\\"
    flist = os.listdir(path)

    for fname in flist:
        os.system("wordcount.exe -0 " + path + fname +
                  " " + os.getcwd() + "\\freq\\" + fname)

def idf(word, id_list):
    for term in id_list:
        if term[1] == word:
            return float(term[3])

def similarity_di_dj(num1, num2, id_list):
    print = "calculate similarity " + "%d" %int(num1) + ".txt" + " %d"%int(num2) + ".txt"
    di_file = open(os.getcwd() + "\\freq\\" + "%d" % int(num1) + ".txt", "r")
    dj_file = open(os.getcwd() + "\\freq\\" + "%d" % int(num2) + ".txt", "r")

    lines = di_file.read().split('\n')
    lines = lines[:-1] # remove last null line

    di_list = []
    for i in id_list:
        count_line = 0
        for j in lines:
            new_list = j.split('\t')
            if i[1] == new_list[1]:
                w = idf(new_list[1], id_list)
                if w == None:
                    w = 0
                di_list.append((new_list[1], int(new_list[0]) * w))
                break
            count_line += 1

        if count_line == len(lines):
            di_list.append((i[1], 0))
    di_file.close()

    lines = dj_file.read().split('\n')
    lines = lines[:-1] # remove last null line

    dj_list = []
    for i in id_list:
        count_line = 0
        for j in lines:
            new_list = j.split('\t')
            if i[1] == new_list[1]:
                w = idf(new_list[1], id_list)
                if w == None:
                    w = 0
                dj_list.append((new_list[1], int(new_list[0]) * w))
                break
            count_line += 1

        if count_line == len(lines):
            dj_list.append((i[1], 0))
    dj_file.close()

    # 벡터 내적 / di 크기 / dj 크기
    v = 0
    di = 0
    dj = 0
    for  i in range(len(id_list)):
        v = v + di_list[i][1]*dj_list[i][1]
        di = di + math.pow(di_list[i][1], 2)
        dj = dj + math.pow(dj_list[i][1], 2)
    di = math.sqrt(di)
    dj = math.sqrt(dj)

    print("v = " + str(v))
    print("di = " + str(di))
    print("dj = " + str(dj))
    print("similarity = " + str(v / (di * dj)))

def make_upper(num_f, id_list):
    m = [[0 for col in range(num_f)] for row in range(num_f)]
    for i in range(num_f):
        for j in range(i, num_f):
            if i == j :
                m[i][j] = 1
            else:
                similarity_di_dj(i+1, j+1, id_list)

    m = np.triu(m, k = 0)

path = os.getcwd() + "\\docs\\"
flist=glob.glob(path+"*.txt")
if not flist: # flist가 비어있다면 비어있다면 flist == false
    file_copy()

path = os.getcwd() + "\\result\\"
flist=glob.glob(path+"*.txt")
if not flist:
    each_morpheme()

path = os.getcwd() + "\\output\\"
flist=glob.glob(path+"*.txt")
if not flist:
    wordcount_df()

# TermTable 구축
try:
    data = open("termtable.txt", "r")
except IOError:
    os.system("copy " + os.getcwd() + "\\output\\*.txt all.txt")
    os.system('wordcount.exe -new all.txt termtable.txt')
finally:
    data = open("termtable.txt", "r")

# mapping 및 IDF계산
lines = data.read().split('\n')
lines = lines[:-1] # remove last null line
id_count = 1
id_list = []

num_f = len(flist) # 총 문서 개수 = 418

for i in lines:
    new_list = i.split('\t')

    # TERM ID, TERM, DF, IDF
    id_list.append((id_count, new_list[1], int(new_list[0]), math.log10(num_f / int(new_list[0]))))
    id_count += 1
data.close()

# 각 문서 i에 대한 자질벡터 구성
# tf(ti) = freq(ti) / maxTF --> freq(ti)사용
# 각 문서마다 freq 계산
path = os.getcwd() + '\\freq\\'
flist = glob.glob(path+"*.txt")
if not flist:
    wordcount_freq()

# di dj 유사도 계산
num1 = input("Please enter the txt number\n")
num2 = input("Please enter the outher txt number\n")
similarity_di_dj(num1, num2, id_list)

