import Tkinter
from PIL import ImageTk, Image


main_window=Tkinter.Tk()

c = Canvas(tk, width=600, height=400)
c.pack()
img = PhotoImage(file="/home/ilja/park/MonitorTest.png")
c.create_image(0, 0, image=img, anchor="nw")

main_window.mainloop()