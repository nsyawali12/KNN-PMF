import pandas as pd
import numpy as np


test = ("Hello world!")
project = ("This is my 3rd Project of Artificial Intelligence")
what = ("Project : K-Nearest Neighbors")

print (test)
print (project)
print (what)

dfile1 = pd.read_csv('DataTrain_Tugas3_AI.csv', index_col=False, header=0);
dfile2 = pd.read_csv('DataTest_Tugas3_AI.csv', index_col=False, header=0);

# dfile1 = data file 1 the first import of Train tugas 3
# dfile2 = data file 2 the 2nd import of Test tugas 3

k = 3

def manhattan(x1,x2):
	return np.abs(x1-x2)

#result = hasil
#i,j = counter

i=0
result=[]
for index2, row2 in dfile2.iterrows():
    res2=[]
    #res2 = array ressult 2 untuk datafile 2
    for index1, row1 in dfile1.iterrows():
        res=0
        for j in range(5):
            res+=(manhattan(row2[j+1],row1[j+1]))
        res2.append({'kelas':row1[6],'jarak':res})
    res2.sort(key=lambda k : k['jarak'])
    kkelas={}
    for j in range(k):
        if res2[j]['kelas'] in kkelas:
            kkelas[res2[j]['kelas']]+=1
        else:
            kkelas[res2[j]['kelas']]=1

    result.append('%g'%(max(kkelas, key=kkelas.get)))


export_hasil = pd.DataFrame(result)
export_hasil.to_csv("K_Tebakan_Tugas3.csv", encoding="utf-8", index=False, header=False);