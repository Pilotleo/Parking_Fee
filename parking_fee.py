import tkinter as tk
from tkinter import messagebox
import datetime
import sys
win = tk.Tk()
win.title('停車費計算器')
win.geometry('1000x160')
win.resizable(False, False)
fm_ent = tk.Frame(win, width=600, height=400)
fm_ent.pack(side=tk.TOP, fill=tk.BOTH)

#年
year1 = tk.StringVar(None, '2022')
ent1 = tk.Entry(fm_ent, width=12, justify='center', textvariable=year1)
ent1.grid(row=0,column=0)
#ent1.pack(side=tk.LEFT, padx=12, pady=7, fill=tk.Y)

lbl_empty = tk.Label(fm_ent, 
               text='年', font=('微軟正黑體', 12), 
               padx=12)
lbl_empty.grid(row=0,column=1)
#lbl_empty.pack(side=tk.LEFT)

#月
month1 = tk.StringVar(None, '2')
ent2 = tk.Entry(fm_ent, width=12, justify='center', textvariable=month1)
#ent2.pack(side=tk.LEFT, padx=12, pady=7, fill=tk.Y)
ent2.grid(row=0,column=2)
lbl_empty = tk.Label(fm_ent, 
               text='月', font=('微軟正黑體', 12), 
               padx=12)
#lbl_empty.pack(side=tk.LEFT)
lbl_empty.grid(row=0,column=3)

#日
day1 = tk.StringVar(None, '1')
ent3 = tk.Entry(fm_ent, width=12, justify='center', textvariable=day1)
#ent3.pack(side=tk.LEFT, padx=12, pady=7, fill=tk.Y)
ent3.grid(row=0,column=4)
lbl_empty = tk.Label(fm_ent, 
               text='日', font=('微軟正黑體', 12), 
               padx=12)
#lbl_empty.pack(side=tk.LEFT)
lbl_empty.grid(row=0,column=5)
#時
hour1 = tk.StringVar(None, '5')
ent4 = tk.Entry(fm_ent, width=12, justify='center', textvariable=hour1)
#ent4.pack(side=tk.LEFT, padx=17, pady=7, fill=tk.Y)
ent4.grid(row=0,column=6)
lbl_empty = tk.Label(fm_ent, 
               text='時', font=('微軟正黑體', 12), 
               padx=12)
#lbl_empty.pack(side=tk.LEFT)
lbl_empty.grid(row=0,column=7)

#分
minute1 = tk.StringVar(None, '00')
ent5 = tk.Entry(fm_ent, width=12, justify='center', textvariable=minute1)
#ent5.pack(side=tk.LEFT, padx=17, pady=7, fill=tk.Y)
ent5.grid(row=0,column=8)
lbl_empty = tk.Label(fm_ent, 
               text='分', font=('微軟正黑體', 12), 
               padx=12)
#lbl_empty.pack(side=tk.LEFT)
lbl_empty.grid(row=0,column=9)
#秒
second1 = tk.StringVar(None, '00')
ent6 = tk.Entry(fm_ent, width=12, justify='center', textvariable=second1)
#ent6.pack(side=tk.LEFT, padx=17, pady=7, fill=tk.Y)
ent6.grid(row=0,column=10)
lbl_empty = tk.Label(fm_ent, 
               text='秒', font=('微軟正黑體', 12), 
               padx=12)
#lbl_empty.pack(side=tk.LEFT)
lbl_empty.grid(row=0,column=11)
#年
year2 = tk.StringVar(None, '2022')
ent7 = tk.Entry(fm_ent, width=12, justify='center', textvariable=year2)
ent7.grid(row=1,column=0)
#ent1.pack(side=tk.LEFT, padx=12, pady=7, fill=tk.Y)

lbl_empty = tk.Label(fm_ent, 
               text='年', font=('微軟正黑體', 12), 
               padx=12)
