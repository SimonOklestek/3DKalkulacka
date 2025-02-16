
from tkinter import *

window = Tk()
list = Listbox(window, font=("arial", 20))
list.insert(1,"Creality")
list.insert(2,"Elegoo")
list.insert(3,"Aurapol")

list.config(height=list.size())




list.pack()
window.mainloop()