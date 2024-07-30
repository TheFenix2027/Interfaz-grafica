from cProfile import label
from tkinter import *

root = Tk()
root.title("Posicionar")
root.geometry("400x200")

label1=Label(root, text="Etiqueta")
label1.grid(row=0, column=0)

boton1=Button(root, text="Boton")
boton1.grid(row=0, column=1)

boton2=Button(root, text="Cerrar", command=root.destroy)
boton2.grid(row=1, column=0)

root.mainloop()