# -*- coding: utf-8 -*-
'''
Recreated on Sat Apr 10 20:45:09 2021

@author: home168
'''
from tkinter import Tk, IntVar, Label, END, Frame, Button, Text, INSERT, PhotoImage
from math import sqrt, sin, cos, tan, log10, log
from os import listdir
import re

##Initialization
bgblack = '#202020'
winwidth = 330
winheight = 656
win = Tk()
win.resizable(False, False)
win.geometry(str(winwidth)+'x'+str(winheight))
win.overrideredirect(True)
win.attributes('-topmost', 1)
win.configure(bg=bgblack)
X = IntVar(value=0)
Y = IntVar(value=0)
canMove = IntVar(value=0)
still = IntVar(value=1)
dragbar = Frame(win, width=50, height=4)
dragbar.configure(bg='black')
dragbar.pack()
logo = PhotoImage(file="images/logo.png")
label = Label(dragbar, image=logo, bd=0, bg=bgblack)
label.grid(row=0, column=0)
#solarPanel = Label(dragbar, width=30, height=4, bg=bgblack,)
#solarPanel.grid(row=0, column=1)

##Any Simple Button Clicked
def buttonClick(number):
    global formula, user_input, isEqualed, Ans, answer
    edit()
    if isEqualed:
        user_input.delete(1.0,"end")
        Ans = answer
        if number in ('+','-','*','/', '\u00F7', '\u00D7'):
            formula = 'Ans'
        else:
            formula = ''
        isEqualed = False
    
    formula = str(formula) + str(number)
    #formula = user_input.get(1.0, 'end-1c') + str(number)
    #if number in ('/100', '**2'): CalculateTask()
    user_input.delete(1.0,"end")
    user_input.insert(INSERT, formula)
    
##Specific Buttons such as SQRT are Clicked 
def buttonClickFunc(functionName):
    global formula, user_input
    formula = str(functionName) + '(' + str(formula) + ')'
    user_input.delete(1.0,"end")
    user_input.insert(INSERT, formula)
    
#AC    
def Clear(*events):
    global formula
    formula = ''
    user_input.config(state="normal")
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
def CalculateTask(*event):
    global formula, user_input, isEqualed, answer
    #user_input.delete(1.0,"end")
    #user_input.insert(INSERT, formula)
    datum = user_input.get("1.0","1.end")
    try:
        data = datum.replace('\u00D7\u00D7', '??')
        data = data.replace('\u00F7', '/')
        data = data.replace('\u00D7', '*')
        data = data.replace('^', '**')
        data = data.replace('\u00b2', '**2')
        data = data.replace('log', 'log10')
        data = data.replace('ln', 'log')
        answer = eval(data)
        if answer % 1 == 0: answer = int(answer)
        displayText(datum + '\n\n\n'+' '*(22-len(str(answer))) + str(answer))
        formula = str(answer)
        isEqualed = True
    except SyntaxError:
        if formula != '':
            displayText('\nSyntax ERROR\n\n[AC]  :Cancel\n[<][>]:Goto')
            formula = ''
        user_input.config(state="disabled")
    except ZeroDivisionError:
        displayText('\nMath ERROR\n\n[AC]  :Cancel\n[<][>]:Goto')
        user_input.config(state="disabled")
    except TypeError:
        displayText('\nUnknown ERROR\n\n[AC]  :Cancel\n[<][>]:Goto')
        user_input.config(state="disabled")
    except NameError:
        displayText('\nSyntax ERROR\n\n[AC]  :Cancel\n[<][>]:Goto')
        user_input.config(state="disabled")
    win.focus_set()
    user_input.config(state='disabled')


def off():
    win.destroy()

def shift():
    pass

def alpha():
    pass

def ArrowClicked(event):
    if str(user_input['state']) == 'disabled':
        user_input.focus_set()
        user_input.config(state='normal')
        
def edit(*event):
    if str(user_input['state']) == 'disabled':
        user_input.focus_set()
        user_input.config(state='normal')
        temp = user_input.get(1.0, '1.end')
        user_input.delete(1.0, 'end')
        user_input.insert(INSERT, temp)
        
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
    g = str(winwidth)+'x'+str(winheight)+'+'+str(newX)+'+'+str(newY)
    win.geometry(g)
label.bind('<B1-Motion>', onLeftButtonMove)

def onRightButtonDown(event):
    still.set(0)
    win.destroy()
label.bind('<Button-3>', onRightButtonDown)            
### Window Drag Ends Here ###

##Button in the lower frame
def button(x, text, command, bg='#606060'):
    return Button(frames[x], text=text, width=5, command=command, fg='#ffffff',
                  bg=bg, activebackground=bg, activeforeground='#ffffff', font=('Carlito', 12))

##Button in the upper frame
def buttonx(x, image, command, bg=bgblack):
    return Button(frames2[x], image=image, command=command,
                  bg=bg, activebackground=bg, bd=0)


#### MAIN CODE STARTS HERE ####
isEqualed = False
Ans = ''
answer = 0

###Frame initized###
frame1 = Frame(win)
frame1.configure(bg=bgblack)
frame1.pack()
framebtn = Frame(win)
framebtn.configure(bg=bgblack)
framebtn.pack()
frame3 = Frame(framebtn)
frame3.configure(bg=bgblack)
frame3.pack(pady=10)
frame2 = Frame(framebtn)
frame2.configure(bg=bgblack)
frame2.pack()

#Each frame for every btn
frames = []
for i in range(0,4):
    for j in range(0,5):
        frame = Frame(frame2, bg=bgblack)
        frame.grid(row=i, column=j)
        frames.append(frame)
