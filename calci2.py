import tkinter as tk
from tkinter import ttk
exp=" "
def press(num):
    global exp
    exp+=str(num)
    equation.set(exp)
def equalpress():
    try:
        global exp
        total=str(eval(exp))
        equation.set(total)
        exp=" "
    except:
        equation.set('error')
        exp=" "
def clear():
    global exp
    exp=" "
    equation.set(" ")
def fullclear():
    exit()
if __name__ == "__main__":
    root=tk.Tk()
    root.title('calculator')
    root.geometry('300x414')
    root.maxsize(width=300,height=414)
    root.configure(bg='blue')
equation=tk.StringVar()
dis_entry=ttk.Entry(root,width=47,state='readonly',background='red',textvariable=equation)
dis_entry.grid(row=0,columnspan=10,ipadx=6,ipady=34)
dis_entry.focus()

btnexit=ttk.Button(root,text='EXIT',width=10,command=lambda:fullclear())
btnexit.grid(row=1,column=0,ipady=20,ipadx=4)

btn7=ttk.Button(root,text='7',width=10,command=lambda:press(7))
btn7.grid(row=2,column=0,ipady=20,ipadx=4)

btn8=ttk.Button(root,text='8',width=10,command=lambda:press(8))
btn8.grid(row=2,column=1,ipady=20,ipadx=4)

btn9=ttk.Button(root,text='9',width=10,command=lambda:press(9))
btn9.grid(row=2,column=2,ipady=20,ipadx=4)

btn4=ttk.Button(root,text='4',width=10,command=lambda:press(4))
btn4.grid(row=3,column=0,ipady=20,ipadx=4)

btn5=ttk.Button(root,text='5',width=10,command=lambda:press(5))
btn5.grid(row=3,column=1,ipady=20,ipadx=4)

btn6=ttk.Button(root,text='6',width=10,command=lambda:press(6))
btn6.grid(row=3,column=2,ipady=20,ipadx=4)


btn1=ttk.Button(root,text='1',width=10,command=lambda:press(1))
btn1.grid(row=4,column=0,ipady=20,ipadx=4)

btn2=ttk.Button(root,text='2',width=10,command=lambda:press(2))
btn2.grid(row=4,column=1,ipady=20,ipadx=4)

btn3=ttk.Button(root,text='3',width=10,command=lambda:press(3))
btn3.grid(row=4,column=2,ipady=20,ipadx=4)

btn0=ttk.Button(root,text='0',width=10,command=lambda:press(0))
btn0.grid(row=5,columnspan=2,ipady=28,ipadx=43)


btnmines=ttk.Button(root,text='-',width=8,command=lambda:press('-'))
btnmines.grid(row=2,column=3,ipady=20,ipadx=4)

btnmul=ttk.Button(root,text='*',width=8,command=lambda:press('*'))
btnmul.grid(row=3,column=3,ipady=20,ipadx=4)

btneql=ttk.Button(root,text='=',width=8,command=lambda:equalpress())
btneql.grid(row=4,column=3,rowspan=20,ipady=70,ipadx=4)

btnpls=ttk.Button(root,text='+',width=8,command=lambda:press('+'))
btnpls.grid(row=1,column=3,ipady=20,ipadx=4)

btnmod=ttk.Button(root,text='/',width=10,command=lambda:press('/'))
btnmod.grid(row=5,column=2,ipady=28,ipadx=4)

#btndvd=ttk.Button(root,text='/',width=8,command=lambda:equalpress('/'))
#btndvd.grid(row=4,column=2,ipady=20,ipadx=10)

btnclr=ttk.Button(root,text='CE',width=14,command=lambda:clear())
btnclr.grid(row=1,column=1,columnspan=2,ipady=20,ipadx=31)


