from contextlib import contextmanager
from tkinter import *
import tkinter
raiz = Tk()
raiz.title("Proyecto Losas")
raiz.config(bg="black")
frame_1=Frame()
frame_1.pack(fill="both")
frame_1.config(bg="black", width="800", height="500")
texto_bienvenida=Label (frame_1, text="¡Bienvenido a X!", font="20", fg="white", bg="black")
texto_bienvenida.grid(row=1, column=1)
indicacion_inicial=Label (frame_1, text="Pulse siguiente para continuar", font=15, fg="white", bg="black", justify="center")
indicacion_inicial.place(x=300, y=270)
def close_window ():
        frame_1.destroy()
def siguiente ():
    close_window
    frame_2=Frame(bg="black", width="800", height="500")
    frame_2.pack(fill="both", side="top")
boton_siguiente=Button(frame_1, text="Siguiente", fg="white", command= siguiente)
boton_siguiente.place(x=700, y=400)
boton_siguiente.pack
raiz.mainloop ()
