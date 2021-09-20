from datetime import datetime
import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import font
from tkinter.font import BOLD
from tkinter import messagebox
import re
import pymysql
from tkinter import ttk
from PIL import Image, ImageTk

######################################### Section1 #######################################################

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return
def admin():
    if usernameEntry.get() == "ADMIN" or passwordEntry.get() == "Admin@001":
        root2.destroy()
        import treeVie

def reset():
    try:
        usernameEntry.delete(0,'end')
        passwordEntry.delete(0, 'end')   	
    except Exception as e:
            messagebox.showerror("Error",e)
def passchk():
    passwd = passwordEntry.get()
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat = re.compile(reg)   
    mat = re.search(pat, passwd)
    if mat:
        print("Password is valid.")
    else:
        messagebox.showerror("ERROR", "Password must contain Special character, numbers or capital letters")
def empty():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror("ERROR", "All fields are required")
def loginPage():
    frame = Frame(root2,width=1400, height=800,)
    frame.place(x=0,y=0)
    fk = Frame(frame,width=1400,height=70,bg="gray4")
    fk.place(x=0,y=0)    
    HistL = Label(frame,text="Products",font=("calibri",18,"bold"),fg="gray4")
    HistL.place(x=10,y=80)
    con4 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur4 = con4.cursor()
    cur4.execute("select * from products")
    row4 = cur4.fetchall()
    treeview3 =ttk.Treeview(frame,height=700)
    treeview3["columns"]= ("PId","P_Name","Price","Category")
    treeview3["show"]="headings"
    s = ttk.Style(root)
    s.theme_use("vista")
    s.configure(".", font=('times new roman', 11))
    s.configure("treeview3.Heading", foreground="BLUE", font=("times new roman", 14, "bold"))
    treeview3.column('PId', width=5, minwidth=5,anchor=tk.CENTER)
    treeview3.column('P_Name', width=30, minwidth=20,anchor=tk.CENTER)
    treeview3.column('Price', width=30, minwidth=30,anchor=tk.CENTER)
    treeview3.column('Category', width=30, minwidth=30,anchor=tk.CENTER)

################################## Adding heading #####################################################

    treeview3.heading('PId', text='PId', anchor=CENTER)
    treeview3.heading('P_Name', text='P_Name', anchor=CENTER)
    treeview3.heading('Price', text='Price' ,anchor=CENTER)
    treeview3.heading('Category', text='Category' ,anchor=CENTER)    
    treeview3.place(x=10,y=120,width=650,height=400)
    i = 0
    for ro in row4:
        treeview3.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
        i = i+1
    hsb = ttk.Scrollbar(treeview3, orient="vertical")
    hsb.configure(command=treeview3.yview)
    treeview3.configure(yscrollcommand=hsb.set)
    hsb.pack(fill=Y,side=RIGHT)

