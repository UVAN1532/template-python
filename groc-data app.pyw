import tkinter as tk
from tkinter import font, messagebox
from win32com.client.gencache import __init__
import easygui

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="open@123",
  database="uvandb"
)
mycursor = mydb.cursor()


class grocerylist:
    def __init__(self, month='not specified', date='not specified'):
        self.total = 0
        global total
        self.month = month
        self.date = date
        self.list = [self.month, 'date:' + self.date]
        self.list2=[]

    def add_item(self, num):
        grlst = []
        for x in range(num):
            it, pr, qnt = map(str, input('enter item , price and quantity in same line separated by space : ').split())
            grlst.extend([('item: ' + it, 'unit price: ' + pr, 'quantity: ' + qnt, int(pr) * int(qnt))])
            self.list2.extend([it,pr,qnt])
            self.total += int(pr) * int(qnt)
        self.list.extend(grlst)

    def prnt_list(self):
        print(self.list)

    def tot(self):
        print(self.total)

    def store_list(self):
        a = (self.month, self.date, self.total,str(self.list2))
        mycursor.execute('INSERT INTO grocery(month,date,total,items) VALUES (%s,%s,%s,%s)', a)
        mydb.commit()
        self.list.clear()
        self.total=0


def get_total(month2):
    mycursor.execute('SELECT * FROM grocery')
    items = mycursor.fetchall()
    mydb.commit()
    tot = 0
    for item in items:
        if month2 in item[0]:
            tot += item[2]
        else:
            continue
    print(tot)


list_created = False


def button9():
    quit()


def button1():
    but2.configure(state='disabled')
    but3.configure(state='disabled')
    but4.configure(state='disabled')
    but5.configure(state='disabled')
    but6.configure(state='disabled')
    but7.configure(state='disabled')
    but8.configure(state='disabled')
    win.geometry('700x600')
    chummalab.configure(bg='#FFDABF')
    subbut.configure(state='normal')
    backbut.configure(state='normal')
    month_lab.configure(bg='#FFDABF')
    date_lab.configure(bg='#FFDABF')
    month_ent.configure(state='normal')
    date_ent.configure(state='normal')
    update_reclst = ''
    recent_lst.configure(text=update_reclst)

def subbutfunc():
    if len(month_ent.get()) == 0:
        month_ent.configure(bg='#FF9999')
    if len(date_ent.get()) == 0:
        date_ent.configure(bg='#FF9999')
    if len(month_ent.get()) > 0:
        month_ent.configure(bg='white')
    if len(date_ent.get()) > 0:
        date_ent.configure(bg='white')
    if not date_ent.get().isdigit() and len(date_ent.get()) > 0:
        messagebox.showinfo(title='Invalid Date', message='PLEASE PROVIDE VALID DATE')
        date_ent.delete(0, tk.END)
    if len(month_ent.get()) > 0 and len(date_ent.get()) > 0:
        global mon
        mon = grocerylist(month_ent.get(), date_ent.get())
        __init__()
        global list_created
        list_created = True
        win.geometry('700x600')
        but2.configure(state='normal')
        but3.configure(state='normal')
        but4.configure(state='normal')
        but5.configure(state='normal')
        but6.configure(state='normal')
        but7.configure(state='normal')
        but8.configure(state='normal')
        month_ent.delete(0, tk.END)
        date_ent.delete(0, tk.END)
        month_ent.configure(bg='white', state='disabled')
        date_ent.configure(bg='white', state='disabled')
        subbut.configure(state='disabled')
        backbut.configure(state='disabled')
        chummalab.configure(bg='#BFBFFF')
        month_lab.configure(bg='#BFBFFF')
        date_lab.configure(bg='#BFBFFF')
        update_reclst = recent_lst.cget('text') +str([mon.month,mon.date])
        recent_lst.configure(text=update_reclst)
        messagebox.showinfo(message='The List Has Been Created And Changes will Be Done to This List Until One More List Is Created ', title='List created')


