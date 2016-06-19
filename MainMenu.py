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
def functionception():
	Denial = Label(mGui, text = 'Thank you for clicking ', fg = 'red').pack()
	anotherButton = Button(mGui, text = 'Do you really want to click again?', command = plotThickens).pack()    # Layering functions
def initArray():
	output = []
	
	FrontPorch = Room("Front Porch", "none", "Back Hall", "Front Hall", "none", False, "","","","","","", True)
	FrontHall = Room("Front Hall", "Upstairs", "Kitchen", "Living Room", "Front Porch", False, "","","","","","",True)
	Upstairs = Room("Upstairs", "Attic", "Front Hall", "Master Bedroom", "Guest Bedroom", False, "","","","","","", True)
	GuestRoom = Room("Guest Bedroom", "none", "none", "Upstairs", "Guest Bathroom", False, "","","","","","", True)
	GuestBath = Room("Guest Bathroom", "none", "none", "Guest Bedroom", "none", True, "Cabinet","House Key","Toilet","Nothing","Sink","Faulty Faucet", True)
	BackHall = Room("Back Hall", "Front Porch", "Mud Room", "none", "none", False, "","","","","","", False)
	StudyRoom = Room("Study Room", "none", "Secret Room", "none", "Living Room", True, "Bookshelf", "Nothing of Interest", "Desk", "Catacomb Key", "Drake's New Album", "Fire Place", False)
	LivingRoom = Room("Living Room", "none", "none", "Study Room", "Front Hall", False, "", "", "", "", "", "", True)
	SecretRoom = Room("Secret Room", "Study Room", "none", "none", "Back Porch", False, "","","","","","",True)
	BackPorch = Room("Back Porch", "Kitchen", "none", "none", "none", False, "","","","","","",True)
	DeathTrap = Room("Death Trap", "none", "none", "none", "none", False, "","","","","","",True)
	Kitchen = Room("Kitchen", "Front Hall", "Back Porch", "Death Trap", "none", False, "","","","","","",True)
	MasterBed = Room("Master Bedroom", "none", "none", "none", "Upstairs", True, "Dresser", "Study Room Key", "Desk", "Nothing", "Pillows", "Nothing", True)
	Attic = Room("Attic", "none", "Upstairs", "Death Trap", "Death Trap", False, "","","","","","",True)
	MudRoom = Room("Mud Room", "Back Hall", "Catacomb Entry Hall", "none", "none", False, "","","","","","",True)
	Catacombs = Room("Catacomb Entry Hall", "Mud Room", "Burial Hall", "none", "none", False, "","","","","","",False)
	BurialRoom = Room("Burial Hall", "Catacomb Entry Hall", "Sewage Letout", "Empty Coffin Room", "Closed Coffin Room", False, "","","","","","",True)
	CoffinRoom1 = Room("Empty Coffin Room", "Death Trap", "none", "Dead End", "Burial Hall", False, "","","","","","",True)
	DeadEnd = Room("Dead End", "none", "none", "none", "Empty Coffin Room", False, "","","","","","",True) 
	CoffinRoom2 = Room("Closed Coffin Room", "none", "Death Trap", "Death Trap", "Death Trap", False, "","","","","","",True)
	SewageLetout = Room("Sewage Letout", "Burial Hall", "Vigil Room", "Princess Cage Room", "Death Trap", False, "","","","","","",True)
	VigilRoom = Room("Vigil Room", "Sewage Letout", "Death Trap", "Death Trap", "Death Trap", True, "Skeleton", "Princess Cage Room Key", "Mug", "Blood", "Noise", "Death Grips Album", True)
	PrincessCageRoom = Room("Princess Cage Room", "none", "none", "none", "none", False,"","","","","","",False)
	
	
	Rooms = [FrontPorch, FrontHall, Upstairs, GuestRoom, GuestBath, BackHall, StudyRoom, LivingRoom, SecretRoom, BackPorch,
	 DeathTrap, Kitchen, MasterBed, Attic, MudRoom, Catacombs, BurialRoom, CoffinRoom1, DeadEnd, CoffinRoom2, SewageLetout, VigilRoom, PrincessCageRoom]
	return Rooms
	 
