import pymysql
import pandas as pd
def Report():
    
    con10 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur11 = con10.cursor()
    cur11.execute("select * from products where Defected > 0 Limit 100000")
    row11 = cur11.fetchall()
    abc = []
    items = []
    DEfecte = []
    for row11 in row11:
        a = int(row11[2]) 
        b = int(row11[5])
        c = int(a * b)
        DEfecte.append(c)
        items.append(row11[1])
        abc.append(c)
    
    a = {'Defected Items': items,'Lose': abc}
    df = pd.DataFrame.from_dict(a, orient='index')
    df = df.transpose()
    df.to_csv(r'Report.csv')
    print(df)
Report()