from tkinter import *
from tkinter import ttk

root = Tk()
desigion_1 = IntVar()
desigion_1.set(1)
Radiobutton(root, text = "Default settings", value = 1, variable = desigion_1, width = 50, height = 3, justify = CENTER, font = "188").pack()
Radiobutton(root, text = "Manually configure", value = 2, variable = desigion_1, width = 50, height = 3, justify = CENTER, font = "188").pack()
root.mainloop()