def backbutpress():
    month_ent.delete(0, tk.END)
    date_ent.delete(0, tk.END)
    if list_created:
        update_reclst = recent_lst.cget('text') +str([mon.month,mon.date])
        recent_lst.configure(text=update_reclst)
    else:
        ur = ''
        recent_lst.configure(text=ur)
    month_ent.configure(bg='white', state='disabled')
    date_ent.configure(bg='white', state='disabled')
    subbut.configure(state='disabled')
    backbut.configure(state='disabled')
    chummalab.configure(bg='#BFBFFF')
    month_lab.configure(bg='#BFBFFF')
    date_lab.configure(bg='#BFBFFF')
    but2.configure(state='normal')
    but3.configure(state='normal')
    but4.configure(state='normal')
    but5.configure(state='normal')
    but6.configure(state='normal')
    but7.configure(state='normal')
    but8.configure(state='normal')

def button2():
    if list_created :
        chummalab2.configure(bg='#FFD9AB')
        item_lab.configure(bg='#FFD9AB')
        unitprice_lab.configure(bg='#FFD9AB')
        quant_lab.configure(bg='#FFD9AB')
        but1.configure(state='disabled')
        but3.configure(state='disabled')
        but4.configure(state='disabled')
        but5.configure(state='disabled')
        but6.configure(state='disabled')
        but7.configure(state='disabled')
        but8.configure(state='disabled')
        backbut2.configure(state='normal')
        addbut.configure(state='normal')
        subbut2.configure(state='normal')
        item_ent.configure(state='normal')
        unitprice_ent.configure(state='normal')
        quant_ent.configure(state='normal')
    else:
        messagebox.showinfo(title='List Error',message='Create List First')


def backbut2press():
    item_ent.delete(0, tk.END)
    unitprice_ent.delete(0, tk.END)
    item_ent.configure(bg='white', state='disabled')
    unitprice_ent.configure(bg='white', state='disabled')
    subbut2.configure(state='disabled')
    backbut2.configure(state='disabled')
    chummalab2.configure(bg='#BFBFFF')
    item_lab.configure(bg='#BFBFFF')
    unitprice_lab.configure(bg='#BFBFFF')
    but1.configure(state='normal')
    but3.configure(state='normal')
    but4.configure(state='normal')
    but5.configure(state='normal')
    but6.configure(state='normal')
    but7.configure(state='normal')
    but8.configure(state='normal')
    quant_lab.configure(bg='#BFBFFF')
    quant_ent.configure(state='disabled')
    addbut.configure(state='disabled')

def addbutpress():
    item_name = item_ent.get()
    unit = unitprice_ent.get()
    quantity = quant_ent.get()
    if unit.isdigit() and len(item_name)>0:
        item_ent.configure(bg='white')
        grlst = []
        grlst.extend([('item: ' + item_name, 'unit price: ' + unit, 'quantity: ' + str(quantity), int(unit) * int(quantity))])
        mon.list.extend(grlst)
        mon.total += int(unit) * int(quantity)
        mon.list2.append([item_name,unit,quantity])
        item_ent.delete(0, tk.END)
        unitprice_ent.delete(0, tk.END)
        quant_ent.set(0)
    if not unit.isdigit() and len(unit)>0:
        messagebox.showinfo(title='INVALID INPUT',message='PLEASE ENTER VALID INPUT ! ')
    if len(item_name)==0:
        item_ent.configure(bg='#FF9999')
    if len(unit)==0:
        unitprice_ent.configure(bg='#FF9999')
    if len(unit)>0 and unit.isdigit():
        unitprice_ent.configure(bg='white')
    if len(item_name)>0 :
        item_ent.configure(bg='white')

def button3():
    if list_created:
        chummalab3.insert(0,str(mon.list[2::])+'\n')
    else:
        messagebox.showinfo(title='List Error', message='Create List First')
