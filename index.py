from tkinter import *

top =Tk()

top.geometry("800x500")
top.title("Notepad")

menubar=Menu(top)

fileMenu=Menu(menubar,tearoff=0)
editMenu=Menu(menubar,tearoff=0)
formateMenu=Menu(menubar,tearoff=0)
viewMenu=Menu(menubar,tearoff=0)
helpMenu=Menu(menubar,tearoff=0)


menubar.add_cascade(label="File",menu=fileMenu)
menubar.add_cascade(label="Edit",menu=editMenu)
menubar.add_cascade(label="Formate",menu=formateMenu)
menubar.add_cascade(label="View",menu=viewMenu)
menubar.add_cascade(label="Help",menu=helpMenu)


fileMenu.add_command(label="New")
fileMenu.add_command(label="New Window")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save As")
fileMenu.add_separator()
fileMenu.add_command(label="Page Setup")
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")

editMenu.add_command(label="Undo")
editMenu.add_separator()
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")
editMenu.add_command(label="Delete")
editMenu.add_separator()
editMenu.add_command(label="Search with Bing")
editMenu.add_command(label="Find...")
editMenu.add_command(label="Find Next")
editMenu.add_command(label="Find Previous")
editMenu.add_command(label="Replace...")
editMenu.add_command(label="Find Go To..")
editMenu.add_separator()
editMenu.add_command(label="Select All")
editMenu.add_command(label="Time/Date")

formateMenu.add_command(label="Word Wrap")
formateMenu.add_command(label="Font...")

viewMenu.add_command(label="Zoom")
viewMenu.add_command(label="Status Bar")

helpMenu.add_command(label="View Help")
helpMenu.add_command(label="Send Feedback")
helpMenu.add_separator()
helpMenu.add_command(label="About Notepad")

text=Text(top,bd=0)
text.pack()

top.config(menu=menubar)


top.mainloop()