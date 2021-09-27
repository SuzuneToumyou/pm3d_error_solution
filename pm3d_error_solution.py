#!/usr/bin/python3
# -*- coding: utf-8 -*

import csv

f = open('./input.csv','r')
fout=open("./output.csv" ,"w")
reader = csv.reader(f)

tmp = 0

writer = csv.writer(fout)

for row in reader:
    mylist=[]
    if tmp == row[0]:
        mylist.append([row[0],row[1],row[2]])
        writer.writerows(mylist)
        #print(row)
    
    elif  tmp != row[0]:
        writer.writerows([""])
        mylist.append([row[0],row[1],row[2]])
        writer.writerows(mylist)
        #print("\n")

    tmp = row[0]

f.close()
fout.close()
