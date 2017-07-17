from Tkinter import *
import time
from PIL import ImageTk, Image

class Monitor(object):
	
	def __init__(self):
		self.root = Tk()
		self.root.overrideredirect(0)
		self.slaveWindow = 0
		self.isManyStrips = True
		self.isBlackScreen = True
		self.minNumberStrips = 5
		self.maxNumberStrips = 10
		self.color = "white"
		self.frecuency = 2
		self.h = self.root.winfo_screenheight()
		self.w = self.root.winfo_screenwidth()

		self.canvas = Canvas(self.root, bg = "black", height = self.h, width = self.w)
		self.strips = []
		self.afterStrips = 0
		#self.root.bind("<Button-1>", raiseWindow)
		self.root.geometry("%dx%d+0+0" % (self.w, self.h))

		self.root.bind("<Button-3>", lambda s: _exit(self))
		
		#self.root.bind("<Button-1>", lambda s: self.chageMod())

		self.canvas.pack()

	def renumel(self, typ):
		self.root.after_cancel(self.afterStrips)
		self.root.destroy()
		self.root = Tk()
		self.root.overrideredirect(typ)
		if typ:
			self.root.bind("<Button-1>", lambda s = 0: self.raiseWindow())
		self.h = self.root.winfo_screenheight()
		self.w = self.root.winfo_screenwidth()
		
		self.canvas = Canvas(self.root, bg = "black", height = self.h, width = self.w)
		#self.root.bind("<Button-1>", lambda )
		self.root.geometry("%dx%d+0+0" % (self.w, self.h))

		self.root.bind("<Button-3>", lambda s = 0: _exit(self))

		self.canvas.pack()
		self.strips = []
		self.isBlackScreen = not typ
		print('797878797878')
		
		
		

	def showStrips(self):
		#self.root.tkraise()
		print('55555')
		#self.root.update()
		while not self.isBlackScreen:
			print('777')
			self.isManyStrips = not self.isManyStrips
			
			for i in range(len(self.strips)):
				self.canvas.delete(self.strips[i])
			#self.canvas = Canvas(self.root, bg = "black", height = self.h, width = self.w)
			if self.isManyStrips:
				stripH = self.h / (self.maxNumberStrips * 2 + 1)
				for i in range(self.maxNumberStrips):
					self.strips.append(self.canvas.create_polygon(0, stripH * (2 * i + 1), self.w, stripH * (2 * i + 1), self.w, stripH * (2 * i + 2), 0, stripH * (2 * i + 2), fill = self.color))
			else:
				stripH = self.h / (self.minNumberStrips * 2 + 1)
				for i in range(self.minNumberStrips):
					self.strips.append(self.canvas.create_polygon(0, stripH * (2 * i + 1), self.w, stripH * (2 * i + 1), self.w, stripH * (2 * i + 2), 0, stripH * (2 * i + 2), fill = self.color))

			self.root.update()
			time.sleep(1 / self.frecuency)
		for i in range(len(self.strips)):
			self.canvas.delete(self.strips[i])

	def raiseWindow(self):
		self.renumel(0)
		self.slaveWindow.renumel2(1)
		print('allNew')
		self.root.mainloop()



		
