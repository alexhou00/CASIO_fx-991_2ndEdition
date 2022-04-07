# -*- coding: utf-8 -*-
'''
Recreated on Sat Apr 10 20:45:09 2021

@author: home168
'''
from tkinter import Tk, IntVar, Label, END, Frame, Button, Text, INSERT, PhotoImage, Scale
from math import sqrt, sin, cos, tan, log10, log, radians
from os import listdir
from decimal import Decimal
import re
from fractions import Fraction

##Initialization
BGBLACK = '#202020'
TEXTBLUE = '#0f3085'
TEXTORANGE = '#b29d41'
BTNGRAY = '#606060'
BTNGREEN = '#9fb665'
SCREENGREEN = '#bad4ba'
screenTextFont = ('CASIO-Font', 16)
screenBarFont = ('Arial', 8)
btnTextFont = ('Arial', 7)
btnNumFont = ('Carlito', 12)
winwidth = 330
winheight = 656

win = Tk()
win.title('CASIO fx-991ES PLUS 2nd edition')
win.resizable(False, False)
win.geometry(str(winwidth)+'x'+str(winheight))
win.overrideredirect(True)
win.attributes('-topmost', 1)
win.configure(bg=BGBLACK)
X = IntVar(value=0)
Y = IntVar(value=0)
canMove = IntVar(value=0)
still = IntVar(value=1)

dragbar = Frame(win, width=50, height=4)
dragbar.configure(bg='black')
dragbar.pack()
logo = PhotoImage(file="images/logo.png")
label = Label(dragbar, image=logo, bd=0, bg=BGBLACK)
label.grid(row=0, column=0)
#solarPanel = Label(dragbar, width=30, height=4, bg=BGBLACK,)
#solarPanel.grid(row=0, column=1)

##Any Simple Button Clicked
def buttonClick(number):
    global formula, user_input, isEqualed, Ans, answer
    if isEqualed:
        edit()
        user_input.delete(1.0,"end")
        Ans = answer
        if number in ('+','-','*','/', '\u00F7', '\u00D7'):
            formula = 'Ans'
        else:
            formula = ''
        isEqualed = False
    
        formula = str(formula) + str(number)
    else:
        formula = user_input.get(2.0, 'end-1c') + str(number)
    user_input.delete(1.0,"end")
    user_input.insert(INSERT, topbar+formula)
    setFont()
    
##Specific Buttons such as SQRT are Clicked 
def buttonClickFunc(functionName):
    global formula, user_input
    formula = str(functionName) + '(' + str(formula) + ')'
    user_input.delete(1.0,"end")
    user_input.insert(INSERT, topbar+formula)
    setFont()
    
#AC    
def Clear(*events):
    global formula
    formula = ''
    user_input.config(state="normal")
    user_input.focus_set()
    user_input.delete(1.0, END)
    user_input.insert(INSERT, topbar)
    setFont()

def backspace():
    global formula, user_input
    formula = str(formula)[:-1]
    user_input.delete(1.0,"end")
    user_input.insert(INSERT, topbar+formula)
    setFont()
    
##Display and Refresh Text on Screen   
def displayText(value):
    user_input.delete(1.0, END)
    user_input.insert(INSERT, topbar+value)
    setFont()
    
## when = is clicked
def CalculateTask(*event):
    global formula, user_input, isEqualed, answer, sd
    #user_input.delete(1.0,"end")
    #user_input.insert(INSERT, formula)
    datum = user_input.get("2.0","2.end")
    try:
        data = datum
        for char in (('\(','('),('[l]','l'),('[s]','s'),('[t]','t'),('[c]','c'),):
            data = re.sub(r'(?<=\d|\)|[XYZ])('+char[0]+')', '*'+char[1], data)
        data = data.replace('\u00D7\u00D7', '??')
        data = data.replace('\u00F7\u00F7', '??')
        data = data.replace('\u00F7', '/')
        data = data.replace('\u00D7', '*')
        data = data.replace('^', '**')
        data = data.replace('\u00b2', '**2')
        data = data.replace('log', 'log10')
        data = data.replace('ln', 'log')
        data = data+')'*(data.count('(')-data.count(')'))
        if angleUnit == 'degree':
            data = radToDeg('sin', data)
            data = radToDeg('cos', data)
            data = radToDeg('tan', data)
        answer = eval(data)
        answer = round(answer, 10)
        answer = float('%s' % float('%.10g' % answer))
        if answer % 1 == 0:
            answer = int(answer)
        elif len(str(Fraction(answer).limit_denominator()))>=10:
            pass
        else:
            answer = Fraction(answer).limit_denominator()
            
        if answer >= 10**10: answer = format_e(Decimal(str(answer)))
        displayText(datum + '\n\n\n'+str(answer))
        formula = str(answer)
        isEqualed = True
        user_input.tag_add('answer', 'end- 1 lines', 'end')
        user_input.tag_config("answer", justify='right')
        
    except SyntaxError:
        if formula != '':
            displayText('Syntax ERROR\n\n[AC]  :Cancel\n[<][>]:Goto')
        else:
            isEqualed = True
        user_input.config(state="disabled")
    except ZeroDivisionError:
        displayText('Math ERROR\n\n[AC]  :Cancel\n[<][>]:Goto')
        user_input.config(state="disabled")
    except TypeError:
        displayText('Syntax ERROR\n\n[AC]  :Cancel\n[<][>]:Goto')
        user_input.config(state="disabled")
    except NameError:
        displayText('Syntax ERROR\n\n[AC]  :Cancel\n[<][>]:Goto')
        user_input.config(state="disabled")
    win.focus_set()
    setFont()
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
        user_input.delete(1.0, 'end')
        user_input.insert(INSERT, topbar+formula)
        
