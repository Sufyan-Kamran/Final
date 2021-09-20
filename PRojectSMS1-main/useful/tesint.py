import pymysql
import pandas as pd
import csv
import tkinter as tk
from tkinter import *
def data():    
    con10 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur11 = con10.cursor()
    cur11.execute("select * from products where Defected > 0 Limit 100000")
    row11 = cur11.fetchall()
    abc = []
    Ditems = []
    DEfecte = []
    for row11 in row11:
        a = int(row11[2]) 
        b = int(row11[5])
        c = int(a * b)
        DEfecte.append(c)
        Ditems.append(row11[1])
        abc.append(c)
    


    con2 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur2 = con2.cursor()
    cur2.execute("select * from products where Defected > 0 Limit 100000")
    row6 = cur2.fetchall()
    abc = []
    items = []
    DEfecte = []
    for ro6 in row6:
        i = 0
        a = int(ro6[2]) 
        b = int(ro6[5])
        c = int(a * b)
        DEfecte.append(c)
        items.append(ro6[1])
        abc.append(c)
    ap = []
    ap.append(sum(DEfecte))
    cur2.execute("select * from products")
    row9 = cur2.fetchall()
    PQTY = []
    PPRICE = []
    TDefect = []
    totalDefected =[]
    for ro9 in row9:
        i = 0
        if ro9[5] > "":
            tDefect = int(ro9[5])
            TDefect.append(tDefect)
        a = int(ro9[2]) 
        b = int(ro9[4])
        c = int(a * b)
        
        PPRICE.append(c)

    totalDefected.append(sum(TDefect))
    PQTY.append(sum(PPRICE))
    totalSTk= []
    cur2.execute("select * from products")
    row7 = cur2.fetchall()
    for r in row7:
        totalSTk.append(r[4])
    totalstock = []
    totalstock.append(sum(totalSTk))
    con2 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur2 = con2.cursor()
    
    cur2.execute("select * from orders where Order_date between '2021-08-20' AND '2021-08-22'")
    row2 = cur2.fetchall()
    totals = []
    sale = []
    items = []
    item = []
    profit = []
    totalprofit = []
    totalpro = []
    
    for ro2 in row2:
        c = ro2[5]
        b = ro2[6]
        a = ro2[5]*ro2[8]
        totals.append(b)
        profit.append(a)
        totalprofit.append(c)
    sale.append(sum(totals))
    item.append(sum(totalprofit))
    bc = sale[0]-sum(profit)
    totalpro.append(bc)
    print(sum(totals))
    print(sum(profit))
    con2.commit()
    con2.close
    
    

    from csv import DictWriter
    field_names = ['Total Sale']
    dict={'Total Sale':'This is computer generated report.'}
    dict1={'Total Sale':f'Total sale is : Rs {sale[0]}'}
    dict2={'Total Sale':f'Total Sold items quantity is : Rs {item[0]}'}
    dict3={'Total Sale':f'Total profit of is : Rs {totalpro[0]}'}
    dict4={'Total Sale':f'Total items quantity which are available in stock is : Rs {totalstock[0]}'}
    dict5={'Total Sale':f'Total amount of all items which are currently available in stock is : Rs {PQTY[0]}'}
    dict6={'Total Sale':f'Defected items total lose which worth is : Rs {ap[0]}'}
    listToStr = ' , '.join([str(element) for element in Ditems ])  
    dict7={'Total Sale':f'Defected items : {listToStr}'}
    dict8 ={'Total Sale':f'Defected items : {totalDefected[0]}'}
    with open('Report1.csv', 'w') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
        dictwriter_object.writerow(dict)
        dictwriter_object.writerow(dict1)
        dictwriter_object.writerow(dict2)
        dictwriter_object.writerow(dict3)
        dictwriter_object.writerow(dict4)
        dictwriter_object.writerow(dict5)
        dictwriter_object.writerow(dict6)
        dictwriter_object.writerow(dict7)
        dictwriter_object.writerow(dict8)
        f_object.close()
    ac = {'Total Sale':sale,'Sale Item':item,'Total Profit': totalpro,'Total Stock':totalstock,'Stock Price ':PQTY ,'Defected Lose': ap,'Defected Items': Ditems,'Defected Worth': abc,'Total Defecteed QTY':totalDefected}
    df = pd.DataFrame.from_dict(ac, orient='index')
    df = df.transpose()
    #df.to_csv(r'Report.csv')
    df.to_csv('Report1.csv', mode='a', index=False, header=True)
    print(df)
    print(listToStr)
    
    
    from csv import DictWriter
    ac = {'Total Sale':sale,'Sale Item':item,'Total Profit': totalpro,'Total Stock':totalstock,'Stock Price ':PQTY ,'Defected Lose': ap,'Defected Items': Ditems,'Defected Worth': abc,'Total Defecteed QTY':totalDefected}
    df = pd.DataFrame.from_dict(ac, orient='index')
    df = df.transpose()
    #df.to_csv(r'Report.csv')
    df.to_csv('Report2.csv', mode='w', index=False, header=True)
    field_names = ['Total Sale']
    dict={'Total Sale':'This is computer generated report.'}
    dict1={'Total Sale':f'Total sale is : Rs {sale[0]}'}
    dict2={'Total Sale':f'Total Sold items quantity is : Rs {item[0]}'}
    dict3={'Total Sale':f'Total profit of is : Rs {totalpro[0]}'}
    dict4={'Total Sale':f'Total items quantity which are available in stock is : Rs {totalstock[0]}'}
    dict5={'Total Sale':f'Total amount of all items which are currently available in stock is : Rs {PQTY[0]}'}
    dict6={'Total Sale':f'Defected items total lose which worth is : Rs {ap[0]}'}
    listToStr = ' , '.join([str(element) for element in Ditems ])  
    dict7={'Total Sale':f'Defected items : {listToStr}'}
    dict8 ={'Total Sale':f'Defected items : {totalDefected[0]}'}
    with open('Report2.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
        dictwriter_object.writerow(dict)
        dictwriter_object.writerow(dict1)
        dictwriter_object.writerow(dict2)
        dictwriter_object.writerow(dict3)
        dictwriter_object.writerow(dict4)
        dictwriter_object.writerow(dict5)
        dictwriter_object.writerow(dict6)
        dictwriter_object.writerow(dict7)
        dictwriter_object.writerow(dict8)
        f_object.close()
    
    print(df)
    print(listToStr)
data()  