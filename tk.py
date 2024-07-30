from tkinter import *

ventana = Tk()
ventana.geometry("500x300")

texto = Label(ventana, text="Hola Mundo", bg="yellow")
texto.pack()

boton1=Button(ventana,text="Cerrar", command=ventana.destroy)
boton1.pack()

ventana.mainloop()