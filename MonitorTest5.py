from tkinter import *
from tkinter import ttk

root = Tk()
color = StringVar()
frecuency = IntVar()
numberStr = IntVar()
lab_1 = Label(root, text = "Enter frecuency", width = 25, height = 3, justify = CENTER, font = "188").grid(row = 0, column = 0)
enter_1 = Entry(root, textvariable = frecuency, width = 25, justify = CENTER, font = "188").grid(row = 0, column = 1)
lab_2 = Label(root, text = "Enter color", width = 25, height = 3, justify = CENTER, font = "188").grid(row = 1, column = 0)
enter_2 = Entry(root, textvariable = color, width = 25, justify = CENTER, font = "188").grid(row = 1, column = 1)
lab_3 = Label(root, text = "Enter number strings", width = 25, height = 3, justify = CENTER, font = "188").grid(row = 2, column = 0)
enter_3 = Entry(root, textvariable = numberStr, width = 25, justify = CENTER, font = "188").grid(row = 2, column = 1)

root.mainloop()