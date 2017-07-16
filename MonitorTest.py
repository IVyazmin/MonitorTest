import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
frame = tk.Frame(root)
frame.grid()
combobox = ttk.Combobox(frame,values = [u"ONE",u"TWO",u"THREE"],height=3)

combobox.set(u"ONE")
combobox.grid(column=0,row=0)
root.mainloop()