framearrow = Frame(frame3, bg=bgblack)
framearrow.grid(row=0, column=2, rowspan=2, columnspan=2)
frames2 = []
for i in range(0,5):
    for j in range(0,6):
        if not((i==0 or i==1) and (j==2 or j==3)):
            frame = Frame(frame3, bg=bgblack)
            frame.grid(row=i, column=j)
            frames2.append(frame)
            
### Screen Setup ###
try:
    user_input = Text(frame1, bg='#bad4ba', bd=10, fg='#0f3085', 
                insertwidth=4, width=22, height=5, 
                font=('CASIO-Font', 15), selectbackground='#0f3085', wrap='none')
    isFontCorrect = True
except:
    user_input = Text(frame1, bg='#bad4ba', bd=10, fg='#0f3085', 
                insertwidth=4, width=22, height=5, 
                font=('Arial', 20), selectbackground='#0f3085')
    isFontCorrect = False
user_input.config(highlightbackground="black")
user_input.pack(padx=9)

##Images and texts for buttons
images = listdir('./images')
photoimages = []
loadimage = PhotoImage(file="images/RndBtn.png")
for im in images[:-3]:
    photoimages.append(PhotoImage(file="images/"+im))


##Upper area buttons
lblbs = []
lblcs = []
arrowGridData = ((0,0,2),(0,1,1),(1,1,1),(0,2,2))
roundBtnText = (('SHIFT', '#b29d41'),('ALPHA', '#d45d89'),('MODE', '#ffffff'),('ON', '#ffffff'))
btnlbls1 = (('SOLVE', None), ('d/dx', None), ('x!', None), ('Σ', None),
            ('', None), ('√', None), ('x³', None), ('', None), ('', None), ('', None),
            ('', None), ('⟵', None), ('Abs', None), ('asin', None), ('acos', None), ('atan', None),
            ('STO', None), ('⟵', None), ('%', None), (',', None), ('', None), ('M-', None))
funcs = [shift, alpha, None, None,
         None, None, None, None,
         None, lambda:buttonClick('sqrt('), lambda:buttonClick('\u00b2'), None, lambda:buttonClick('log('), lambda:buttonClick('ln('),
         lambda:buttonClick('-'), None, None, lambda:buttonClick('sin('), lambda:buttonClick('cos('), lambda:buttonClick('tan('),
         None, None, lambda:buttonClick('('), lambda:buttonClick(')'), None, None, ]
for btn in range(0, 4):
    lblc = Label(frames2[btn], text=roundBtnText[btn][0], bg=bgblack, fg=roundBtnText[btn][1], font=("Arial", 7), bd=-3)
    lblc.grid()
    lblcs.append(lblc)
    buttonc = buttonx(btn, loadimage, None)
    buttonc.grid()
for btn in range(0, 22):
    lblb = Label(frames2[btn+4], text=btnlbls1[btn][0], image=btnlbls1[btn][1], bg=bgblack, fg='#b29d41', font=("Arial", 7), bd=-3)
    lblb.grid()
    lblbs.append(lblb)
    buttonb = buttonx(btn+4, photoimages[btn], funcs[btn+4])
    buttonb.grid()
for btn in range(-4, 0):
    buttonarr = Button(framearrow, image=photoimages[btn], command=None,
                  bg=bgblack, activebackground=bgblack, bd=0)
    buttonarr.grid(row=arrowGridData[btn+4][0], column=arrowGridData[btn+4][1], rowspan=arrowGridData[btn+4][2])


#Lower Area buttons
lblas = []
buttons = ('7', '8', '9', 'DEL', 'AC', '4', '5', '6', '\u00D7', '\u00F7', '1', '2', '3', '+', '-', '0', '.', '\u00D710\u02E3', 'Ans', '=')
btnlbls2 = ('CONST',    'CONV',     'CLR',    'INS',        'OFF',
            '┌MATRIX┐', '┌VECTOR┐', '',       'nPr',        'nCr',
            '┌STAT┐',   '┌CMPLX┐',  '┌BASE┐', 'Pol',        'Rec',
            'RND',      'Ran#',     'π',      'DRG \u25B6', 'OFF', )
functions = (lambda:buttonClick('7'), lambda:buttonClick('8'), lambda:buttonClick('9'), backspace,                    Clear, 
             lambda:buttonClick('4'), lambda:buttonClick('5'), lambda:buttonClick('6'), lambda:buttonClick('\u00D7'), lambda:buttonClick('\u00F7'),
             lambda:buttonClick('1'), lambda:buttonClick('2'), lambda:buttonClick('3'), lambda:buttonClick('+'),      lambda:buttonClick('-'),
             lambda:buttonClick('0'), lambda:buttonClick('.'), off,                     lambda:buttonClick('Ans'),    CalculateTask)

for btn in range(0, 20):
    lbla = Label(frames[btn], text=btnlbls2[btn], bg=bgblack, fg='#b29d41', font=("Arial", 7), bd=-10)
    lbla.grid()
    lblas.append(lbla)
    if btn == 3 or btn == 4:
        buttona = button(btn, buttons[btn], functions[btn], bg='#9fb665')
    else:
        buttona = button(btn, buttons[btn], functions[btn])
    buttona.grid(padx=5)


formula = ''
topbar = '              D    Math  \n'
user_input.focus_set()
user_input.bind('<Return>', CalculateTask)
user_input.bind('<Button-1>', edit)
win.bind('<Left>', ArrowClicked)
win.bind('<Right>', ArrowClicked)
win.mainloop()



