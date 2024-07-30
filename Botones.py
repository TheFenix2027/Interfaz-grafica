from cProfile import label
from tkinter import *
import time

root=Tk()
root.title("Mi primera ventana")
root.geometry("500x300")

boton1 = Button(root, text="Minimizar", command=root.iconify)
boton1.pack()

def imprimir():
    label1 = Label(root, text="Imprimiendo...")
    label1.pack()
boton2 = Button(root, text="Imprimir", command=imprimir)
boton2.pack()

boton3 = Button(root, text="Cerrar", command=root.destroy)
boton3.pack()

root.mainloop()