from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Radio Buttons")
root.resizable(0,0)

etiqueta1=Label(root, text="Escriba su número", font=("Candara 10"))
etiqueta1.place(x=20, y=20)

etiqueta2=Label(root, text="Elija la cantidad:", font=("Candara 10"))
etiqueta2.place(x=20, y=50)

boton1=Button(root, text="Cerrar", command=root.destroy, bg="red", font=("Candara 10"))
boton1.place(x=300, y=100)

opcion=IntVar()
num=IntVar()

def operacion():
    numero = int(entrada1.get())
    if opcion.get()==1:
        total = numero*5
    elif opcion.get()==2:
        total = numero*10
    elif opcion.get()==3:
        total = numero*20
    elif opcion.get()==4:
        total = numero*30
    elif opcion.get()==5:
        total = numero*40
    print(f"El total de la operación es: {str(total)}")

entrada1=Entry(root, bd=5)
entrada1.place(x=150, y=20)

x5 = Radiobutton(root, text="x5", value=1, bd=5, variable=opcion)
x5.place(x=20, y=80)

x10 = Radiobutton(root, text="x10", value=2, bd=5, variable=opcion)
x10.place(x=70, y=80)

x20 = Radiobutton(root, text="x20", value=3,  bd=5, variable=opcion)
x20.place(x=120, y=80)

x30 = Radiobutton(root, text="x30", value=4, bd=5, variable=opcion)
x30.place(x=20, y=110)

x40 = Radiobutton(root, text="x40", value=5, bd=5, variable=opcion)
x40.place(x=70, y=110)

boton2=Button(root, text="Realizar operación", command=operacion, bd=5, font=("Candara 10"))
boton2.place(x=20, y=140)

root.mainloop()