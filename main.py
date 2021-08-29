import cx_Oracle

dsn_tns = cx_Oracle.makedsn('DESKTOP-3CTHK6S', '1521', service_name='XE') 
conn = cx_Oracle.connect(user=r'system', password='system', dsn=dsn_tns)

c = conn.cursor()

from tkinter import *
dic={'bal':0,'with':0,'dep':0}
def login():
    r=Toplevel()
    r.configure(background='orange')
    r.title("sridhar")
    r.geometry('250x250+550+150')
    e=StringVar()
    f=StringVar()
    E=Entry(r,textvariable=e).grid(column=1,row=0)
    E1=Entry(r,textvariable=f,show='*').grid(column=1,row=1)
    def x():
        def bal():
            dsn_tns = cx_Oracle.makedsn('DESKTOP-3CTHK6S', '1521', service_name='XE') 
            conn = cx_Oracle.connect(user=r'system', password='system', dsn=dsn_tns)

            c = conn.cursor()
            c.execute('select acc_bal from tkbank where username like:llike',llike=e.get())
            bal=0
            for i in c:
                bal=i[0]
            dic['bal']=bal
            l=Label(r,text=bal).grid(column=1,row=4)
        def w():
            s=Toplevel()
            e=StringVar()
            l=Label(s,text='withdraw').grid(column=0,row=0)
            E=Entry(s,textvariable=e).grid(column=1,row=0)
            def withdraw():
                k=e.get()
                d=int(k)
                if((dic['bal']-d)>=2500):
                    dic['bal']-=d
                    print(dic['bal'])
                    l=Label(s,text='you have succesfully withdrawn=',font=("aira black",15),bg='orange',fg='green').grid(column=0,row=2)
                    l=Label(s,text=d,font=("aira black",15),bg='orange',fg='green').grid(column=1,row=2)
                    b=Button(s,text='DONE',command=s.destroy).grid(column=1,row=1)
                    dsn_tns = cx_Oracle.makedsn('DESKTOP-3CTHK6S', '1521', service_name='XE') 
                    conn = cx_Oracle.connect(user=r'system', password='system', dsn=dsn_tns)

                    c = conn.cursor()
                    c.execute('update tkbank set acc_bal=:acc_bal where user_pwd=:user_pwd',acc_bal=dic['bal'],user_pwd=f.get())
                    conn.commit()
                else:
                    l=Label(s,text='cannot withdraw\n NO SUFFICIENT MONEY IN THE ACCOUNT').grid(column=0,row=2)
                    b=Button(s,text='add amount',command=di).grid(column=0,row=3)
                    b=Button(s,text='DONE',command=s.destroy).grid(column=1,row=1)
                    
            b=Button(s,text='ok',command=withdraw,bg='light blue',fg='indigo').grid(column=1,row=1)
        def di():
            q=Toplevel()
            q.configure(background='orange')
            q.geometry('100x25+550+150')
            e=StringVar()
            l=Label(q,text='deposit').grid(column=0,row=0)
            E=Entry(q,textvariable=e).grid(column=1,row=0)
            def deposit():
                k=e.get()
                d=int(k)
                dic['bal']+=d
                l=Label(q,text='you have succefully deposited',font=("aira black",15),bg='orange',fg='black').grid(column=0,row=2)
                l=Label(q,text=d,font=("aira black",15),bg='orange',fg='black').grid(column=0,row=3)
            b=Button(q,text='ok',command=deposit,bg='light blue',fg='indigo').grid(column=1,row=1)

        dsn_tns = cx_Oracle.makedsn('DESKTOP-3CTHK6S', '1521', service_name='XE') 
        conn = cx_Oracle.connect(user=r'system', password='system', dsn=dsn_tns)

        c = conn.cursor()
        row=[e.get()]
        c.execute('select username,user_pwd,acc_bal from tkbank where username like:llike',llike=e.get())
        for i in c:
            t=i[0]
            d=i[1]
            z=i[2]
        d=str(d)  #to convert d to str so that f.get() matches with d#
        if(t==e.get() and d==f.get()):
            l=Label(r,text='DONE!!!!!',font=("aira black",15),bg='orange',fg='pink').grid(column=1,row=3)
            a=Button(r,text='balance info',command=bal,bg='violet',fg='indigo').grid(column=0,row=4)
            a=Button(r,text='withdraw',command=w,bg='orange',fg='red').grid(column=0,row=5)
            a=Button(r,text='deposit',command=di,bg='pink',fg='red').grid(column=0,row=6)
        else:
            l=Label(r,text='invalid password try again').grid(column=1,row=3)
    b=Button(r,text='submit',command=x,bg='light blue',fg='indigo').grid(column=1,row=2)
    l=Label(r,text='Username',font=("aira black",15),bg='orange',fg='green').grid(column=0,row=0)
    l2=Label(r,text='Password',font=("aira black",15),bg='orange',fg='black').grid(column=0,row=1)
    