lbl_empty.grid(row=1,column=1)
#lbl_empty.pack(side=tk.LEFT)
#月
month2 = tk.StringVar(None, '2')
ent8 = tk.Entry(fm_ent, width=12, justify='center', textvariable=month2)
#ent8.pack(side=tk.LEFT, padx=12, pady=7, fill=tk.Y)
ent8.grid(row=1,column=2)
lbl_empty = tk.Label(fm_ent, 
               text='月', font=('微軟正黑體', 12), 
               padx=12)
#lbl_empty.pack(side=tk.LEFT)
lbl_empty.grid(row=1,column=3)
#日
day2 = tk.StringVar(None, '1')
ent9 = tk.Entry(fm_ent, width=12, justify='center', textvariable=day2)
#ent9.pack(side=tk.LEFT, padx=12, pady=7, fill=tk.Y)
ent9.grid(row=1,column=4)
lbl_empty = tk.Label(fm_ent, 
               text='日', font=('微軟正黑體', 12), 
               padx=12)
#lbl_empty.pack(side=tk.LEFT)
lbl_empty.grid(row=1,column=5)
#時
hour2 = tk.StringVar(None, '15')
ent10 = tk.Entry(fm_ent, width=12, justify='center', textvariable=hour2)
#ent10.pack(side=tk.LEFT, padx=17, pady=7, fill=tk.Y)
ent10.grid(row=1,column=6)
lbl_empty = tk.Label(fm_ent, 
               text='時', font=('微軟正黑體', 12), 
               padx=12)
#lbl_empty.pack(side=tk.LEFT)
lbl_empty.grid(row=1,column=7)
#分
minute2 = tk.StringVar(None, '05')
ent11 = tk.Entry(fm_ent, width=12, justify='center', textvariable=minute2)
#ent11.pack(side=tk.LEFT, padx=17, pady=7, fill=tk.Y)
ent11.grid(row=1,column=8)
lbl_empty = tk.Label(fm_ent, 
               text='分', font=('微軟正黑體', 12), 
               padx=12)
#lbl_empty.pack(side=tk.LEFT)
lbl_empty.grid(row=1,column=9)
#秒
second2 = tk.StringVar(None, '00')
ent12 = tk.Entry(fm_ent, width=12, justify='center', textvariable=second2)
#ent12.pack(side=tk.LEFT, padx=17, pady=7, fill=tk.Y)
ent12.grid(row=1,column=10)
lbl_empty = tk.Label(fm_ent, 
               text='秒', font=('微軟正黑體', 12), 
               padx=12)
#lbl_empty.pack(side=tk.LEFT)
lbl_empty.grid(row=1,column=11)

def money_cal():
    dt1=datetime.datetime(int(year1.get()),int(month1.get()),int(day1.get()),int(hour1.get()),int(minute1.get()),int(second1.get()))
    dt2=datetime.datetime(int(year2.get()),int(month2.get()),int(day2.get()),int(hour2.get()),int(minute2.get()),int(second2.get()))
    dt3=dt2-dt1
    dday=dt3.days
    #dhour=dt3.hours
    #dminute=dt3.minutes
    dseconds=dt3.seconds
    hours=int(dseconds/1800)
    if dday>0:
        if dseconds > 28800:
            dday+=1
            money1= dday*240            
        elif dseconds%1800 >0:
            if hours>0:
                hours=hours+1
                money1= dday*240 +hours*15
            elif dseconds%1800 !=0:
                hours+=1
                money1= dday*240+hours*15
        else:
            money1= dday*240+hours*15
    elif dseconds > 28800:
        dday+=1
        money1= dday*240            
    elif dseconds%1800 >0 :
        if hours>0:
            hours=hours+1
            money1= dday*240 +hours*15
        else:
            money1=0
    else:
        money1=hours*15    
    #print(dt3)
    messagebox.showwarning('計算結果', '你的停車費是'+ str(money1))
    
def button_event1():
    #把StringVar轉數字塞到日期  
    money_cal()
mybutton = tk.Button(fm_ent, text='計算停車費',command=button_event1)
mybutton.grid(row=0,column=12)
win.mainloop()
