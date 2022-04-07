# -*- coding: utf-8 -*-
'''
Recreated on Sat Apr 10 20:45:09 2021

@author: home168
'''
from tkinter import Tk, IntVar, Label, END, Frame, Button, Text, INSERT, PhotoImage
from math import sqrt
#from os import path

##Initialization
win = Tk()
win.resizable(False, False)
win.geometry('300x500')
win.overrideredirect(True)
win.attributes('-topmost', 1)
win.configure(bg='#202020')
X = IntVar(value=0)
Y = IntVar(value=0)
canMove = IntVar(value=0)
still = IntVar(value=1)
dragbar = Frame(win, width=50, height=4)
dragbar.configure(bg='black')
dragbar.pack()
logo = PhotoImage(file="images/logo.png")
label = Label(dragbar, image=logo, bd=0, bg='#202020')
label.grid(row=0, column=0)
#solarPanel = Label(dragbar, width=30, height=4, bg='#202020',)
#solarPanel.grid(row=0, column=1)

##Any Simple Button Clicked
def buttonClick(number):
    global formula, user_input, isEqualed, Ans, answer
    if isEqualed:
        user_input.delete(1.0,"end")
        Ans = answer
        if number in ('+','-','*','/', '\u00F7', '\u00D7'):
            formula = 'Ans'
        else:
            formula = ''
        isEqualed = False
    formula = str(formula) + str(number)
    #if number in ('/100', '**2'): CalculateTask()
    user_input.delete(1.0,"end")
    user_input.insert(INSERT, formula)
    
##Specific Buttons such as SQRT are Clicked 
def buttonClickFunc(functionName):
    global formula, user_input
    formula = str(functionName) + '(' + str(formula) + ')'
    CalculateTask()
    user_input.delete(1.0,"end")
    user_input.insert(INSERT, formula)
    
#C    
def Clear():
    global formula
    formula = ''
    user_input.delete(1.0, END)
    
    
def backspace():
    global formula, user_input
    formula = str(formula)[:-1]
    user_input.delete(1.0,"end")
    user_input.insert(INSERT, formula)

##Display and Refresh Text on Screen   
def displayText(value):
    user_input.delete(1.0, END)
    user_input.insert(INSERT, value)

## when = is clicked
def CalculateTask():
    global formula, user_input, isEqualed, answer
    user_input.delete(1.0,"end")
    user_input.insert(INSERT, formula)
    data = user_input.get("1.0",END)
    try:
        data = data.replace('\u00F7', '/')
        data = data.replace('\u00D7', '*')
        answer = eval(data)
        if answer % 1 == 0: answer = int(answer)
        displayText(answer)
        formula = str(answer)
        isEqualed = True
    except SyntaxError:
        if formula != '':
            displayText('\nSyntax ERROR\n\n[AC]  :Cancel\n[<][>]:Goto')
            formula = ''
    except ZeroDivisionError:
        displayText('\nMath ERROR\n\n[AC]  :Cancel\n[<][>]:Goto')
    except TypeError:
        displayText('Funcs aren\'t numbers!')
        
        
def off():
    win.destroy()
    
### Window Drag Starts Here ###
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
    g = '300x500+'+str(newX)+'+'+str(newY)
    win.geometry(g)
label.bind('<B1-Motion>', onLeftButtonMove)

def onRightButtonDown(event):
    still.set(0)
    win.destroy()
label.bind('<Button-3>', onRightButtonDown)            
### Window Drag Ends Here ###

##Button in the lower frame
def button(text, command, bg='#606060'):
    return Button(frame2, text=text, width=5, command=command, fg='#ffffff', bg=bg, activebackground=bg, activeforeground='#ffffff')

isEqualed = False
Ans = ''
answer = 0

###Frame initized###
frame1 = Frame(win)
frame1.configure(bg='#202020')
frame1.pack()
framebtn = Frame(win)
framebtn.configure(bg='#202020')
framebtn.pack()
frame3 = Frame(framebtn)
frame3.configure(bg='#202020')
frame3.pack()
frame2 = Frame(framebtn)
frame2.configure(bg='#202020')
frame2.pack()

### Screen Setup ###
try:
    user_input = Text(frame1, bg='#bad4ba', bd=10, fg='#0f3085', 
                insertwidth=4, width=22, height=5, 
                font=('CASIO-Font', 15))
    isFontCorrect = True
except:
    user_input = Text(frame1, bg='#bad4ba', bd=10, fg='#0f3085', 
                insertwidth=4, width=22, height=5, 
                font=('Arial', 20))
    isFontCorrect = False
