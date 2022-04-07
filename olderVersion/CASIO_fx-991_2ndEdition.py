# -*- coding: utf-8 -*-
'''
Recreated on Sat Apr 10 20:45:09 2021

@author: home168
'''
from tkinter import Tk, IntVar, Label, END, StringVar, Frame, Entry, Button, RIGHT, Canvas, Text
from math import sqrt

win = Tk()
win.resizable(False, False)
win.geometry('230x330')
win.overrideredirect(True)
win.attributes('-topmost', 1)
win.configure(bg='#202020')
X = IntVar(value=0)
Y = IntVar(value=0)
canMove = IntVar(value=0)
still = IntVar(value=1)
dragbar = Frame(win, width=50, height=3)
dragbar.configure(bg='black')
dragbar.pack()
label = Label(dragbar, width=15, height=3, bg='#202020', text='CASIO\nfx-991ES PLUS', fg='#c6c4c0')
label.grid(row=0, column=0)
solarPanel = Label(dragbar, width=30, height=3, bg='#202020',)
solarPanel.grid(row=0, column=1)


def buttonClick(number):
    global formula
    if number in ('+','-','*','/'): CalculateTask()
    formula = str(formula) + str(number)
    if number in ('/100', '**2'): CalculateTask()
    UserIn.set(formula)
    if formula == '': UserIn.set('0')
    
def buttonClickFunc(functionName):
    global formula
    formula = str(functionName) + '(' + str(formula) + ')'
    CalculateTask()
    UserIn.set(formula)
    
def ClearEntry():
    global formula
    while True:
        if formula != '':
            if formula[-1] in ('0','1','2','3','4','5','6','7','8','9','.','a','b','c','d','e','f','A','B','C','D','E','F'):
                formula = str(formula)[:-1]
                UserIn.set(formula)
            else:
                break
        else:
            break
    if formula == '':
        UserIn.set('0')

def Clear():
    global formula
    formula = ''
    user_input.delete(0, END)
    user_input.insert(0, '0')
    
def backspace():
    global formula
    formula = str(formula)[:-1]
    UserIn.set(formula)

    
def displayText(value):
    user_input.delete(0, END)
    user_input.insert(0, value)

def CalculateTask():
    global formula
    UserIn.set(formula)
    data = user_input.get()
    try:
        answer = eval(data)
        displayText(answer)
        formula = str(answer)
    except SyntaxError as e:
        displayText('Invalid Syntax!')
        formula = ''
    except ZeroDivisionError:
        displayText('Can\'t divided by zero!')
    except TypeError:
        displayText('Funcs aren\'t numbers!')
        
        
def off():
    win.destroy()
    
def onLeftButtonDown(event):
    win.attributes('-alpha', 0.6)
    X.set(event.x)
    Y.set(event.y)
    canMove.set(1)
    
label.bind('<Button-1>', onLeftButtonDown)

def onLeftButtonUp(event):
    win.attributes('-alpha', 1)
    canMove.set(0)
label.bind('<ButtonRelease-1>', onLeftButtonUp)

def onLeftButtonMove(event):
    if canMove.get()==0:
        return
    newX = win.winfo_x()+(event.x-X.get())
    newY = win.winfo_y()+(event.y-Y.get())
    g = '230x330+'+str(newX)+'+'+str(newY)
    win.geometry(g)
label.bind('<B1-Motion>', onLeftButtonMove)

def onRightButtonDown(event):
    still.set(0)
    win.destroy()
label.bind('<Button-3>', onRightButtonDown)
            

UserIn = StringVar()

frame1 = Frame(win)
frame1.configure(bg='#202020')
frame1.pack()
frame2 = Frame(win)
frame2.configure(bg='#202020')
frame2.pack()
user_input = Text(frame1, bg = '#bad4ba', bd = 10, fg='#0f3085', 
                insertwidth = 4, width = 22,
                font = ('CASIO-Calculator-Font', 12, 'bold'), textvariable = UserIn, justify = RIGHT)
'''try:
    user_input = Text(frame1, bg = '#bad4ba', bd = 10, fg='#0f3085', 
        insertwidth = 4, width = 22,
        font = ('CASIO-Calculator-Font', 12, 'bold'), textvariable = UserIn, justify = RIGHT)
except:
    user_input = Entry(frame1, bg = '#bad4ba', bd = 10, fg='#0f3085', 
        insertwidth = 4, width = 22,
        font = ('Arial', 12,'bold'), textvariable = UserIn, justify = RIGHT)'''
