import Tkinter
import time
from PIL import ImageTk, Image

class Monitor(object):
	
	def __init__(self):
		self.root = Tkinter.Tk()
		self.status = True
		self.minNumberStrips = 5
		self.maxNumberStrips = 15
		self.color = "white"
		self.frecuency = 2
		self.h = self.root.winfo_screenheight()
		self.w = self.root.winfo_screenwidth()
		self.canvas = Tkinter.Canvas(self.root, borderwidth = 0, bg = "black", height = self.h, width = self.w)
		self.strips = []
		
#
#	def openDialog(self):
#		Child()
#
#class Child(object):
#	
#	def __init__(self, arg):
#		#
#		
#
#isStandartParameters = messagebox.askyesno(title = "Properties", message = "")


def reConf(monitorr):
	print(100)
	monitorr.status = not monitorr.status
	for i in range(len(monitorr.strips)):
		monitorr.canvas.delete(monitorr.strips[i])
	print(200)
	if monitorr.status:
		stripH = monitorr.h / 31
		for i in range(15):
			monitorr.strips.append(monitorr.canvas.create_polygon(0, stripH * (2 * i + 1), monitorr.w, stripH * (2 * i + 1), monitorr.w, stripH * (2 * i + 2), 0, stripH * (2 * i + 2), fill = 'white'))
	else:
		stripH = monitorr.h / 11
		for i in range(5):
			monitorr.strips.append(monitorr.canvas.create_polygon(0, stripH * (2 * i + 1), monitorr.w, stripH * (2 * i + 1), monitorr.w, stripH * (2 * i + 2), 0, stripH * (2 * i + 2), fill = 'white'))
	print(300)
	monitorr.root.update()


def rePaint(monitorr):
	print(monitorr.status)
	print(60)
	while True:
		print(70)
		reConf(monitorr)
		print(80)
		time.sleep(1)
		print(90)

def _exit(monitorr):
	print("Exit")
	#monitorr.strips = []
	monitorr.root.destroy()
	exit()




monitor = Monitor()
monitor.root.overrideredirect(1)
monitor.root.geometry("%dx%d+0+0" % (monitor.w, monitor.h))
monitor.root.bind("<Button-1>", lambda e: _exit(monitor))
monitor.canvas.pack()

monitor.root.after(10000, rePaint(monitor))

root.mainloop()