###########################################################################################################
###########################################################################################################
###########################################################################################################
    ItemsL = Label(frame,text="History",font=("calibri",18,"bold"),fg="gray4")
    ItemsL.place(x=670,y=80)
    con5 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur5 = con5.cursor()
    cur5.execute("select * from orders where name=%s and email=%s",(row[1],row[3]))
    row5 = cur5.fetchall()
    treeview4 =ttk.Treeview(frame,height=700)
    treeview4["columns"]= ("Id","Name","Product","Qty","Bill","Date")
    treeview4["show"]="headings"
    s = ttk.Style(root)
    s.theme_use("vista")
    s.configure(".", font=('times new roman', 11))
    s.configure("treeview4.Heading", foreground="BLUE", font=("times new roman", 14, "bold"))
    #adding columns
    treeview4.column('Id', minwidth=1,anchor=tk.CENTER, stretch=NO, width=50)
    treeview4.column('Name',  minwidth=10,anchor=tk.CENTER, stretch=NO, width=130)
    treeview4.column('Product', width=10, minwidth=10,anchor=tk.CENTER)
    treeview4.column('Qty', minwidth=10,anchor=tk.CENTER, stretch=NO, width=50)
    treeview4.column('Bill', minwidth=10,anchor=tk.CENTER, stretch=NO, width=80)
    treeview4.column('Date', width=10, minwidth=10,anchor=tk.CENTER) 
    #adding heading
    treeview4.heading('Id', text='Id', anchor=CENTER)
    treeview4.heading('Name', text='Name', anchor=CENTER)
    treeview4.heading('Product', text='Product' ,anchor=CENTER)
    treeview4.heading('Qty', text='Qty' ,anchor=CENTER)
    treeview4.heading('Bill', text='Bill' ,anchor=CENTER)
    treeview4.heading('Date', text='Date' ,anchor=CENTER)    
    treeview4.place(x=670,y=120,width=700,height=400)        
    i = 0
    for ro in row5:
        treeview4.insert('',i, text="", values=(ro[0],ro[1],ro[4],ro[5],ro[6],ro[7]))
        i = i+1
    hsb = ttk.Scrollbar(treeview4, orient="vertical")
    hsb.configure(command=treeview4.yview)
    treeview4.configure(yscrollcommand=hsb.set)
    hsb.pack(fill=Y,side=RIGHT)

###################################### LABELS  ###########################################################
    div = Frame(frame,bg="gray4",height=5,width=1400)
    div.place(x=0,y=530)
    userlabe = Label(frame, text="Order Detail",fg = "Green",font=("times new roman", 23))
    userlabe.place(x=10,y=536)
    idlabe = Label(frame, text="Id : ",fg = "blue",font=("times new roman", 15))
    idlabe.place(x=10,y=600)
    Namelabe = Label(frame, text="Name : ",fg="blue",font=("times new roman", 15))
    Namelabe.place(x=10,y=650)
    Emaillabe = Label(frame, text="Email : ",fg="blue",font=("times new roman", 15))
    Emaillabe.place(x=10,y=700)
    pIDlabe = Label(frame, text="Product Id : ",fg="blue",font=("times new roman", 15))
    pIDlabe.place(x=10,y=750)
    Productlabe = Label(frame, text="Produt Name : ",fg="blue",font=("times new roman", 15))
    Productlabe.place(x=450,y=600)
    Pricelabe = Label(frame, text="Price : ",fg="blue",font=("times new roman", 15))
    Pricelabe.place(x=450,y=650)
    Qtylabe = Label(frame, text="Qty : ",fg="blue",font=("times new roman", 15))
    Qtylabe.place(x=450,y=700)
    Pricelabe = Label(frame, text="Total Bill : ",fg="red",font=("times new roman", 15))
    Pricelabe.place(x=450,y=750)
    DId = Label(frame, text="Order Qty : ",fg="red",font=("times new roman", 15))
    DId.place(x=750,y=650)
    Dname = Label(frame, text="Defected Product Name : ",fg="red",font=("times new roman", 15))
    Dname.place(x=750,y=700)
    Dnames = Label(frame, text="Defected Qty : ",fg="red",font=("times new roman", 15))
    Dnames.place(x=750,y=750)
