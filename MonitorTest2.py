import Tkinter
from PIL import ImageTk, Image

def _exit(event):
	print("Exit")
	main_window.destroy()

main_window=Tkinter.Tk()
print("yuiop")
w = main_window.winfo_screenwidth()
h = main_window.winfo_screenheight()
main_window.overrideredirect(1)
main_window.geometry("%dx%d+0+0" % (400, 300))
#main_window.bind("<Escape>", _exit)
#main_window.bind("<space>", _exit)
main_window.bind("<Button-1>", _exit)

main_window.mainloop()

