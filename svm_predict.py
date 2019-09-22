import pandas as pd
import xlrd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
#from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.datasets import make_classification
x_train=[]
y_train=[]


data=xlrd.open_workbook(r"C:\VIT HACK\train.xlsx")
sheet = data.sheet_by_index(0) 
sheet.cell_value(0, 0) 
skip=0
for i in range(1,sheet.nrows):
    row=[]
    try:
        for j in range(1,sheet.ncols-1):
            row.append(float(sheet.cell_value(i, j)))
    except:
        skip+=1
        continue
    x_train.append(row)
    y_train.append(float(sheet.cell_value(i, 13)))
        



clf = SVC(gamma='auto')
clf.fit(x_train,y_train) 

skip=0
x_test=[]
data1=xlrd.open_workbook(r"C:\VIT HACK\train.xlsx")
sheet1 = data.sheet_by_index(0) 
sheet1.cell_value(0, 0) 
company_names=[]
for i in range(1,sheet1.nrows): 
    row=[]
    try:
        for j in range(1,sheet1.ncols-1):
            row.append(float(sheet.cell_value(i, j)))
    except:
        skip+=1
        continue
    x_test.append(row)
    company_names.append(sheet.cell_value(i, 0))


    
y_test=clf.predict(x_test)
for comp,res in zip(company_names,y_test):
    print(comp,": ",res)

y_prec=clf.predict(x_train) 

print((1-np.sum(abs(np.array(y_prec)-np.array(y_train)))/len(y_train))*100)




#x=["CMP Rs.",]
#y=
#y=data.temp
#x=data.drop('temp',axis=1)
#x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
#print(len(x_test))