####################################### UPDATE LABELS VALUES ###################################################    

    labe = Label(frame, text="",font=("times new roman", 15))
    labe.place(x=150,y=600)
    labe["text"] = row[0]
    labe1 = Label(frame, text="",font=("times new roman", 15))
    labe1.place(x=150,y=650)
    labe1["text"] = row[1]
    labe2 = Label(frame, text="",font=("times new roman", 15))
    labe2.place(x=150,y=700)
    labe2["text"] = row[3]
    en1 = Entry(frame)
    en1.place(x=600,y=700)
    global pnam_var
    pnam_var = StringVar()
    enk = Entry(frame,textvariable=pnam_var,width=0)
    enk.place(x=600,y=1000)
    # dId = Entry(frame)
    #dId.place(x=900,y=650)
    dNames = Entry(frame)
    dNames.place(x=900,y=750)

    
    def hello():
        try:
            #grab record NUmber 
            selects = treeview3.focus()
            #grab record values
            global value 
            global labe3
            global labe4
            global labe5
            global labe6
            value = treeview3.item(selects,'values')        
            labe3 = Label(frame, text="",font=("times new roman", 15))
            labe3.place(x=150,y=750)
            labe3["text"] = value[0]
            labe4 = Label(frame, text="",font=("times new roman", 15))
            labe4.place(x=600,y=600)
            labe4["text"] = value[1]
            labe5 = Label(frame, text="",font=("times new roman", 15))
            labe5.place(x=600,y=650)
            labe5["text"] = value[2]
            labe6 = Label(frame, text="",font=("times new roman", 15))
            labe6.place(x=600,y=750)
            global pi
            pi = int(value[0])
            a= int(value[2])
            global b
            b = int(en1.get())#int(row[0])
            qt = int(value[4])
            global pid
            pid = int(value[0])
            if b <= qt:
                global fqt
                fqt = qt - b   
                btn1["state"] = "normal"
                print(fqt)
                global ca
                ca = a*b
                labe6["text"] = ca
                print(ca)
            else:
            
                btn1["state"] = "disable"
                messagebox.showerror("error","Sorry! not enough quantity available.")
            
        except Exception as e:
            messagebox.showerror("Error",e)
    def new():
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
            cur = con.cursor()
            b = int(en1.get())#int(row[0])
            
            enk.insert(0,value[1])
            print(enk.get())
            if b == "":
                messagebox.showerror("Field Error"," All fields are required")
            else: 
                ppid = con.cursor()
                ppid.execute("select * from products where Pid=%s",(pid))
                ppid = ppid.fetchall()
                for ppid1 in ppid:
                    asaa = ppid1[7]
                    print(ppid1[7])

                cur.execute("insert into ordr(Id,name,email,Pid,Pname,QTY,bill,Order_date,Buying_Rate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[3],pid,enk.get(),b,ca,formatted_date,asaa))
                cur.execute("update products set QTY=%s where Pid=%s",(fqt,pi))
                con.commit()
                con.close
                messagebox.showinfo("New Product", "New product added successfully")
                btn1["state"] = "disable"
            enk.delete(0,END)
            labe3["text"] = ""
            labe3["width"] = 1
            labe4["text"] = ""
            labe4["width"] = 2
            labe5["text"] = ""
            labe5["width"] = 2
            labe6["text"] = ""
            labe6["width"] = 1
        except Exception as e:
            messagebox.showerror("Error",e)
    def Logout():
        try:
            messagebox.showinfo("Logout", "Thanks for using our app.")
            frame.destroy()
            usernameEntry.focus()
            usernameEntry.delete(0,END)
            passwordEntry.delete(0,END)
        except Exception as e:
            messagebox.showerror("Error",e)
    def Search():
        treeview3.delete(*treeview3.get_children())
        try:
            con4 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
            cur4 = con4.cursor()
            cur4.execute("select * from products where PName = %s",(Serac.get()))
            row4 = cur4.fetchall()
            i = 0
            for ro in row4:
                treeview3.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
                i = i+1
            if row4 == None:
                cur4 = con4.cursor()
                cur4.execute("select * from products where Category= %s",(Serac.get()))
                row4 = cur4.fetchall()
                i = 0
                for ro in row4:
                    treeview3.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
                    i = i+1
            else:
                cur4 = con4.cursor()
                cur4.execute("select * from products where Category= %s",(Serac.get()))
                row4 = cur4.fetchall()
                i = 0
                for ro in row4:
                    treeview3.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
                    i = i+1
        except Exception as e:
            print(e)
    def Defected():
        try:
            #grab record NUmber 
            selects = treeview4.focus()
            #grab record values
            global value 
            value = treeview4.item(selects,'values')        
            print(value[2])
            if value[3] <= dNames.get():
                messagebox.showerror("error","All fields are required !")
            else:
                try:
                    con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
                    cur = con.cursor()
                    cur.execute("select * from ordr")
                    con.commit()
                    con.close
                    Dids = Label(frame, text="",fg="red",font=("times new roman", 15))
                    Dids.place(x=950,y=650)
                    Dids["text"]=value[3]
                    DNa = Label(frame, text="",fg="red",font=("times new roman", 15))
                    DNa.place(x=950,y=700)
                    DNa["text"]=value[2]
                    a = int(dNames.get())
                    try:                       
                        con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
                        cur = con.cursor()
                        cur.execute("select * from products where Pname=%s",(value[2]))
                        defrow = cur.fetchall()
                        for r in defrow:
                            #print(r[5])1
                            if r[5] <= "":
                                print(a)
                                con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
                                cur = con.cursor()
                                cur.execute("update products set Defected=%s where PName=%s",(a,value[2]))
                                con.commit()
                                con.close
                                messagebox.showinfo("Defected Product", "Sorry for inconvenience. Thanks for your valuable feedback. It will help to make our services more better.")
                                dNames.delete(0, END)
                                DNa["text"] = ""
                                Dids["text"] = ""
                            else:
                                #print(int(r[5]) + a)
                                b = (int(r[5]) + a)
                                
                                con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
                                cur = con.cursor()
                                cur.execute("update products set Defected=%s where PName=%s",(b,value[2]))
                                con.commit()
                                con.close
                                messagebox.showinfo("Defected Product", "Sorry for inconvenience. Thanks for your valuable feedback. It will help to make our services more better.")
                                dNames.delete(0, END)
                                DNa["text"] = ""
                                Dids["text"] = ""
                    except Exception as e:
                        messagebox.showinfo("Defected Product", e)
                except:
                    print(":ERROR")
        except Exception as e:
            messagebox.showerror("error", e)

    def refresh():
        con4 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
        cur4 = con4.cursor()
        cur4.execute("select * from products")
        row4 = cur4.fetchall()
        treeview3 =ttk.Treeview(frame,height=700)
        treeview3["columns"]= ("PId","P_Name","Price","Category")
        treeview3["show"]="headings"
        s = ttk.Style(root)
        s.theme_use("vista")
        s.configure(".", font=('times new roman', 11))
        s.configure("treeview3.Heading", foreground="BLUE", font=("times new roman", 14, "bold"))
        treeview3.column('PId', width=5, minwidth=5,anchor=tk.CENTER)
        treeview3.column('P_Name', width=30, minwidth=20,anchor=tk.CENTER)
        treeview3.column('Price', width=30, minwidth=30,anchor=tk.CENTER)
        treeview3.column('Category', width=30, minwidth=30,anchor=tk.CENTER)


    ################################## Adding heading #####################################################

        treeview3.heading('PId', text='PId', anchor=CENTER)
        treeview3.heading('P_Name', text='P_Name', anchor=CENTER)
        treeview3.heading('Price', text='Price' ,anchor=CENTER)
        treeview3.heading('Category', text='Category' ,anchor=CENTER)    
        treeview3.place(x=10,y=120,width=650,height=400)
        i = 0
        for ro in row4:
            treeview3.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
            i = i+1
        hsb = ttk.Scrollbar(treeview3, orient="vertical")
        hsb.configure(command=treeview3.yview)
        treeview3.configure(yscrollcommand=hsb.set)
        hsb.pack(fill=Y,side=RIGHT)

    ###########################################################################################################
    ###########################################################################################################
    ###########################################################################################################
        ItemsL = Label(frame,text="History",font=("calibri",18,"bold"),fg="gray4")
        ItemsL.place(x=670,y=80)
        con5 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
        cur5 = con5.cursor()
        cur5.execute("select * from ordr where name=%s and email=%s",(row[1],row[3]))
        row5 = cur5.fetchall()
        treeview4 =ttk.Treeview(frame,height=700)
        treeview4["columns"]= ("Id","Name","Product","Qty","Bill","Date")
        treeview4["show"]="headings"
        s = ttk.Style(root)
        s.theme_use("vista")
        s.configure(".", font=('times new roman', 11))
        s.configure("treeview4.Heading", foreground="BLUE", font=("times new roman", 14, "bold"))
        #adding columns
        treeview4.column('Id', minwidth=1,anchor=tk.CENTER, stretch=NO, width=50)
        treeview4.column('Name',  minwidth=10,anchor=tk.CENTER, stretch=NO, width=130)
        treeview4.column('Product', width=10, minwidth=10,anchor=tk.CENTER)
        treeview4.column('Qty', minwidth=10,anchor=tk.CENTER, stretch=NO, width=50)
        treeview4.column('Bill', minwidth=10,anchor=tk.CENTER, stretch=NO, width=80)
        treeview4.column('Date', width=10, minwidth=10,anchor=tk.CENTER) 
        #adding heading
        treeview4.heading('Id', text='Id', anchor=CENTER)
        treeview4.heading('Name', text='Name', anchor=CENTER)
        treeview4.heading('Product', text='Product' ,anchor=CENTER)
        treeview4.heading('Qty', text='Qty' ,anchor=CENTER)
        treeview4.heading('Bill', text='Bill' ,anchor=CENTER)
        treeview4.heading('Date', text='Date' ,anchor=CENTER)    
        treeview4.place(x=670,y=120,width=700,height=400)        
        i = 0
        for ro in row5:
            treeview4.insert('',i, text="", values=(ro[0],ro[1],ro[4],ro[5],ro[6],ro[7]))
            i = i+1
        hsb = ttk.Scrollbar(treeview4, orient="vertical")
        hsb.configure(command=treeview4.yview)
        treeview4.configure(yscrollcommand=hsb.set)
        hsb.pack(fill=Y,side=RIGHT)

    
    
    
    
    
    
    
    
############################################################################################  
    
    image2 = Image.open("Buttonimages/loogo3.png")
    image2 = image2.resize((50,50), Image.ANTIALIAS) 
    test = ImageTk.PhotoImage(image2)
    canvas = tk.Label(fk,bg="gray4",fg="red",image=test)
    canvas.image = test
    canvas.place(x=30,y=10)
    s = Label(fk, text="Stationary", font=("times new romans",12,"bold"),bg="gray4",fg="White")
    s.place(x=100,y=2)
    ks = Label(fk, text="Management", font=("times new romans",12,"bold"),bg="gray4",fg="White")
    ks.place(x=100,y=24)
    ss = Label(fk, text="System", font=("times new romans",12,"bold"),bg="gray4",fg="White")
    ss.place(x=100,y=44)
    l = Label(fk, text="", font=("calibri",18,"bold"),bg="gray4",fg="Red")
    l.place(x=600,y=10)
    l["text"] = "Welcome " + row[1]
    Serac = Entry(fk, font=("times new romans",14,"bold"))
    Serac.place(x=1000,y=20,width=150)
    logbtn = Button(fk,text="Logout",bg="red",fg="white", command=Logout)
    logbtn.place(x=1300,y=20,width=70)
    btn = Button(fk,text="Search",bg="white",fg="gray4",command=Search)
    btn.place(x=1200,y=20,width=70)
    btn = Button(frame,text="Select", bg="deep sky blue",fg="White",command=hello,font=("times new roman",12,"bold"))
    btn.place(x=450,y=550,width=70)
    btn1 = Button(frame,state="disable", bg="green",fg="white",text="Order",font=("times new roman",12,"bold"), command=new)
    btn1.place(x=550,y=550,width=70)
    Btnrefresh = Button(frame, bg="blue",fg="white",text="Refresh",font=("times new roman",12,"bold"), command=refresh)
    Btnrefresh.place(x=650,y=550,width=70)
    Btsnrefresh = Button(frame, bg="Red",fg="white",text="DEFECTED",font=("times new roman",12,"bold"), command=Defected)
    Btsnrefresh.place(x=750,y=550,width=70)
    con7 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur7 = con7.cursor()
    cur7.execute("select * from ordr ")
    cs = cur7.fetchall()
    con7.commit()
    con7.close()    
    print(cs)
def login():    
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
        cur = con.cursor()
        cur.execute("select * from employees where fname=%s and passwrd=%s",(usernameEntry.get(),passwordEntry.get()))
        global row
        row = cur.fetchone()
        print(row)
        if row==None:
            messagebox.showerror("ERROR", "Enter Valid Username or Password")    
        else:
            messagebox.showinfo("Success", "Login Successfully")
            loginPage()	
    except:
        pass
################################################ Section Change #####################################################

root2 = Tk()  
root2.geometry('1400x800+0+0')  
root2.title('Stationary Management System | Login')
root2.resizable("false","false")

######################################## Login Page Background ###########################################

image1 = Image.open("Buttonimages/background3.jpg")
image1 = image1.resize((1400,800), Image.ANTIALIAS) 
test = ImageTk.PhotoImage(image1)
canvas = tk.Label(root2,image=test)
canvas.image = test
canvas.place(x=0,y=0)

######################################## FRAME #######################################################
root = Frame(canvas, width=600,height=600, bg="white")
root.place(x=430,y=120)
root3 = Frame(canvas, width=1400,height=50, bg="gray4")
root3.place(x=0,y=0)

######################################## Login Page Labels and Entries ####################################

label2 = Label(root3,font=("times new roman",18,"bold"),bg="gray4",fg="White",text="Stationary Management System | Developed By Maryam.")
label2.place(x=450,y=10)
global usernameEntry
usernameEntry = StringVar()
Modelname = Label(root, font=("arial",25,BOLD),fg="red4",bg="white", text="Stationary Management System")
Modelname.place(x=50, y=20)
Modelname2 = Label(root, font=("arial",15,BOLD),fg="green",bg="white", text="Login Page")
Modelname2.place(x=220, y=80)
username = Label(root,  font=("arial",14,BOLD), foreground="red",bg="white", text="User Name")
username.place(x=120, y=170)
username = StringVar()
usernameEntry = Entry(root, textvariable=username )
usernameEntry.place(x=240, y=170, width=200, height=25)
usernameEntry.focus()
passwordLabel = Label(root, font=("arial",14,BOLD), foreground="red",bg="white", text="Password")
passwordLabel.place(x=120, y=270 )
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*')
passwordEntry.place(x=240, y=270 , width=200, height=25)

######################################## Buttons ###########################################################
photo = PhotoImage(file = "Buttonimages/Loginbtn.png")
photo.zoom(200,200)
resetb = PhotoImage(file = "Buttonimages/Reset.png")
resetb.zoom(120,120)
Exitbt = PhotoImage(file = "Buttonimages/exitb.png")
Exitbt.zoom(120,120)
loginButton = Button(root, text="Login", font=("arial", 12, BOLD),bd=0,bg="white",image=photo, command=lambda:[passchk(), empty(),admin(),login()])#validateLogin
loginButton.place(x=250, y=370 , width=130)
resetButton = Button(root, text="Reset", font=("arial", 12, BOLD),bd=0,bg="white",image=resetb, foreground="blue" , command=reset)
resetButton.place(x=250, y=420 , width=130)
exitButton = Button(root, text="Exit", font=("arial", 12, BOLD),bd=0,bg="white",image=Exitbt,foreground="red", command=root2.destroy) 
exitButton.place(x=250, y=470 , width=130)

root2.mainloop()     