user_input.config(highlightbackground="black")
user_input.pack(padx=6)
user_input.insert(0, '0')

buttonpercent = Button(frame2, text='%', width=5, command=lambda : buttonClick('/100'))
buttonpercent.grid(row=0, column=0, padx=5, pady=5)
buttonsqrt = Button(frame2, text=u'\u221A', width=5, command=lambda : buttonClickFunc('sqrt'))
buttonsqrt.grid(row=0, column=1, padx=5, pady=5)
buttonsqr = Button(frame2, text='x^2', width=5, command=lambda : buttonClick('**2'))
buttonsqr.grid(row=0, column=2, padx=5, pady=5)
button1x = Button(frame2, text='1/x', width=5, command=lambda : buttonClickFunc('1/'))
button1x.grid(row=0, column=3, padx=5, pady=5)

buttonce = Button(frame2, text='CE', width=5, command=ClearEntry)
buttonce.grid(row=1, column=0, padx=5, pady=5)
buttonc = Button(frame2, text='C', width=5, command=Clear)
buttonc.grid(row=1, column=1, padx=5, pady=5)
buttonbs = Button(frame2, text=u'\u232B', width=5, command=backspace)
buttonbs.grid(row=1, column=2, padx=5, pady=5)
buttondivide = Button(frame2, text=u'\u00F7', width=5, command=lambda : buttonClick('/'))
buttondivide.grid(row=1, column=3, padx=5, pady=5)

button7 = Button(frame2, text='7', width=5, command=lambda : buttonClick('7'))
button7.grid(row=2, column=0, padx=5, pady=5)
button8 = Button(frame2, text='8', width=5, command=lambda : buttonClick('8'))
button8.grid(row=2, column=1, padx=5, pady=5)
button9 = Button(frame2, text='9', width=5, command=lambda : buttonClick('9'))
button9.grid(row=2, column=2, padx=5, pady=5)
buttontimes = Button(frame2, text=u'\u00D7', width=5, command=lambda : buttonClick('*'))
buttontimes.grid(row=2, column=3, padx=5, pady=5)

button4 = Button(frame2, text='4', width=5, command=lambda : buttonClick('4'))
button4.grid(row=3, column=0, padx=5, pady=5)
button5 = Button(frame2, text='5', width=5, command=lambda : buttonClick('5'))
button5.grid(row=3, column=1, padx=5, pady=5)
button6 = Button(frame2, text='6', width=5, command=lambda : buttonClick('6'))
button6.grid(row=3, column=2, padx=5, pady=5)
buttonminus = Button(frame2, text='-', width=5, command=lambda : buttonClick('-'))
buttonminus.grid(row=3, column=3, padx=5, pady=5)

button1 = Button(frame2, text='1', width=5, command=lambda : buttonClick('1'))
button1.grid(row=4, column=0, padx=5, pady=5)
button2 = Button(frame2, text='2', width=5, command=lambda : buttonClick('2'))
button2.grid(row=4, column=1, padx=5, pady=5)
button3 = Button(frame2, text='3', width=5, command=lambda : buttonClick('3'))
button3.grid(row=4, column=2, padx=5, pady=5)
buttonplus = Button(frame2, text='+', width=5, command=lambda : buttonClick('+'))
buttonplus.grid(row=4, column=3, padx=5, pady=5)


buttonplusminus = Button(frame2, text='OFF', width=5, command=off)
buttonplusminus.grid(row=5, column=0, padx=5, pady=5)
button0 = Button(frame2, text='0', width=5, command=lambda : buttonClick('0'))
button0.grid(row=5, column=1, padx=5, pady=5)
buttonpoint = Button(frame2, text='.', width=5, command=lambda : buttonClick('.'))
buttonpoint.grid(row=5, column=2, padx=5, pady=5)
buttonequal = Button(frame2, text='=', width=5, command=CalculateTask)
buttonequal.grid(row=5, column=3, padx=5, pady=5)

formula = ''

win.mainloop()


#The FontStruction “CASIO-Calculator-Font” (https://fontstruct.com/fontstructions/show/1475969) by “TH3_C0N-MAN” is licensed under a Creative Commons Attribution Share Alike license (http://creativecommons.org/licenses/by-sa/3.0/).

