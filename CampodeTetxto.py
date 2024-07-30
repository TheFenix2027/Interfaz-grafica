from ctypes import resize
from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Entrada")
root.resizable(0,0)

nombre = StringVar()
apellido = StringVar()
saludo = StringVar()

etiqueta1=Label(root, text="Nombre:", bd=4, font=("Candara 10"))
etiqueta1.place(x=10, y=10)

entrada1= Entry(root, textvariable=nombre, bd=5)
entrada1.place(x=170, y=10)

etiqueta2=Label(root, text="Apellido:", bd=4, font=("Candara 10"))
etiqueta2.place(x=10, y=40)

entrada2=Entry(root, textvariable=apellido, bd=5)
entrada2.place(x=170, y=40)

def saludar():
    saludo.set("Hola "+nombre.get()+" "+apellido.get())

boton1=Button(root, text="Saludar", command=saludar, bd=4, font=("Candara 10"))
boton1.place(x=10, y=100)

boton2=Button(root, text="Cerrar", command=root.destroy, bd=4, font=("Candara 10"))
boton2.place(x=100, y=100)

entrada3=Entry(root, bd=4, font=("Candara 10"), textvariable=saludo, state="disable")
entrada3.place(x=70, y=221)
root.mainloop() 