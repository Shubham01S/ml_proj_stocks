from tkinter import *
from sqlite3 import *
import time
import tkinter
from tkinter import messagebox
#from PIL import ImageTk,Image
#from numpy import mean
import numpy as np
import matplotlib.pyplot as plt
import quandl
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import scale
class Stocks:
    def main(sf):
        try:
            sf.scr.destroy()
            sf.scr=Tk()
        except:
            try:
                sf.scr=Tk()
            except:
                pass


        sf.scr.geometry("1366x768")
        sf.scr.title("STOCK ANALYIS")
        #sf.mainf1=Frame(sf.scr,height=150,width=1366)
        #sf.mainf1.pack(fill=BOTH,expand=1)
        sf.mainf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.mainf2,height=618,width=1366)
        sf.c.pack()
##        sf.window=tkinter.Tk()
##        sf.image=Image.open("C:\\Users\\parul\\Documents\\s1.jpg")
##        sf.img=ImageTk.PhotoImage(sf.image)
##        sf.label=tkinter.Label(sf.window,image=sf.img)
##        sf.label.pack()
##        #sf.d=Canvas(sf.scr,height=618,width=1366)
        #sf.back=PhotoImage(file="C:\\Users\\parul\\Documents\\st1.png")
        #sf.c.create_image(700,284,image=sf.back)
        #sf.back_label=Label(sf.scr,image=sf.back)
        #sf.back_label.place(x=0,y=0,relwidth=1,relheight=1)
        #sf.d.pack()
        
        sf.lab=Button(sf.mainf2,text= "Click Here to know about Stocks",command=lambda:sf.Login(),cursor="hand2", bd=10 ,font=("cooper black",30, 'bold'),fg="white",bg="#0b1335")
        sf.lab.place(x=400,y=200)
        sf.mainf2.pack(fill=BOTH,expand=1)