def button4():
    if list_created:
        chummalab3.insert(0,mon.total)
    else:
        messagebox.showinfo(title='List Error', message='Create List First')
def button5():
    if list_created:
        a = (mon.month, int(mon.date), int(mon.total),str(mon.list2))
        mycursor.execute("INSERT INTO grocery(month,date,total,items) VALUES (%s,%s,%s,%s)",a)
        mydb.commit()
        mon.list.clear()
        mon.total=0
        mon.list = [mon.month, 'date:' + mon.date]
        messagebox.showinfo(title='SAVED!!!',message='LIST SAVED IN DATA BASE')
    else:
        messagebox.showinfo(title='List Error', message='Create List First')
def subbut2press():
    item_ent.delete(0, tk.END)
    unitprice_ent.delete(0, tk.END)
    item_ent.configure(bg='white', state='disabled')
    unitprice_ent.configure(bg='white', state='disabled')
    subbut2.configure(state='disabled')
    backbut2.configure(state='disabled')
    chummalab2.configure(bg='#BFBFFF')
    item_lab.configure(bg='#BFBFFF')
    unitprice_lab.configure(bg='#BFBFFF')
    but1.configure(state='normal')
    but3.configure(state='normal')
    but4.configure(state='normal')
    but5.configure(state='normal')
    but6.configure(state='normal')
    but7.configure(state='normal')
    but8.configure(state='normal')
    quant_lab.configure(bg='#BFBFFF')
    quant_ent.configure(state='disabled')
    addbut.configure(state='disabled')
    messagebox.showinfo(title='Items Added',message='ITEMS HAVE BEEN ADDED')


def button6():
    spec_mon=easygui.enterbox('Enter Month')
    if len(spec_mon)>0 and not spec_mon.isdigit():
        mycursor.execute('SELECT * FROM grocery')
        items = mycursor.fetchall()
        tot = 0
        for item in items:
            if spec_mon in item[0]:
                tot += item[2]
            else:
                continue
        chummalab3.insert(0,tot)
    else:
        messagebox.showinfo(title='INVALID',message='ENTER VALID INPUT!')
def button7():
    mycursor.execute('DELETE FROM grocery WHERE (month)!=""')
    mydb.commit()
    messagebox.showinfo(title='DELETED DATABASE',message='ALL LISTS HAVE BEEN DELETED FROM DATABASE')
def button8():
    mycursor.execute('SELECT * FROM grocery')
    a = mycursor.fetchall()
    c = 0
    for items in a:
        c += 1
        chummalab3.insert(0,items)
    if c >= 1:
        pass
    else:
       chummalab3.insert(0,'No Lists In Data-Base')

def clearpress():
    chummalab3.delete(0,tk.END)