class SlaveWindow(object):
	
	def __init__(self):
		self.monitorRef = monitor
		self.window = Toplevel(self.monitorRef.root)
		self.monitorRef.slaveWindow = self
		self.window.overrideredirect(0)
		self.window.tkraise()
		self.window.title('Configuration')

		self.windowHight = int(self.monitorRef.h / 4)
		self.windowWidth = int(self.monitorRef.w / 2)
		self.windowY = int(self.monitorRef.h * 0.375)
		self.windowX = int(self.monitorRef.w / 4)

		self.labelHight = int(self.windowHight / 5)
		self.labelWidth = int(self.windowWidth / 2)
 		self.labelFont = 'Arial ' + str(self.labelHight - 5)

		self.window.geometry("%dx%d+%d+%d" % (self.windowWidth, self.windowHight, self.windowX, self.windowY))
		self.window.lift(self.monitorRef.root)
		self.color = StringVar(value = 'white')
		self.minNumberStrips = DoubleVar(value = 5)
		self.maxNumberStrips = DoubleVar(value = 15)
		self.frecuency = DoubleVar(value = 2)

		
		self.colorEntry = Entry(self.window, textvariable = self.color, font=self.labelFont, width = self.labelWidth)
		self.minNSEntry = Entry(self.window, textvariable = self.minNumberStrips, font=self.labelFont, width = self.labelWidth)
		self.maxNSEntry = Entry(self.window, textvariable = self.maxNumberStrips, font=self.labelFont, width = self.labelWidth)
		self.frecuencyEntry = Entry(self.window, textvariable = self.frecuency, font=self.labelFont, width = self.labelWidth)
		self.button = Button(self.window, text = 'OK', command = self.useConfiguration)
		self.colorLable = Label(self.window, text = 'Color', font=self.labelFont, height = self.labelHight, width = self.labelWidth)
		self.minNSLable = Label(self.window, text = 'Small number of strips', font=self.labelFont, height = self.labelHight, width = self.labelWidth)
		self.maxNSLable = Label(self.window, text = 'Big number of strips', font=self.labelFont, height = self.labelHight, width = self.labelWidth)
		self.frecuencyLable = Label(self.window, text = 'Frecuence', font=self.labelFont, height = self.labelHight, width = self.labelWidth)

		self.colorEntry.grid(row = 0, column = 1)
		self.colorLable.grid(row = 0, column = 0)
		self.minNSEntry.grid(row = 1, column = 1)
		self.minNSLable.grid(row = 1, column = 0)
		self.maxNSEntry.grid(row = 2, column = 1)
		self.maxNSLable.grid(row = 2, column = 0)
		self.frecuencyEntry.grid(row = 3, column = 1)
		self.frecuencyLable.grid(row = 3, column = 0)
		
		self.button.grid(row = 4)

		
	def renumel2(self, typ):
		
		self.monitorRef = monitor
		self.window = Toplevel(self.monitorRef.root)
		self.monitorRef.slaveWindow = self
		self.window.overrideredirect(0)
		self.window.title('Configuration')
		self.window.geometry("%dx%d+%d+%d" % (int(self.monitorRef.w / 4), int(self.monitorRef.h / 2), int(self.monitorRef.w * 0.375), int(self.monitorRef.h * 0.25)))
		#self.window.lift(self.monitorRef.root)
		self.color = StringVar(value = 'white')
		self.minNumberStrips = DoubleVar(value = 5)
		self.maxNumberStrips = DoubleVar(value = 15)
		self.frecuency = DoubleVar(value = 2)
 
		self.colorEntry = Entry(self.window, textvariable = self.color, font=self.labelFont, width = self.labelWidth)
		self.minNSEntry = Entry(self.window, textvariable = self.minNumberStrips, font=self.labelFont, width = self.labelWidth)
		self.maxNSEntry = Entry(self.window, textvariable = self.maxNumberStrips, font=self.labelFont, width = self.labelWidth)
		self.frecuencyEntry = Entry(self.window, textvariable = self.frecuency, font=self.labelFont, width = self.labelWidth)
		self.button = Button(self.window, text = 'OK', command = self.useConfiguration)
		self.colorLable = Label(self.window, text = 'Color', font=self.labelFont, height = self.labelHight, width = self.labelWidth)
		self.minNSLable = Label(self.window, text = 'Small number of strips', font=self.labelFont, height = self.labelHight, width = self.labelWidth)
		self.maxNSLable = Label(self.window, text = 'Big number of strips', font=self.labelFont, height = self.labelHight, width = self.labelWidth)
		self.frecuencyLable = Label(self.window, text = 'Frecuence', font=self.labelFont, height = self.labelHight, width = self.labelWidth)

		self.colorEntry.grid(row = 0, column = 1)
		self.colorLable.grid(row = 0, column = 0)
		self.minNSEntry.grid(row = 1, column = 1)
		self.minNSLable.grid(row = 1, column = 0)
		self.maxNSEntry.grid(row = 2, column = 1)
		self.maxNSLable.grid(row = 2, column = 0)
		self.frecuencyEntry.grid(row = 3, column = 1)
		self.frecuencyLable.grid(row = 3, column = 0)
		
		self.button.grid(row = 4)
	

	def useConfiguration(self):
		print('567')
		self.monitorRef.color = self.color.get()
		self.monitorRef.minNumberStrips = int(self.minNumberStrips.get())
		self.monitorRef.maxNumberStrips = int(self.maxNumberStrips.get())
		self.monitorRef.frecuency = self.frecuency.get()
		
		print('((((((((((((((((((')
		
		self.monitorRef.isBlackScreen = False
		
		self.monitorRef.renumel(1)
		self.renumel2(0)
		self.monitorRef.afterStrips = self.monitorRef.root.after(1, self.monitorRef.showStrips)
		self.monitorRef.root.mainloop()
		
		print('789')
		

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