##        sf.m=Menubutton(sf.scr,text="file",bg="blue",fg="yellow",relief="raised")
##        sf.m.place(x=0,y=0)
##        sf.m.fm=Menu(sf.m)
##        sf.m["menu"]=sf.m.fm
##        sf.m.fm.add_command(label="new",command=lambda:sf.fun())
##        sf.m.fm.add_command(label="open",command=lambda:sf.fun())
##        sf.m.fm.add_command(label="save",command=lambda:sf.fun())
##        sf.sb=Menu(sf.m.fm,tearoff=0)
##        sf.sb.add_command(label="file",command=lambda:sf.fun())
##        sf.sb.add_command(label="project",command=lambda:sf.fun())
##        sf.sb.add_command(label="module",command=lambda:sf.fun())
##        sf.m.fm.add_cascade(label="recent",menu=sf.sb)

        sf.scr.mainloop()
    def msft(sf):
        dt1=quandl.get('EOD/MSFT',auth_token="sG1gRzNEgoDwzJbfm22k")
        print(dt1.shape)
        print(dt1.index)
        dt1["Adj_Close"].plot()
        plt.show()
        dt1.head(1)
        dt1=dt1[['Adj_Open','Adj_High','Adj_Low','Adj_Close','Adj_Volume']]
        dt1["Adj_Close"].shift(-2).head()
        dt1["Adj_Close"].shift(-2).tail()
        pct=int(len(dt1)*0.001)
        dt1["newclose"]=dt1["Adj_Close"].shift(-pct)
        print(dt1["newclose"].tail(82))
        x=dt1.drop("newclose",1)
        x=scale(x)
        x_a=x[:-pct]
        x_p=x[-pct:]
        y=dt1.dropna()["newclose"]
        x_r,x_t,y_r,y_t=train_test_split(x_a,y,test_size=0.3)
        alg=LinearRegression()
        alg.fit(x_r,y_r)
        print(alg.score(x_t,y_t),alg.predict(x_p))
        print(dt1["Adj_Close"].tail(8))

    def Login(sf):
        sf.cartlist=[]
        sf.amount=0
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Stock prediction")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.loginf1=Frame(sf.scr,height=150,width=1366)
        #sf.logo=PhotoImage(file="logo.PNG")
        #sf.ba=Label(sf.loginf1,image=sf.logo,height=150).place(x=0,y=0)
        sf.home=Button(sf.loginf1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.home.place(x=800,y=100)
        sf.adlog=Button(sf.loginf1,text="Administrator Login",command=lambda:sf.Adminlogin(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("cooper black",16))
        sf.adlog.place(x=925,y=100)
        sf.abt=Button(sf.loginf1,text="About Us",bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        #sf.abt.config(command=lambda:sf.about())
        sf.abt.place(x=1210,y=100)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.loginf1,text=sf.localtime,fg="black",font=("default",16),bg="#0b1335")
        sf.tim.place(x=925,y=50)
        sf.loginf1.pack(fill=BOTH,expand=1)
        sf.loginf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.loginf2,height=618,width=1366)
        sf.c.pack()
        #sf.logo1=PhotoImage(file="pizzamain.png")
        #sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(50,100,700,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.loginf2,text="LOGIN",fg="white",bg="#0b1335",width=26,font=("cooper black",27))
        sf.log.place(x=59,y=105)
        sf.lab1=Label(sf.loginf2,text="UserName",bg="#d3ede6",font=("cooper black",22))
        sf.lab1.place(x=100,y=180)
        sf.user=Entry(sf.loginf2,bg="white",font=("cooper black",22),bd=6 ,justify='left')
        sf.user.place(x=320,y=180)
        sf.lab2=Label(sf.loginf2,text="Password",bg="#d3ede6",font=("cooper black",22))
        sf.lab2.place(x=105,y=250)
        sf.pasd=Entry(sf.loginf2,bg="white",font=("cooper black",22),bd=6 ,justify='left')
        sf.pasd.place(x=320,y=250)
        sf.lg=Button(sf.loginf2,text="Login",cursor="hand2",command=lambda:sf.logindatabase(),fg="white",bg="#0b1335",font=("cooper black",20),bd=4)
        sf.lg.place(x=180,y=320)
        def clear(sf):
            sf.user.delete(0,END)
            sf.pasd.delete(0,END)
        sf.cl=Button(sf.loginf2,text="Clear",cursor="hand2",command=lambda:clear(sf),fg="white",bg="#0b1335",font=("cooper black",20),bd=4)
        sf.cl.place(x=450,y=320)
        sf.rg=Button(sf.loginf2,text="Not a member?",command=lambda:sf.Register(),fg="white",cursor="hand2",bg="#8c68c1",font=("cooper black",20),bd=6)
        sf.rg.place(x=200,y=390)
        sf.c.create_rectangle(850,120,1310,480,fill="#d3ede6",outline="white",width=4)
        #sf.ext=PhotoImage(file="p4.png")
        #sf.url=Label(sf.loginf2,image=sf.ext,cursor="hand2").place(x=855,y=125)
        sf.loginf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    def resultlog(sf):
        sf.loguser=sf.user.get()
        sf.logpass=sf.pasd.get()
        return sf.loguser,sf.logpass
    def Register(sf):
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Stocks prediction")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.regf1=Frame(sf.scr,height=150,width=1366)
        #sf.logo=PhotoImage(file="logo.PNG")
        #sf.ba=Label(sf.regf1,image=sf.logo,height=150).place(x=0,y=0)
        sf.home=Button(sf.regf1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",fg="white",font=("default",16))
        sf.home.place(x=800,y=100)
        sf.adlog=Button(sf.regf1,text="Administrator Login",command=lambda:sf.Adminlogin(),cursor="hand2",bg="#0b1335",fg="white",font=("default",16))
        sf.adlog.place(x=950,y=100)
        sf.abt=Button(sf.regf1,text="About Us",command=lambda:sf.about(),bg="#0b1335",cursor="hand2",fg="white",font=("default",16))
        sf.abt.place(x=1210,y=100)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.regf1,text=sf.localtime,fg="white",font=("default",16),bg="#0b1335")
        sf.tim.place(x=925,y=50)
        sf.regf1.pack(fill=BOTH,expand=1)
        
        sf.regf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.regf2,height=618,width=1366)
        sf.c.pack()
        #sf.logo1=PhotoImage(file="pizzamain.png")
        #sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(150,100,1216,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.regf2,text="REGISTRATION",fg="white",bg="#0b1335",width=20,font=("cooper black",27))
        sf.log.place(x=480,y=120)
        sf.lab1=Label(sf.regf2,text="FirstName",bg="#d3ede6",font=("cooper black",18))
        sf.lab1.place(x=190,y=200)
        sf.first=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.first.place(x=430,y=200)
        sf.lab2=Label(sf.regf2,text="LastName",bg="#d3ede6",font=("cooper black",18))
        sf.lab2.place(x=730,y=200)
        sf.last=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.last.place(x=920,y=200)
        sf.lab3=Label(sf.regf2,text="Username",bg="#d3ede6",font=("cooper black",18))
        sf.lab3.place(x=190,y=250)
        sf.usern=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.usern.place(x=430,y=250)
        sf.lab4=Label(sf.regf2,text="Password",bg="#d3ede6",font=("cooper black",18))
        sf.lab4.place(x=730,y=250)
        sf.passd=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.passd.place(x=920,y=250)
        sf.lab5=Label(sf.regf2,text="Email",bg="#d3ede6",font=("cooper black",18))
        sf.lab5.place(x=190,y=300)
        sf.email=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.email.place(x=430,y=300)
        sf.lab6=Label(sf.regf2,text="Mobile No.",bg="#d3ede6",font=("cooper black",18))
        sf.lab6.place(x=730,y=300)
        sf.mob=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.mob.place(x=920,y=300)
        sf.bc=Button(sf.regf2,text="Back",cursor="hand2",command=lambda:sf.Login(),fg="white",bg="#0b1335",font=("cooper black",18),bd=5)
        sf.bc.place(x=370,y=370)
        sf.rg=Button(sf.regf2,text="Register",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.Regdatabase(),font=("cooper black",18),bd=5)
        sf.rg.place(x=610,y=370)
        def clear(sf):
            sf.usern.delete(0,END)
            sf.passd.delete(0,END)
            sf.first.delete(0,END)
            sf.last.delete(0,END)
            sf.email.delete(0,END)
            sf.mob.delete(0,END)
        sf.cl=Button(sf.regf2,text="Clear",cursor="hand2",fg="white",bg="#0b1335",command=lambda:clear(sf),font=("cooper black",18),bd=5)
        sf.cl.place(x=910,y=370)
        sf.regf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    def resultreg(sf):
        sf.reguser=sf.usern.get()
        sf.regpasd=sf.passd.get()
        sf.firstname=sf.first.get()
        sf.lastname=sf.last.get()
        sf.Email=sf.email.get()
        sf.Mob=sf.mob.get()
        return sf.reguser,sf.regpasd,sf.firstname,sf.lastname,sf.Email,sf.Mob

    def logindatabase(sf):
        sf.credlog=sf.resultlog()
        sf.con=connect("h:/pizza.db")
        sf.cur=sf.con.cursor()
        try:
            sf.cur.execute("create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x=sf.cur.execute("select count(*) from customer where username=%r and password=%r"%(sf.credlog[0],sf.credlog[1]))
        if list(x)[0][0]==0:
            if sf.credlog[0]=="" or sf.credlog[1]=="":
                messagebox.showinfo("Login","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Login","You are Not Registered Yet")
            
        else:
            messagebox.showinfo("Login","You have Successfully Log In\nWelcome !!!")            
            sf.stkmain()

    def Regdatabase(sf):
        sf.credreg=sf.resultreg()
        sf.con=connect("h:/pizza.db")
        print("opened")
        sf.cur=sf.con.cursor()
        try:
            sf.cur.execute("create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x=sf.cur.execute("select count(*) from customer where username=%r and mob=%r "%(sf.credreg[0],sf.credreg[5]))
        if list(x)[0][0]==0:
            if sf.credreg[0]=="" or sf.credreg[1]=="" or sf.credreg[2]=="" or sf.credreg[3]=="" or sf.credreg[5]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed(except Email)")
            else:
                sf.cur.execute("insert into customer values(%r,%r,%r,%r,%r,%r)"%(sf.credreg[0],sf.credreg[1],sf.credreg[2],sf.credreg[3],sf.credreg[4],sf.credreg[5]))
                sf.con.commit()
                messagebox.showinfo("Register","You are Successfully Registered")
                sf.Login()
        else:
            messagebox.showinfo("Register","Username Already Exist \nEnter New Username")
        
    def stkmain(sf):
         sf.scr.destroy()
         sf.scr=Tk()
         sf.pizf1=Frame(sf.scr,height=150,width=1366)
         sf.c=Canvas(sf.pizf1,height=150,width=1366)
         sf.c.pack()
         #sf.logo=PhotoImage(file="logo.PNG")
         #sf.c.create_image(683,75,image=sf.logo)
         sf.c.create_text(950,80,text="WELCOME",fill="black",font=("default",20))
         sf.name="User"
         sf.c.create_text(950,120,text=sf.name,fill="black",font=("default",18))
         sf.out=Button(sf.pizf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",font=("default",16))
         sf.out.place(x=1200,y=100)
         sf.localtime=time.asctime(time.localtime(time.time()))
         sf.c.create_text(1000,40,text=sf.localtime,fill="white",font=("default",16))
         sf.mainf1=Frame(sf.scr,height=150,width=1366)
         sf.mainf1.pack(fill=BOTH,expand=1)
         sf.pizf1.pack(fill=BOTH,expand=1)
         sf.mainf2=Frame(sf.scr,height=618,width=1366)
         sf.c=Canvas(sf.mainf2,height=618,width=1366)
         sf.c.pack()
         sf.m=Menubutton(sf.scr,text="STOCKS",bg="blue",fg="yellow",relief="raised")
         sf.m.place(x=0,y=0)
         sf.m.fm=Menu(sf.m)
         sf.m["menu"]=sf.m.fm
         sf.m.fm.add_command(label="MICROSOFT CORPORATIONS",command=lambda:sf.msft())
##         sf.m.fm.add_command(label="TCS",command=lambda:sf.fun())
##         sf.m.fm.add_command(label="save",command=lambda:sf.fun())
##         sf.sb=Menu(sf.m.fm,tearoff=0)
##         sf.sb.add_command(label="file",command=lambda:sf.fun())
##         sf.sb.add_command(label="project",command=lambda:sf.fun())
##         sf.sb.add_command(label="module",command=lambda:sf.fun())
##         sf.m.fm.add_cascade(label="recent",menu=sf.sb)
## 
         

         
        
        
x=Stocks()
x.main()
##    def fun(sf):
##      sf.scr.destroy()
##      sf.scr=Tk()
##      sf.m.fm.add_command(label="new",command=lambda:sf.fun())
##      sf.m.fm.add_command(label="open",command=lambda:sf.fun())
##      sf.m.fm.add_command(label="save",command=lambda:sf.fun())
##      sf.sb=Menu(m.fm,tearoff=0)
##      sf.sb.add_command(label="file",command=lambda:sf.fun())
##      sf.sb.add_command(label="project",command=lambda:sf.fun())
##      sf.sb.add_command(label="module",command=lambda:sf.fun())
##      sf.m.fm.add_cascade(label="recent",menu=sf.sb)
##      sf.scr.mainloop()
 
 
