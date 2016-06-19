#Health Menu

import sys
from tkinter import *
import tkinter.messagebox
import base64
import urllib
import webbrowser

def check():
		ChecklistLabel = Label(mGui, text = 'Things To Do').pack()


mGui = Tk()

mGui.geometry('500x500+500+300')
mGui.title('Health Menu')

mlabel = Label(mGui, text = 'Heath Menu', fg = 'Red', bg = 'white')  
mlabel.pack()  

Checklist = Button(mGui, text = 'Daily Checklist', command = check).pack(side = LEFT)