def edit(*event):
    if str(user_input['state']) == 'disabled':
        user_input.config(state='normal')
        user_input.focus_set()
        temp = user_input.get(2.0, '2.end')
        user_input.delete(1.0, 'end')
        user_input.insert(INSERT, topbar+temp)
        setFont()

def format_e(n):
    a = '%E' % n
    return a.split('E')[0].rstrip('0').rstrip('.') + 'E' + a.split('E')[1]

def SD(*event):
    global sd, answer
    sd = 1 - sd

def radToDeg(string, goal):
    if string in goal:
        ind = goal.index(string)
        find = goal[ind:]
        count = 0
        count2 = 0
        for i in find:
            if i == "(":
                count += 1
                count2 += 1
            elif i == ")":
                count -= 1
            if count2 >= 1 and count == 0:
                num = find.index(i)+ind
                goal = goal[:num] + ")" + goal[num:]
                goal = re.sub(string+'\(', string+'(radians(', goal)
                return goal
        return goal
    return goal

def setFont(*event):
    global tags
    #for tag in tags:
    user_input.tag_add('main', '2.0', 'end')
    user_input.tag_config('main', font=screenTextFont)
    user_input.tag_add('shift', '1.0')
    user_input.tag_config('shift', background=TEXTBLUE, foreground=SCREENGREEN)
    user_input.tag_add('alpha', '1.2')
    user_input.tag_config('alpha', background=TEXTBLUE, foreground=SCREENGREEN)
    user_input.tag_add('m', '1.4')
    user_input.tag_config('m', foreground=SCREENGREEN)
    user_input.tag_add('sto', '1.6', '1.9')
    user_input.tag_config('sto', foreground=SCREENGREEN)
    user_input.tag_add('rcl', '1.9', '1.12')
    user_input.tag_config('rcl', foreground=SCREENGREEN)
    user_input.tag_add('stat', '1.13', '1.17')
    user_input.tag_config('stat', foreground=SCREENGREEN)
    user_input.tag_add('cmplx', '1.17', '1.22')
    user_input.tag_config('cmplx', foreground=SCREENGREEN)
    user_input.tag_add('mat', '1.22', '1.25')
    user_input.tag_config('mat', foreground=SCREENGREEN)
    user_input.tag_add('vct', '1.25', '1.28')
    user_input.tag_config('vct', foreground=SCREENGREEN)
    user_input.tag_add('d', '1.29')
    user_input.tag_config('d', background=TEXTBLUE, foreground=SCREENGREEN)
    user_input.tag_add('r', '1.30')
    user_input.tag_config('r', background=SCREENGREEN, foreground=SCREENGREEN)
    user_input.tag_add('g', '1.31')
    user_input.tag_config('g', background=SCREENGREEN, foreground=SCREENGREEN)
    user_input.tag_add('fix', '1.33', '1.36')
    user_input.tag_config('fix', foreground=SCREENGREEN)
    user_input.tag_add('sci', '1.36', '1.39')
    user_input.tag_config('sci', foreground=SCREENGREEN)
    user_input.tag_add('math', '1.40', '1.44')
    user_input.tag_config('math', foreground=TEXTBLUE)
    user_input.tag_add('darrow', '1.45')
    user_input.tag_config('darrow', foreground=SCREENGREEN)
    user_input.tag_add('uarrow', '1.46')
    user_input.tag_config('uarrow', foreground=SCREENGREEN)

    
### Window Drag Starts Here ###
def onLeftButtonDown(event):
    win.attributes('-alpha', scale.get()/500*3)
    X.set(event.x)
    Y.set(event.y)
    canMove.set(1)
    
label.bind('<Button-1>', onLeftButtonDown)

def onLeftButtonUp(event):
    win.attributes('-alpha', scale.get()/100)
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

def changeTransparency(number):
    win.attributes('-alpha', int(number)/100)
    
##Button in the lower frame
def button(x, text, command, bg=BTNGRAY):
    return Button(frames[x], text=text, width=5, command=command, fg='#ffffff', cursor="hand2", 
                  bg=bg, activebackground=bg, activeforeground='#ffffff', font=btnNumFont)

##Button in the upper frame
def buttonx(x, image, command, bg=BGBLACK):
    return Button(frames2[x], image=image, command=command, cursor="hand2", 
                  bg=bg, activebackground=bg, bd=0)