def Main():
	inputCounter = 0
	arrayRooms = initArray()
	input1 = ""
	tempRoom = arrayRooms[0]
	while input1 != "quit" and tempRoom.name != "Death Trap" and tempRoom.name != "Princess Cage Room":
		inputCounter += 1
		print ("========================================================")
		print ("You are in the", tempRoom.name + ".")	
		input1 = input ("Choose any of the Cardinal directions (n, s, e, w) or search.\n")
		#submitFunction()
		if (tempRoom.north == "none" and input1 == "n"):
			print ("Direction not available, try again")
			
		elif (tempRoom.south == "none" and input1 == "s"):
			print("Direction not available, try again")
			
		elif (tempRoom.east == "none" and input1 == "e"):
			print("Direction not available, try again")
			
		elif(tempRoom.west == "none" and input1 == "w"):
			print("Direction not available, try again")
			
		elif(tempRoom.searchable == False and input1 == "search"):
			print ("Searching is not an option here")
			
		elif(tempRoom.searchable == True and input1 == "search"):
			input2 = input("You look around, there are three items of interest.\n Which do you look at? (1, 2, 3 or back)")
			if (input2 == "1"):
				print ("You found the " + tempRoom.item1 + "!")
				unlockRoom(arrayRooms, tempRoom.item1)	
			elif (input2 == "2"):
				print ("You found the " + tempRoom.item2 + "!")
				unlockRoom(arrayRooms, tempRoom.item2)
			elif (input2 == "3"):
				print ("You found the " + tempRoom.item3 + "!")
				unlockRoom(arrayRooms, tempRoom.item3)
			
				
		elif (tempRoom.north != "none" and input1 == "n"):
			tempRoom = findRoom(arrayRooms, tempRoom.north)
			if (tempRoom.available == False):
				print ("Hmm... This route appears to be locked at the moment")
				tempRoom = findRoom(arrayRooms, tempRoom.south)
				
		elif (tempRoom.south != "none" and input1 == "s"):
			tempRoom = findRoom(arrayRooms, tempRoom.south)
			if (tempRoom.available == False):
				print ("Hmm... This route appears to be locked at the moment")
				tempRoom = findRoom(arrayRooms, tempRoom.north)
				
		elif (tempRoom.east != "none" and input1 == "e"):
			tempRoom = findRoom(arrayRooms, tempRoom.east)
			if (tempRoom.available == False):
				print ("Hmm... This route appears to be locked at the moment")
				tempRoom = findRoom(arrayRooms, tempRoom.west)
				
		elif(tempRoom.west != "none" and input1 == "w"):
			tempRoom = findRoom(arrayRooms, tempRoom.west)
			if (tempRoom.available == False):
				print ("Hmm... This route appears to be locked at the moment")
				tempRoom = findRoom(arrayRooms, tempRoom.east)
			
	if(tempRoom.name == "Death Trap"):
		print ("Oh no! Your path lead to a Death Trap!")
		print ("You have perished and will need to start over.")
	elif(tempRoom.name == "Princess Cage Room"):
		print ("Congratulations! You found the Princess!")
		print ("Thank you for playing, Winner.")
	print ("========================================================")
	print ("We Hope you had fun!")
	print ("Your total number of inputs was: " + str(inputCounter))
	print ("Goodbye!")
	
	#return (output)

def findRoom(array, title):
	for i in range (0, len(array)):
		if (title == array[i].name):
			return array[i]
def unlockRoom(array, title):
	if (title == "House Key"):
		array[5].available = True
		print ("This looks like the key needed to unlock the Back Hall!")
	elif (title == "Study Room Key"):
		array[6].available = True
		print ("This looks like the key needed to unlock the Study Room!")
	elif (title == "Drake's New Album"):
		print ("a.k.a Drake's New Album")
	elif (title == "Death Grips Album"):
		print ("a.k.a Noise")
	elif (title == "Catacomb Key"):
		array[15].available = True
		print ("This looks like the key needed to unlock the Catacombs!")
	elif (title == "Princess Cage Room Key"):
		array[len(array)-1].available = True
		print ("This looks like the key needed to unlock the Princess!")
		print ("Simply find the room she is hiding in and you will win!!")

def traverseBox():
	root = Tk()
	root.title("Dungeon Game")
	Northbutton = Button(root, text = 'Go North', command = north, fg = 'goldenrod', bg = 'green').pack()
	Southbutton = Button(root, text = 'Go South', command = south, fg = 'goldenrod', bg = 'green').pack()
	Eastbutton = Button(root, text = 'Go East', command = east, fg = 'goldenrod', bg = 'green').pack()
	Westbutton = Button(root, text = 'Go West', command = west, fg = 'goldenrod', bg = 'green').pack()
def north():
	stringvar = 'n'
	return stringvar
def south():
	stringvar = 's'
	return stringvar
def east():
	stringvar = 'e'
	return stringvar
def west():
	stringvar = 'w'
	return stringvar
def OnClick():
	global userData
	userData = entry.get()
	root.destroy()
	return userData
def submitFunction():
	root = Tk()
	root.title("Dungeon Game")
	submitButton = Button(root, text = "Choose any of the Cardinal directions (n, s, e, w) or search.\n", command = OnClick).pack()
	root.focus_set()
	root.mainloop()
	return userData
	
canvas_width = 1200
canvas_height = 680

mGui = Tk()
mGui.title("Pip - Boy")

canvas = Canvas( width = canvas_width, height = canvas_height)

canvas.pack()

photo = tkinter.PhotoImage(file = 'fallout3logo.png')

canvas.create_image(650,320, image = photo)



thebutton = Button(mGui, text = 'Dungeon Game!', command = Main, fg = 'goldenrod', bg = 'green')
button1_window = canvas.create_window(10,10, anchor = NW, window = thebutton)

timebutton = Button(mGui, text = 'Time Options',fg = 'goldenrod', bg = 'green')
timebutton_window = canvas.create_window(500,25, window = timebutton)

quitbutton = Button(mGui, text = 'Quit Button',fg = 'goldenrod', bg = 'green')
quitbutton_window = canvas.create_window(900,25,window = quitbutton)

menubar = Menu(canvas)

filemenu = Menu(canvas)
filemenu.add_command(label = "File")

mGui.mainloop()
