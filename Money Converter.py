import tkinter
from tkinter import *

def usdeurconv():
    val = usd2.get()
    usdval = float(val) / 1.17
    tkinter.Label(root4, text='EUR: '+ str(usdval), font=('Segoe UI', 11)).pack()

def usdeur():
    global root4
    root4 = Toplevel(root)
    root4.geometry('325x325')
    tkinter.Label(root4, text='USD to EUR', font=('Segoe UI', 25)).pack()
    tkinter.Label(root4, text='Enter the amount of money here', font=('Segoe UI', 14)).pack()
    global usd2
    usd2 = tkinter.Entry(root4, width = 27)
    usd2.pack()
    tkinter.Button(root4, text='Get Result', font=('Segoe UI', 11), relief=GROOVE, height=1, width=10, command=usdeurconv).pack()

def eurusdconv():
    val = eur.get()
    usdval = float(val) * 1.17
    tkinter.Label(root3, text='USD: '+ str(usdval), font=('Segoe UI', 11)).pack()

def eurusd():
    global root3
    root3 = Toplevel(root)
    root3.geometry('325x325')
    tkinter.Label(root3, text='EUR to USD', font=('Segoe UI', 25)).pack()
    tkinter.Label(root3, text='Enter the amount of money here', font=('Segoe UI', 12)).pack()
    global eur
    eur = tkinter.Entry(root3, width = 27)
    eur.pack()
    tkinter.Button(root3, text='Get Result', font=('Segoe UI', 11), relief=GROOVE, height=1, width=10, command=eurusdconv).pack()


def convertfromusd():
    val = usd.get()
    vndval = int(val) * 23000
    conv = int(vndval)
    tkinter.Label(root2, text='VND: ' + str(conv), font=('Segoe UI', 11)).pack()

def convert():
    val = vnd.get()
    usdval = float(val) / 23000
    conv = float(usdval)
    tkinter.Label(root1, text='USD: ' + str(conv), font=('Segoe UI', 11)).pack()

def vndusd():
    global root1
    root1 = Toplevel(root)
    root1.geometry('325x325')
    tkinter.Label(root1, text='VND to USD converter', font=('Segoe UI', 17)).pack()
    tkinter.Label(root1, text='Enter the amount of money here', font=('Segoe UI', 12)).pack()
    global vnd
    vnd = tkinter.Entry(root1, width = 27)
    vnd.pack()
    tkinter.Button(root1, text='Get Result', font=('Segoe UI', 11), relief=GROOVE, height=1, width=10, command=convert).pack()


def usdvnd():
    global root2
    root2 = Toplevel(root)
    root2.geometry('325x325')
    tkinter.Label(root2, text='USD to VND converter', font=('Segoe UI', 17)).pack()
    tkinter.Label(root2, text='Enter the amount of money here', font=('Segoe UI', 12)).pack()
    global usd
    usd = tkinter.Entry(root2, width = 27)
    usd.pack()
    tkinter.Button(root2, text='Get Result', font=('Segoe UI', 11), relief=GROOVE, height=1, width=10, command=convertfromusd).pack()

root = tkinter.Tk()
root.title('Money Converter')
root.geometry('350x350') 

tkinter.Label(text="Money Converter", font=('Segoe UI', 23)).pack()
tkinter.Label(text="VND to USD", font=('Segoe UI', 13)).pack()
tkinter.Button(root, text="VND -> USD", font=('Segoe UI', 11), relief=GROOVE, height=1, width=20, command=vndusd).pack()
tkinter.Button(root, text="USD -> VND", font=('Segoe UI', 11), relief=GROOVE, height=1, width=20, command=usdvnd).pack()
tkinter.Button(root, text="USD -> EUR", font=('Segoe UI', 11), relief=GROOVE, height=1, width=20, command=usdeur).pack()
tkinter.Button(root, text="EUR -> USD", font=('Segoe UI', 11), relief=GROOVE, height=1, width=20, command=eurusd).pack()

root.mainloop()
