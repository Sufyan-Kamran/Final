import pymysql
import pandas as pd
import csv
con = pymysql.connect(host="localhost", user="root", password="", database="employee" )

con2 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
cur2 = con2.cursor()
cur2.execute("select * from orders")
row2 = cur2.fetchall()
for ro2 in row2:
    a = ro2[3]
    #print(ro2[3])
con.commit()
con.close
cur = con.cursor()
cur.execute("select * from products where Pid=%s",(a))
row = cur.fetchall()
for ro in row:
    pass
    print(ro[2])
con.commit()
con.close
ab = input("ENTER NUMBER : ")
cur3 = con.cursor()
cur3.execute("select * from products where Pid=%s",(ab))
row3 = cur3.fetchall()
for ro3 in row3:
    a = ro3[7]
    print(ro3[7])
con.commit()
con.close

cur4 = con.cursor()
cur4.execute("insert into orders(Buying_Rate) value(%s)",(a))
row4 = cur4.fetchall()
for ro4 in row4:
    a4 = ro4[8]
    #print(ro4[8])
con.commit()
con.close





