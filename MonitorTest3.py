from Tkinter import *
import time
from PIL import ImageTk, Image

class Monitor(object):
	
	def __init__(self):
		self.root = Tk()
		self.root.overrideredirect(0)
		self.isManyStrips = True
		self.isBlackScreen = True
		self.minNumberStrips = 5
		self.maxNumberStrips = 15
		self.color = "white"
		self.frecuency = 2
		self.h = self.root.winfo_screenheight()
		self.w = self.root.winfo_screenwidth()
		self.canvas = Canvas(self.root, borderwidth = 0, bg = "black", height = self.h, width = self.w)
		self.strips = []

		#self.root.overrideredirect(True)
		self.root.geometry("%dx%d+0+0" % (500, 500))

		self.root.bind("<Button-3>", lambda s: _exit(self))
		#self.root.bind("<Button-1>", lambda s: _exit(self))
		self.root.bind("<Button-1>", lambda s: self.chageMod())

		self.canvas.pack()

	def chageMod(self):
		self.isBlackScreen = not self.isBlackScreen
		self.showStrips()

	def showStrips(self):
		while not self.isBlackScreen:
			#print(100)
			self.isManyStrips = not self.isManyStrips
			for i in range(len(self.strips)):
				self.canvas.delete(self.strips[i])
			#print(200)
			if self.isManyStrips:
				stripH = self.h / 31
				for i in range(15):
					self.strips.append(self.canvas.create_polygon(0, stripH * (2 * i + 1), self.w, stripH * (2 * i + 1), self.w, stripH * (2 * i + 2), 0, stripH * (2 * i + 2), fill = 'white'))
			else:
				stripH = self.h / 11
				for i in range(5):
					self.strips.append(self.canvas.create_polygon(0, stripH * (2 * i + 1), self.w, stripH * (2 * i + 1), self.w, stripH * (2 * i + 2), 0, stripH * (2 * i + 2), fill = 'white'))
			#print(300)
			self.root.update()
			time.sleep(1)
		for i in range(len(self.strips)):
			self.canvas.delete(self.strips[i])


		
class SlaveWindow(object):
	
	def __init__(self):
		self.monitorRef = monitor
		self.window = Toplevel(self.monitorRef.root)
		self.monitorRef.root.overrideredirect(0)
		self.window.title('Configuration')
		self.window.geometry('400x500+20+20')
		stripsC = StringVar()
 
		message_entry = Entry(textvariable=message)
		message_entry.place(relx=.5, rely=.1, anchor="c")
		 
		message_button = Button(text="Click Me", command=show_message)
		message_button.place(relx=.5, rely=.5, anchor="c")

		


def reConf(monitorr):
	monitorr.isManyStrips = not monitorr.isManyStrips
	for i in range(len(monitorr.strips)):
		monitorr.canvas.delete(monitorr.strips[i])
	#print(200)
	if monitorr.isManyStrips:
		stripH = monitorr.h / 31
		for i in range(15):
			monitorr.strips.append(monitorr.canvas.create_polygon(0, stripH * (2 * i + 1), monitorr.w, stripH * (2 * i + 1), monitorr.w, stripH * (2 * i + 2), 0, stripH * (2 * i + 2), fill = 'white'))
	else:
		stripH = monitorr.h / 11
		for i in range(5):
			monitorr.strips.append(monitorr.canvas.create_polygon(0, stripH * (2 * i + 1), monitorr.w, stripH * (2 * i + 1), monitorr.w, stripH * (2 * i + 2), 0, stripH * (2 * i + 2), fill = 'white'))
	#print(300)
	monitorr.root.update()
	

def _exit(monitorr):
	print("Exit")
	monitorr.root.destroy()
	exit()




monitor = Monitor()
slaveWindow = SlaveWindow()

monitor.root.mainloop()








#monitor.canvas.tk_focusFollowsMouse()
#monitor.canvas.focus()
#monitor.canvas.focus_force()
#monitor.canvas.focus_set()
#print(monitor.root.focus_get())