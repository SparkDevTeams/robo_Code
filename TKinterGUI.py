# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:09:35 2018

@author: Rez
"""

from tkinter import *
import random
import time
import datetime
def keyup(e):
    f2bbaL.config(bg = "white")
    f2babL.config(bg = "white")
    f2bbcL.config(bg = "white")
    f2bcbL.config(bg = "white")
def keydown(e):
    if e.char == 'w':
        f2bbaL.config(bg = "green")
    if e.char == 'a':
        f2babL.config(bg = "green")
    if e.char == 's':
        f2bbcL.config(bg = "green")
    if e.char == 'd':
        f2bcbL.config(bg = "green")
    if e.char == '1':
        ftaal.config(bg = "green")
        ftabl.config(bg = "white")
        ftacl.config(bg = "white")
        ftadl.config(bg = "white")
        ftael.config(bg = "white")
    if e.char == '2':
        ftaal.config(bg = "white")
        ftabl.config(bg = "green")
        ftacl.config(bg = "white")
        ftadl.config(bg = "white")
        ftael.config(bg = "white")
    if e.char == '3':
        ftaal.config(bg = "white")
        ftabl.config(bg = "white")
        ftacl.config(bg = "green")
        ftadl.config(bg = "white")
        ftael.config(bg = "white")
    if e.char == '4':
        ftaal.config(bg = "white")
        ftabl.config(bg = "white")
        ftacl.config(bg = "white")
        ftadl.config(bg = "green")
        ftael.config(bg = "white")
    if e.char == '5':
        ftaal.config(bg = "white")
        ftabl.config(bg = "white")
        ftacl.config(bg = "white")
        ftadl.config(bg = "white")
        ftael.config(bg = "green")
def display(data):
    repr(data)
    sensor = data
    lbl2.config(text = sensor)
#-------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("     Robot Movement GUI     ")
root.configure(background = 'white')
test = StringVar()
sensor = StringVar()


test.set("Change Me!")
Tops = Frame(root, width = 1350, height = 100, bd = 14, relief = "raise")
Tops.pack()
#------------------------------------------------------------------------------------------------------------------------------------------
fl = Frame(root, width = 900, height = 650, bd = 8, relief = "raise")
fl.pack(side = LEFT)
f2 = Frame(root, width = 685, height = 650, bd = 8, relief = "raise")
f2.pack(side = RIGHT)
f2.pack_propagate(0)
lblInfo = Label(Tops, font = ('arial', 70, 'bold'), text = "     Robot Movement GUI     " , bd = 10)
lblInfo.pack()
#------------------------------------------------------------------------------------------------------------------------------------------
fla = Frame(fl, width = 900, height = 100, bd = 4, relief = "raise")
fla.pack(side = TOP, fill = X, expand = True)
fla.pack_propagate(0)
flb = Frame(fl, width = 900, height = 425, bd = 4, relief = "raise")
flb.pack(side = BOTTOM, fill = X, expand = True)
flb.pack_propagate(0)
lbl = Label(fla, font = ('arial', 12, 'bold'), text = "Sensor Data", bd = 4)
lbl.pack(fill = BOTH, expand = True)
lbl.pack_propagate(0)
#-------------------------------------------------------------------------------------------------------------------------------------------
flba = Frame(flb, width = 225, height = 425, bd = 4, relief = "raise")
flba.pack(side = LEFT)
flba.pack_propagate(0)
flbb = Frame(flb, width = 225, height = 425, bd = 4, relief = "raise")
flbb.pack(side = LEFT)
flbb.pack_propagate(0)
flbc = Frame(flb, width = 225, height = 425, bd = 4, relief = "raise")
flbc.pack(side = LEFT)
flbc.pack_propagate(0)
flbd = Frame(flb, width = 225, height = 425, bd = 4, relief = "raise")
flbd.pack(side = LEFT)
flbd.pack_propagate(0)
#-------------------------------------------------------------------------------------------------------------------------------------------
flbaa = Frame(flba, width = 225, height = 85, bd = 4, relief = "raise")
flbaa.pack(side = TOP)
flbba = Frame(flbb, width = 225, height = 85, bd = 4, relief = "raise")
flbba.pack(side = TOP)
flbca = Frame(flbc, width = 225, height = 85, bd = 4, relief = "raise")
flbca.pack(side = TOP)
flbda = Frame(flbd, width = 225, height = 85, bd = 4, relief = "raise")
flbda.pack(side = TOP)


sensor1title = Label(flbaa, font = ('arial', 12, 'bold'), text = "Humidity", bd = 4, bg = "#ADD8E6")
sensor1title.pack()
sensor2title = Label(flbba, font = ('arial', 12, 'bold'), text = "Gas", bd = 4, bg = "yellow")
sensor2title.pack()
sensor3title = Label(flbca, font = ('arial', 12, 'bold'), text = "Ultrasonic", bd = 4, bg = "black", fg = "white")
sensor3title.pack()
sensor4title = Label(flbda, font = ('arial', 12, 'bold'), text = "Water", bd = 4, bg = "#00FFFF")
sensor4title.pack()
#--------------------------------------------------------------------------------------------------------------------------------------------
flbab = Frame(flba, width = 225, height = 335, bd = 4, relief = "raise")
flbab.pack(side = BOTTOM)
flbab.pack_propagate(0)
flbbb = Frame(flbb, width = 225, height = 335, bd = 4, relief = "raise")
flbbb.pack(side = BOTTOM)
flbbb.pack_propagate(0)
flbcb = Frame(flbc, width = 225, height = 335, bd = 4, relief = "raise")
flbcb.pack(side = BOTTOM)
flbcb.pack_propagate(0)
flbdb = Frame(flbd, width = 225, height = 335, bd = 4, relief = "raise")
flbdb.pack(side = BOTTOM)
flbdb.pack_propagate(0)

sensor1data = Label(flbab, font = ('arial', 12, 'bold'), text = "Too Humid", bd = 4)
sensor1data.bind("<KeyPress>", keydown)
sensor1data.bind("<KeyRelease>", keyup)
sensor1data.pack(fill = BOTH)
sensor1data.focus_set()

sensor2data = Label(flbbb, font = ('arial', 12, 'bold'), text = "Nothing is killing you.... yet", bd = 4)
sensor2data.pack()
sensor3data = Label(flbcb, font = ('arial', 12, 'bold'), text = "Everything is far", bd = 4)
sensor3data.pack()
sensor4data = Label(flbdb, font = ('arial', 12, 'bold'), text = "You are drowning", bd = 4)
sensor4data.pack()
#--------------------------------------------------------------------------------------------------------------------------------------------
f2a = Frame(f2, width = 685, height = 130, bd = 8, relief = "raise")
f2a.pack(side = TOP)
f2a.pack_propagate(0)
f2aa = Frame(f2a, width = 130, height = 130, bd = 8, relief = "raise")
f2aa.pack(side = LEFT)
f2aa.pack_propagate(0)
f2ab = Frame(f2a, width = 130, height = 130, bd = 8, relief = "raise")
f2ab.pack(side = LEFT)
f2ab.pack_propagate(0)
f2ac = Frame(f2a, width = 130, height = 130, bd = 8, relief = "raise")
f2ac.pack(side = LEFT)
f2ac.pack_propagate(0)
f2ad = Frame(f2a, width = 130, height = 130, bd = 8, relief = "raise")
f2ad.pack(side = LEFT)
f2ad.pack_propagate(0)
f2ae = Frame(f2a, width = 130, height = 130, bd = 8, relief = "raise")
f2ae.pack(side = LEFT)
f2ae.pack_propagate(0)

ftaal = Label(f2aa, font = ('arial', 24, 'bold'), text = "1", bd = 4, bg = "white", width = 130, height = 130)
ftaal.pack()
ftabl = Label(f2ab, font = ('arial', 24, 'bold'), text = "2", bd = 4, bg = "white", width = 130, height = 130)
ftabl.pack()
ftacl = Label(f2ac, font = ('arial', 24, 'bold'), text = "3", bd = 4, bg = "white", width = 130, height = 130)
ftacl.pack()
ftadl = Label(f2ad, font = ('arial', 24, 'bold'), text = "4", bd = 4, bg = "white", width = 130, height = 130)
ftadl.pack()
ftael = Label(f2ae, font = ('arial', 24, 'bold'), text = "5", bd = 4, bg = "white", width = 130, height = 130)
ftael.pack()
#---------------------------------------------------------------------------------------------------------------------------------------------
f2b = Frame(f2, width = 685, height = 520, bd = 8, relief = "raise")
f2b.pack(side = BOTTOM)
f2b.pack_propagate(0)

f2ba = Frame(f2b, width = 220, height = 520, bd = 8, relief = "raise")
f2ba.pack(side = LEFT)
f2ba.pack_propagate(0)
f2bb = Frame(f2b, width = 220, height = 520, bd = 8, relief = "raise")
f2bb.pack(side = LEFT)
f2bb.pack_propagate(0)
f2bc = Frame(f2b, width = 220, height = 520, bd = 8, relief = "raise")
f2bc.pack(side = RIGHT)
f2bc.pack_propagate(0)

f2baa = Frame(f2ba, width = 220, height = 157, bd = 8, relief = "raise")
f2baa.pack(side = TOP)
f2bab = Frame(f2ba, width = 220, height = 158, bd = 8, relief = "raise")
f2bab.pack(side = TOP)
f2bab.pack_propagate(0)
f2bac = Frame(f2ba, width = 220, height = 157, bd = 8, relief = "raise")
f2bac.pack(side = TOP)

f2bba = Frame(f2bb, width = 220, height = 157, bd = 8, relief = "raise")
f2bba.pack(side = TOP)
f2bba.pack_propagate(0)
f2bbb = Frame(f2bb, width = 220, height = 158, bd = 8, relief = "raise")
f2bbb.pack(side = TOP)
f2bbc = Frame(f2bb, width = 220, height = 157, bd = 8, relief = "raise")
f2bbc.pack(side = TOP)
f2bbc.pack_propagate(0)

f2bca = Frame(f2bc, width = 220, height = 157, bd = 8, relief = "raise")
f2bca.pack(side = TOP)
f2bcb = Frame(f2bc, width = 220, height = 158, bd = 8, relief = "raise")
f2bcb.pack(side = TOP)
f2bcb.pack_propagate(0)
f2bcc = Frame(f2bc, width = 220, height = 157, bd = 8, relief = "raise")
f2bcc.pack(side = TOP)

f2babL = Label(f2bab, font = ('arial', 48, 'bold'), text = "↺", bd = 4, bg = "white", width = 220, height = 158)
f2babL.pack(fill = BOTH)
f2bcbL = Label(f2bcb, font = ('arial', 48, 'bold'), text = "↻", bd = 4, bg = "white", width = 220, height = 158)
f2bcbL.pack(fill = BOTH)
f2bbaL = Label(f2bba, font = ('arial', 48, 'bold'), text = "↑", bd = 4, bg = "white", width = 220, height = 158)
f2bbaL.pack(fill = BOTH)
f2bbcL = Label(f2bbc, font = ('arial', 48, 'bold'), text = "↓", bd = 4, bg = "white", width = 220, height = 158)
f2bbcL.pack(fill = BOTH)

root.mainloop()