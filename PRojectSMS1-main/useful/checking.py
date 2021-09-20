from datetime import datetime
from PIL.Image import MODES
import pymysql
import pandas as pd
import csv
def Report():
    con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur = con.cursor()
    cur.execute("select * from orders where Order_date between %s AND %s",(a.get(),b.get()))

    row = cur.fetchall()
    con.commit()
    con.close
    c= []
    sums = 0
    qty =0
    for ro in row:
        sums = sums + ro[6]
        qty = qty + ro[5]
    totalsale = []
    totalsale.append(sums)
    totalqty = []
    totalqty.append(qty)
    #print("Total Sale is " , sums)
    #print("Total Sales Units is " , qty)
    con2 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur2 = con2.cursor()
    cur2.execute("select * from orders where Order_date between %s AND %s",(ad.get(),bd.get()))
    

    row10 = cur2.fetchall()
    POS = []
    for ro10 in row10:
        i = 0
        aa = int(ro10[8]) 
        ba = int(ro10[5])
        ca = int(aa * ba)
        POS.append(ca)
    TotalProfit = []
    TotalProfit.append(sum(POS))
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
    for ro9 in row9:
        i = 0
        a = int(ro9[2]) 
        b = int(ro9[4])
        c = int(a * b)
        PPRICE.append(c)
    PQTY.append(sum(PPRICE))
    totalSTk= []
    cur2.execute("select * from products")
    row7 = cur2.fetchall()
    for r in row7:
        totalSTk.append(r[4])
    totalstock = []
    totalstock.append(sum(totalSTk))
    a = {'Defected Items': items,'Lose': abc,'Total Sale':totalsale,'Sale Item':totalqty,'Total Stock':totalstock,'Total Stock Value': PQTY,'Total Profit': TotalProfit,'Total Lose':ap,}
    df = pd.DataFrame.from_dict(a, orient='index')
    df = df.transpose()
    df.to_csv(r'Report.csv')
    print(df)


def Monthly():
    
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m')
    con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur = con.cursor()
    asa = input("enter date : ")
    cur.execute("select * FROM `orders` WHERE date =%s ;",(formatted_date))
    row = cur.fetchall()
    con.commit()
    con.close
    c= []
    sums = 0
    qty =0
    for ro in row:
        sums = sums + ro[6]
        qty = qty + ro[5]
    totalsale = []
    totalsale.append(sums)
    totalqty = []
    totalqty.append(qty)
    #print("Total Sale is " , sums)
    #print("Total Sales Units is " , qty)
    con2 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur2 = con2.cursor()
    
    cur2.execute("select * FROM `orders` WHERE date =%s ;",(formatted_date))
    row10 = cur2.fetchall()
    POS = []
    for ro10 in row10:
        i = 0
        aa = int(ro10[8]) 
        ba = int(ro10[5])
        ca = int(aa * ba)
        POS.append(ca)
    TotalProfit = []
    TotalProfit.append(sum(POS))
    con2 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur2 = con2.cursor()
    cur2.execute("select * from products where Defected > 0 Limit 100000 ")
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
    for ro9 in row9:
        i = 0
        a = int(ro9[2]) 
        b = int(ro9[4])
        c = int(a * b)
        PPRICE.append(c)
    PQTY.append(sum(PPRICE))
    totalSTk= []
    cur2.execute("select * from products")
    row7 = cur2.fetchall()
    for r in row7:
        totalSTk.append(r[4])
    totalstock = []
    totalstock.append(sum(totalSTk))
    a = {'Defected Items': items,'Lose': abc,'Total Sale':totalsale,'Sale Item':totalqty,'Total Stock':totalstock,'Total Stock Value': PQTY,'Total Profit': TotalProfit,'Total Lose':ap,}
    df = pd.DataFrame.from_dict(a, orient='index')
    df = df.transpose()
    #asaaa=(SELECT MONTH (Order_date) month, COUNT(Id) Product_Sold FROM orders GROUP BY MONTH (Order_date) ORDER BY MONTH (Order_date);)
    df.to_csv(r'Report.csv')
    print(df)
Report()