def mainwin():
    root.destroy()
    global win,item_lab,item_ent, but1, but2, but3, but4, but5, but6, but7, but8, but9, month_ent, month_lab, \
    date_ent, date_lab, chummalab, chummalab2, subbut, backbut, recent_lst,unitprice_lab,unitprice_ent,quant_lab,\
    quant_ent,backbut2,subbut2,addbut,chummalab3,outputlab,clearbut
    win = tk.Tk()
    win.geometry('720x600')
    win.resizable(False,False)
    win.title('Grocery data')
    win.configure(bg='#8A2BE2')
    but1 = tk.Button(win, text='CREATE A LIST', width=20, height=2, activebackground='#D0D0FF', bd=3, relief='ridge',
                     command=button1)
    but1.place(x=80, y=30)
    but2 = tk.Button(win, text='ADD ITEMS TO CREATED LIST', width=30, height=2, activebackground='#D0D0FF', bd=3,
                     relief='ridge',command=button2)
    but2.place(x=50, y=90)
    but3 = tk.Button(win, text='PRINT ITEMS IN CURRENT LIST', width=30, height=2, activebackground='#D0D0FF', bd=3,
                     relief='ridge',command=button3)
    but3.place(x=50, y=150)
    but4 = tk.Button(win, text='PRINTING TOTAL OF CURRENT LIST', width=30, height=2, activebackground='#D0D0FF', bd=3,
                     relief='ridge',command=button4)
    but4.place(x=50, y=210)
    but5 = tk.Button(win, text='STORE LIST IN DATA-BASE', width=30, height=2, activebackground='#D0D0FF', bd=3,
                     relief='ridge',command=button5)
    but5.place(x=50, y=270)
    but6 = tk.Button(win, text='PRINTING TOTAL OF A MONTH', width=30, height=2, activebackground='#D0D0FF', bd=3,
                     relief='ridge',command=button6)
    but6.place(x=50, y=330)
    but7 = tk.Button(win, text='DELETE LIST IN DATA-BASE', width=30, height=2, activebackground='#D0D0FF', bd=3,
                     relief='ridge',command=button7)
    but7.place(x=50, y=390)
    but8 = tk.Button(win, text='PRINT LISTS IN DATA-BASE', width=30, height=2, activebackground='#D0D0FF', bd=3,
                     relief='ridge',command=button8)
    but8.place(x=50, y=450)
    but9 = tk.Button(win, text='EXIT PROGRAM', width=20, height=2, activebackground='#D0D0FF', bd=3, relief='ridge',
                     command=button9)
    but9.place(x=80, y=510)
    chummalab = tk.Button(win, height=9, width=40, bg='#BFBFFF', relief='ridge', state='disabled')
    chummalab.place(x=340, y=50)
    cus_font = font.Font()
    month_lab = tk.Label(win, text='Month of List  ', bg='#BFBFFF', font=('Helvetica bold', 10), )
    month_lab.place(x=370, y=70)
    month_ent = tk.Entry(win, bd=3, relief='groove', state='disabled')
    month_ent.place(x=457, y=70)
    date_lab = tk.Label(win, text='Date of Month  ', bg='#BFBFFF', font=('Helvetica bold', 10))
    date_lab.place(x=370, y=110)
    date_ent = tk.Entry(win, bd=3, relief='groove', state='disabled')
    date_ent.place(x=457, y=110)
    backbut = tk.Button(win, text='Back', activebackground='#D0D0FF', bd=3, relief='ridge', width=6,
                        command=backbutpress, state='disabled')
    backbut.place(y=150, x=380)

    subbut = tk.Button(win, text='SUBMIT', activebackground='#D0D0FF', bd=3, relief='ridge', command=subbutfunc,
                       state='disabled')
    subbut.place(x=523, y=150)
    recent_lst = tk.Label(win, text='', bg='#8A2BE2', font=('verdana', 11))
    recent_lst.place(x=7, y=570)

    def on_enter(event):
        but1.config(bg='#FFD9AB')

    def on_leave(event):
        but1.config(bg='white')

    def on_enter2(event):
        but2.config(bg='#FFD9AB')

    def on_leave2(event):
        but2.config(bg='white')

    def on_enter3(event):
        but3.config(bg='#FFD9AB')

    def on_leave3(event):
        but3.config(bg='white')

    def on_enter4(event):
        but4.config(bg='#FFD9AB')

    def on_leave4(event):
        but4.config(bg='white')

    def on_enter5(event):
        but5.config(bg='#FFD9AB')

    def on_leave5(event):
        but5.config(bg='white')

    def on_enter6(event):
        but6.config(bg='#FFD9AB')

    def on_leave6(event):
        but6.config(bg='white')

    def on_enter7(event):
        but7.config(bg='#FFD9AB')

    def on_leave7(event):
        but7.config(bg='white')

    def on_enter8(event):
        but8.config(bg='#FFD9AB')

    def on_leave8(event):
        but8.config(bg='white')

    def on_enter9(event):
        but9.config(bg='#FFD9AB')

    def on_leave9(event):
        but9.config(bg='white')

    but1.bind('<Enter>', on_enter)
    but1.bind('<Leave>', on_leave)
    but2.bind('<Enter>', on_enter2)
    but2.bind('<Leave>', on_leave2)
    but3.bind('<Enter>', on_enter3)
    but3.bind('<Leave>', on_leave3)
    but4.bind('<Enter>', on_enter4)
    but4.bind('<Leave>', on_leave4)
    but5.bind('<Enter>', on_enter5)
    but5.bind('<Leave>', on_leave5)
    but6.bind('<Enter>', on_enter6)
    but6.bind('<Leave>', on_leave6)
    but7.bind('<Enter>', on_enter7)
    but7.bind('<Leave>', on_leave7)
    but8.bind('<Enter>', on_enter8)
    but8.bind('<Leave>', on_leave8)
    but9.bind('<Enter>', on_enter9)
    but9.bind('<Leave>', on_leave9)

    chummalab2 = tk.Button(win, width=40, height=12, bg='#BFBFFF', relief='ridge', state='disabled')
    chummalab2.place(x=340, y=210)
    item_lab=tk.Label(win,text='Product ', bg='#BFBFFF', font=('Helvetica bold', 10))
    item_lab.place(x=370,y=223)
    item_ent=tk.Entry(win, bd=3, relief='groove', state='disabled')
    item_ent.place(x=450,y=220)
    unitprice_lab=tk.Label(win,text='Unit Price', bg='#BFBFFF', font=('Helvetica bold', 10))
    unitprice_lab.place(x=370,y=263)
    unitprice_ent=tk.Entry(win, bd=3, relief='groove', state='disabled')
    unitprice_ent.place(x=450,y=260)
    quant_lab=tk.Label(win,text='Quantity', bg='#BFBFFF', font=('Helvetica bold', 10))
    quant_lab.place(x=370,y=303)
    quant_ent=tk.Scale(win,from_=1,to=50,orient='horizontal',bg='#BFBFFF',width=10,length=123,troughcolor='#FFD9AB',state='disabled')
    quant_ent.place(x=450,y=300)
    backbut2 = tk.Button(win, text='Back', activebackground='#D0D0FF', bd=3, relief='ridge', width=6, state='disabled',command=backbut2press)
    backbut2.place(y=360, x=360)
    subbut2= tk.Button(win, text='SUBMIT', activebackground='#D0D0FF', bd=3, relief='ridge',
                       state='disabled', command=subbut2press)
    subbut2.place(x=563, y=360)
    addbut=tk.Button(win, text='ADD', activebackground='#D0D0FF', bd=3, relief='ridge', command=addbutpress,
                       state='disabled',width=6,bg='#FFD9AB')
    addbut.place(y=360,x=461)
    chummalab3=tk.Listbox(win, width=51, height=10, bg='#BFBFFF',font=('verdana',9))
    chummalab3.place(x=290,y=415)
    clearbut=tk.Button(win, text='Clear', activebackground='#D0D0FF', bd=3, relief='ridge', width=6,command=clearpress)
    clearbut.place(y=530,x=600)
    win.mainloop()


root = tk.Tk()
root.title('GROC-DATA ')
root.geometry('450x200')
root.configure(bg='#8A2BE2')
root.resizable(False,False)
mainhead=tk.Label(root,text='GROC-DATA',bg='#8A2BE2',font=('courier',50),fg='#FFD9AB')
openbut=tk.Button(root,text='OPEN',bd=2,relief='ridge',activebackground='#AFAFEF',width=6,command=mainwin)
openbut.place(x=155,y=120)
quitbut=tk.Button(root,text='QUIT',bd=2,relief='ridge',activebackground='#AFAFEF',width=6,command=button9)
quitbut.place(x=235,y=120)
mainhead.place(x=40,y=30)
root.mainloop()
