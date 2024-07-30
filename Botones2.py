from distutils import command
import tkinter as tk
from tkinter import Label, ttk

root = tk.Tk()
root.geometry("500x300")

def seleccionar(opcion):
    print(opcion)

ttk.Button(root, text="Carro", command=lambda: seleccionar("Carro")).pack()
ttk.Button(root, text="Motor", command=lambda: seleccionar("Motor")).pack()
ttk.Button(root, text="Avión", command=lambda: seleccionar("Avión")).pack()
ttk.Button(root, text="Cerrar", command=root.destroy).pack()

root.mainloop()