user_input.config(highlightbackground="black")
user_input.pack(padx=9)

##
loadimage = PhotoImage(file="images/RndBtn.png")
buttonshift = Button(frame3, image=loadimage, bg='#202020', bd=0, activebackground='#202020')
buttonshift.grid(row=0, column=0)
buttonshift = Button(frame3, image=loadimage, bg='#202020', bd=0, activebackground='#202020')
buttonshift.grid(row=0, column=0)
buttonshift = Button(frame3, image=loadimage, bg='#202020', bd=0, activebackground='#202020')
buttonshift.grid(row=0, column=0)
buttonshift = Button(frame3, image=loadimage, bg='#202020', bd=0, activebackground='#202020')
buttonshift.grid(row=0, column=0)
buttonshift = Button(frame3, image=loadimage, bg='#202020', bd=0, activebackground='#202020')
buttonshift.grid(row=0, column=0)
buttonshift = Button(frame3, image=loadimage, bg='#202020', bd=0, activebackground='#202020')
buttonshift.grid(row=0, column=0)

'''
buttonpercent = Button(frame3, text='%', width=5, command=lambda : buttonClick('/100'))
buttonpercent.grid(row=0, column=0, padx=5, pady=5)
buttonsqrt = Button(frame3, text=u'\u221A', width=5, command=lambda : buttonClickFunc('sqrt'))
buttonsqrt.grid(row=0, column=1, padx=5, pady=5)
buttonsqr = Button(frame3, text='x^2', width=5, command=lambda : buttonClick('**2'))
buttonsqr.grid(row=0, column=2, padx=5, pady=5)
button1x = Button(frame3, text='1/x', width=5, command=lambda : buttonClickFunc('1/'))
button1x.grid(row=0, column=3, padx=5, pady=5)'''


#row0
button7 = button('7', lambda:buttonClick('7'))
button7.grid(row=0, column=0, padx=5, pady=5)
button8 = button('8', lambda:buttonClick('8'))
button8.grid(row=0, column=1, padx=5, pady=5)
button9 = button('9', lambda:buttonClick('9'))
button9.grid(row=0, column=2, padx=5, pady=5)
buttonbs = button('DEL', backspace, bg='#9fb665')
buttonbs.grid(row=0, column=3, padx=5, pady=5)
buttonc = button('AC', Clear, bg='#9fb665')
buttonc.grid(row=0, column=4, padx=5, pady=5)
#row1
button4 = button('4', lambda:buttonClick('7'))
button4.grid(row=1, column=0, padx=5, pady=5)
button5 = button('5', lambda:buttonClick('5'))
button5.grid(row=1, column=1, padx=5, pady=5)
button6 = button('6', lambda:buttonClick('6'))
button6.grid(row=1, column=2, padx=5, pady=5)
buttontimes = button('\u00D7', lambda:buttonClick('\u00D7'))
buttontimes.grid(row=1, column=3, padx=5, pady=5)
buttondivide = button('\u00F7', lambda:buttonClick('\u00F7'))
buttondivide.grid(row=1, column=4, padx=5, pady=5)
#row2
button1 = button('1', lambda:buttonClick('1'))
button1.grid(row=2, column=0, padx=5, pady=5)
button2 = button('2', lambda:buttonClick('2'))
button2.grid(row=2, column=1, padx=5, pady=5)
button3 = button('3', lambda:buttonClick('3'))
button3.grid(row=2, column=2, padx=5, pady=5)
buttonplus = button('+', lambda:buttonClick('+'))
buttonplus.grid(row=2, column=3, padx=5, pady=5)
buttonminus = button('-', lambda:buttonClick('-'))
buttonminus.grid(row=2, column=4, padx=5, pady=5)
#row3
button0 = button('0', lambda:buttonClick('0'))
button0.grid(row=3, column=0, padx=5, pady=5)
buttonpoint = button('.', lambda:buttonClick('.'))
buttonpoint.grid(row=3, column=1, padx=5, pady=5)
buttonpower10 = button('x10^x', off)
buttonpower10.grid(row=3, column=2, padx=5, pady=5)
buttonans = button('Ans', lambda:buttonClick('Ans'))
buttonans.grid(row=3, column=3, padx=5, pady=5)
buttonequal = button('=', CalculateTask)
buttonequal.grid(row=3, column=4, padx=5, pady=5)
#buttonoff = Button(frame2, text='OFF', width=5, command=off)
#buttonoff.grid(row=3, column=2, padx=5, pady=5)

formula = ''

win.mainloop()