#### MAIN CODE STARTS HERE ####
isEqualed = False
angleUnit = 'degree'
sd = False
Ans = ''
answer = 0
tags = [('shift',), ('alpha'), ('m'), ('sto'), ('rcl'), ('stat'), ('cmplx'), ('mat'), ('vct'), ('d'), ('r'), ('g'), ('fix'), ('sci'), ('math'), ('darrow'), ('uarrow')]

###Frame initized###
frame1 = Frame(win)
frame1.configure(bg=BGBLACK)
frame1.pack()
framebtn = Frame(win)
framebtn.configure(bg=BGBLACK)
framebtn.pack()
frame3 = Frame(framebtn)
frame3.configure(bg=BGBLACK)
frame3.pack(pady=10)
frame2 = Frame(framebtn)
frame2.configure(bg=BGBLACK)
frame2.pack()

#Each frame for every btn
frames = []
for i in range(0,4):
    for j in range(0,5):
        frame = Frame(frame2, bg=BGBLACK)
        frame.grid(row=i, column=j)
        frames.append(frame)
framearrow = Frame(frame3, bg=BGBLACK)
framearrow.grid(row=0, column=2, rowspan=2, columnspan=2)
frames2 = []
for i in range(0,5):
    for j in range(0,6):
        if not((i==0 or i==1) and (j==2 or j==3)):
            frame = Frame(frame3, bg=BGBLACK)
            frame.grid(row=i, column=j)
            frames2.append(frame)
            
### Screen Setup ###

user_input = Text(frame1, bg=SCREENGREEN, bd=10, fg=TEXTBLUE, wrap='none', pady=0, 
                insertwidth=4, insertbackground=TEXTBLUE, width=22, height=5, 
                font=screenTextFont, selectbackground=TEXTBLUE, selectforeground=SCREENGREEN)
user_input.config(font=screenBarFont, width=56, height=8)
isFontCorrect = True
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
roundBtnText = (('SHIFT', TEXTORANGE),('ALPHA', '#d45d89'),('MODE', '#ffffff'),('ON', '#ffffff'))
btnlbls1 = (('SOLVE', None), ('d/dx', None), ('x!', None), ('Σ', None),
            ('', None), ('√', None), ('x³', None), ('', None), ('', None), ('', None),
            ('', None), ('⟵', None), ('Abs', None), ('asin', None), ('acos', None), ('atan', None),
            ('STO', None), ('⟵', None), ('%', None), (',', None), ('', None), ('M-', None))
funcs = [shift, alpha, None, None,
         None, None, None, None,
         None, lambda:buttonClick('sqrt('), lambda:buttonClick('\u00b2'), None, lambda:buttonClick('log('), lambda:buttonClick('ln('),
         lambda:buttonClick('-'), None, None, lambda:buttonClick('sin('), lambda:buttonClick('cos('), lambda:buttonClick('tan('),
         None, None, lambda:buttonClick('('), lambda:buttonClick(')'), SD, None, ]
for btn in range(0, 4):
    lblc = Label(frames2[btn], text=roundBtnText[btn][0], bg=BGBLACK, fg=roundBtnText[btn][1], font=btnTextFont, bd=-3)
    lblc.grid()
    lblcs.append(lblc)
    buttonc = buttonx(btn, loadimage, None)
    buttonc.grid()
for btn in range(0, 22):
    lblb = Label(frames2[btn+4], text=btnlbls1[btn][0], image=btnlbls1[btn][1], bg=BGBLACK, fg=TEXTORANGE, font=btnTextFont, bd=-3)
    lblb.grid()
    lblbs.append(lblb)
    buttonb = buttonx(btn+4, photoimages[btn], funcs[btn+4])
    buttonb.grid()
for btn in range(-4, 0):
    buttonarr = Button(framearrow, image=photoimages[btn], command=None, cursor="hand2", 
                  bg=BGBLACK, activebackground=BGBLACK, bd=0)
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
    lbla = Label(frames[btn], text=btnlbls2[btn], bg=BGBLACK, fg=TEXTORANGE, font=btnTextFont, bd=-10)
    lbla.grid()
    lblas.append(lbla)
    if btn == 3 or btn == 4:
        buttona = button(btn, buttons[btn], functions[btn], bg=BTNGREEN)
    else:
        buttona = button(btn, buttons[btn], functions[btn])
    buttona.grid(padx=5)

scale = Scale(win, length=100, orient="horizontal", showvalue=False, bg=BGBLACK, bd=0, sliderrelief='flat', from_=15, 
              sliderlength=10, width=5, fg=BGBLACK, highlightbackground=BGBLACK, troughcolor='#404040',command=changeTransparency)
scale.pack(pady=2)
scale.set(100)


formula = ''
topbar = 'S A M STORCL STATCMPLXMATVCT DRG FIXSCI Math \u25bc\u25b2\n'

user_input.insert(INSERT, topbar)
user_input.focus_set()
user_input.bind('<Return>', CalculateTask)
user_input.bind('<Button-1>', edit)
user_input.bind_all('<Key>', setFont)

win.bind('<Left>', ArrowClicked)
win.bind('<Right>', ArrowClicked)
setFont()

win.mainloop()