def newaccount():
    s=Toplevel()
    s.configure(background='orange')
    s.geometry('550x250+550+150')
    t=StringVar()
    g=StringVar()
    h=StringVar()
    E=Entry(s,textvariable=t).grid(column=1,row=2)
    E1=Entry(s,textvariable=g,show='*').grid(column=1,row=3)
    def x():
        def z():
            E2=Entry(s,textvariable=h).grid(column=1,row=4)
            l2=Label(s,text='deposit',font=("aira black",15),bg='orange',fg='pink').grid(column=0,row=4)
            def q():
                d=h.get()
                k=int(d)
                dic['bal']=k
                dsn_tns = cx_Oracle.makedsn('DESKTOP-3CTHK6S', '1521', service_name='XE') 
                conn = cx_Oracle.connect(user=r'system', password='system', dsn=dsn_tns)

                c = conn.cursor()
                row=[k,temp]
                c.execute('update tkbank set acc_bal=:acc_bal where acc_no=:acc_no',acc_bal=k,acc_no=temp)
                conn.commit()
                if(k>=2500):
                    l=Label(s,text='hurray!!!!\nYour account has been created',font=("aira black",15),bg='orange',fg='black').grid(column=1,row=8)
                    c=Button(s,text='login',command=login,bg='light blue',fg='indigo').grid(column=1,row=10)
                else:
                    l=Label(s,text='your account has not been created\n please deposit more than 2500 to start account',font=("aira black",15),bg='orange',fg='black').grid(column=1,row=9)
                    b=Button(s,text='quit',command=quit,bg='light blue',fg='indigo').grid(column=1,row=10)
            b=Button(s,text='ok',command=q).grid(column=1,row=10)

        c.execute('select acc_no from tkbank')
        temp=0
        for i in c:
            temp=i[0]
        temp+=1
        rows=[t.get(),g.get(),temp]
        c.execute("insert into tkbank(username,user_pwd,acc_no) values(:1,:2,:3)",rows)
        conn.commit()
        conn.close()
        l1=Label(s,text='enter minimum of 2500 rupees to create account',font=("aira black",15),bg='orange',fg='black').grid(column=1,row=6)
        k=Button(s,text='deposit',command=z,bg='light blue',fg='indigo').grid(column=1,row=7)
    b=Button(s,text='submit',command=x,bg='light blue',fg='indigo').grid(column=1,row=5)
    l=Label(s,text='username',font=("aira black",15),bg='orange',fg='green').grid(column=0,row=2)
    l2=Label(s,text='password',font=("aira black",15),bg='orange',fg='black').grid(column=0,row=3)

def account():
    global s
    s=Tk()
    s.configure(background='yellow')
    s.title('ACCOUNT')
    s.geometry('300x260+550+150')
    photo = PhotoImage(file="tk bank.png")
    w = Label(s, image=photo)
    w.photo = photo
    w.grid(column=0,row=0)
    #img=PhotoImage(file="u1.png")
    #k=Label(s,image=img).pack()
    l=Button(s,text='login',command=login,fg='black',bg='grey',height=2,width=10,font=("Monotype Corsiva",10)).grid(column=0,row=1)
    b=Button(s,text='new account',command=newaccount,fg='indigo',bg='grey',height=2,width=10).grid(column=0,row=2)
account()



