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
    sensor1data.config(text = "Not dead", bg = "white", fg = "black")
def keydown(e):
    if e.char == 'w':
        sensor1data.config(text = "Forward")
    if e.char == 'a':
        sensor1data.config(text = "Left")
    if e.char == 's':
        sensor1data.config(text = "Backward")
    if e.char == 'd':
        sensor1data.config(text = "Right")
    if e.char == '1':
        sensor1data.config(text = "Speed 1")
    if e.char == '2':
        sensor1data.config(text = "Speed 2")
    if e.char == '3':
        sensor1data.config(text = "Speed 3")
    if e.char == '4':
        sensor1data.config(text = "Speed 4")
    if e.char == '5':
        sensor1data.config(text = "Speed 5")
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
sensor2data = Label(flbbb, font = ('arial', 12, 'bold'), text = "Nothing is killing you", bd = 4)
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
f2ab = Frame(f2a, width = 130, height = 130, bd = 8, relief = "raise")
f2ab.pack(side = LEFT)
f2ac = Frame(f2a, width = 130, height = 130, bd = 8, relief = "raise")
f2ac.pack(side = LEFT)
f2ad = Frame(f2a, width = 130, height = 130, bd = 8, relief = "raise")
f2ad.pack(side = LEFT)
f2ae = Frame(f2a, width = 130, height = 130, bd = 8, relief = "raise")
f2ae.pack(side = LEFT)
root.mainloop()