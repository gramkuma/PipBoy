#Tkinter Menumaking
#Author: Sharknado, Too
#Date: 3/29/15
#Version: 1.7

import sys
from tkinter import *
import tkinter.messagebox
import base64
import urllib
import webbrowser

class Room:
	name = "none"
	north = "none"
	south = "none"
	west = "none"
	east = "none"
	searchable = False
	searchLoc1 = ""
	item1 = ""
	searchLoc2 = ""
	item2 = ""
	searchLoc3 = ""
	item3 = ""
	available = False
	
	def __init__(self, title, n, s, e, w, search, loc1, ite1, loc2, ite2, loc3, ite3, avail):
		self.name = title
		self.north = n
		self.south = s
		self.west = w
		self.east = e
		self.searchable = search
		self.searchLoc1 = loc1
		self.item1 = ite1
		self.searchLoc2 = loc2
		self.item2 = ite2
		self.searchLoc3 = loc3
		self.item3 = ite3
		self.available = avail

def plotThickens():
	Wow = Label(mGui, text = 'You are really inquisitive... ', fg = 'red').pack()
	
def functionception():
	Denial = Label(mGui, text = 'Thank you for clicking ', fg = 'red').pack()
	anotherButton = Button(mGui, text = 'Do you really want to click again?', command = plotThickens).pack()    # Layering functions
	
def EntryBox():
	box = Entry(mGui, textvariable = whining).pack()
	submitButton = Button (mGui, text = 'Submit' , command = submit).pack()
	
def submit():
	resultsButton = Button(mGui, text = 'Would you like to see our response?', command = response).pack()
	
def response():
	OutofIdeasLabel = Label(mGui, text =' "The text has not been read in." ' ).pack()

def really():
	anotherLabell = Label(mGui, text =' See the about menu ', fg = 'salmon4' ).pack()

def about():
	tkinter.messagebox.showinfo(title = "About", message = " This is currently a test to ensure that there are different kinds of message boxes we can incorporate. This program is to show that implementing a menu is easy to do!")
	return 
	
def fire():
	tkinter.messagebox.showwarning(title = "WARNING", message = "This is just a test!")
	return

def josiah():
	answer = tkinter.messagebox.askyesno(title = "Survey", message = "Are you enjoying our program so far?")
	if answer > 0:
		answerDeux = follow = tkinter.messagebox.askyesno(title = "Response", message = "Thank you for your response!")
		if answerDeux > 0:
			tkinter.messagebox.showinfo(title = "Response", message = "What are you still doing here?")
		if answerDeux == 0:
			tkinter.messagebox.showinfo(title = "Response", message = "You can exit now....")
	if answer == 0:
		tkinter.messagebox.showinfo(title = "Response", message = "I am sorry you had to go through this then.")

def bmap():
	photo = PhotoImage ( file = "bus.png")
	ImageLabel = Label(mGui, image = photo)
	ImageLabel.pack()
def web():
	Google = "www.google.com"
	webbrowser.open(Google)	
mGui = Tk()

mGui.geometry('500x500+500+300')
mGui.title('First Tkinter Try')

whining = StringVar()

mlabel = Label(mGui, text = 'Main Menu', fg = 'Green')  
mlabel.pack()    #Can use grid or pack but no difference....

thebutton = Button(mGui, text = 'Click here!', command = functionception, fg = 'red', bg = 'goldenrod').pack()

complaints = Button(mGui, text = 'Comments, Questions, Concerns, Complaints?', command = EntryBox, fg = 'dark orchid', bg = 'light sky blue').pack()

# MAKING THE MENU

menubar = Menu(mGui)

filemenu = Menu(menubar)
filemenu.add_command(label = "File")
filemenu.add_command(label = "New")
filemenu.add_command(label = "Open")
filemenu.add_command(label = "Open Recent")
filemenu.add_command(label = "Save")
filemenu.add_command(label = "Save As")
filemenu.add_command(label = "Close All")
filemenu.add_command(label = "Quit")

menubar.add_cascade(label = "General Options", menu = filemenu,)

#Help Menu
helpmenu = Menu(menubar)
helpmenu.add_command(label = "More Help", command = really)
helpmenu.add_command(label = "Warning!", command = fire)
helpmenu.add_command(label = "About", command = about)

menubar.add_cascade(label = "Help", menu = helpmenu,)

#Questions Menu
QandAmenu = Menu(menubar)
QandAmenu.add_command(label = "Questionnaire", command = josiah)

menubar.add_cascade(label = "Questions", menu = QandAmenu)

# Locations and Images
ImageMenu = Menu(menubar)
ImageMenu. add_command(label = "Map of Boulder", command = bmap)
ImageMenu. add_command(label = "Google", command = web)

menubar.add_cascade(label = "Location and Services", menu = ImageMenu)

mGui.config(menu = menubar)      #This makes the name appear on the bar up top

mGui.mainloop()
