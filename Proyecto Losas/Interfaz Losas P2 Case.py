from tkinter import *
import tkinter
raiz = Tk()
raiz.title("Proyecto Losas")
raiz.config(bg="black")
frame_1=Frame(raiz)
frame_1.pack(fill="both")
frame_1.config(bg="black", width="800", height="500")
texto_bienvenida=Label (frame_1, text="¡Bienvenido a X!", font="20", fg="white", bg="black")
texto_bienvenida.place(x=335, y=220)
indicacion_inicial=Label (frame_1, text="Pulse siguiente para continuar", font=15, fg="white", bg="black", justify="center")
indicacion_inicial.place(x=300, y=270)
def siguiente ():
    raiz.withdraw()
    frame_2=tkinter.Toplevel(bg="black", width="800", height="500")
    tx_cantidad_losas=Label (frame_2, text="Seleccione la cantidad de Losas", font="20", fg="white", bg="black")
    tx_cantidad_losas.place(x=250, y=100)
    tx_cantidad_losas_comedor=Label (frame_2, text="Comedor y Hab.", font="20", fg="white", bg="black")
    tx_cantidad_losas_comedor.place(x=50, y=300)
    tx_cantidad_losas_baño=Label (frame_2, text="Baño", font="20", fg="white", bg="black")
    tx_cantidad_losas_baño.place(x=300, y=300)
    tx_cantidad_losas_bajo_losa=Label (frame_2, text="Bajo Losa", font="20", fg="white", bg="black")
    tx_cantidad_losas_bajo_losa.place(x=450, y=300)
    tx_cantidad_losas_voladizo=Label (frame_2, text="Voladizo", font="20", fg="white", bg="black")
    tx_cantidad_losas_voladizo.place(x=650, y=300)                   #Si intento modificar los entrys antes del el boton, este se borra
    entrada_comedor=Entry(frame_2, font="20", fg="Black", bg="white")
    entrada_comedor.place(x=30, y=350)
    entrada_losas_b=Entry(frame_2, font="20", fg="Black", bg="white")
    entrada_losas_b.place(x=225, y=350)
    entrada_bajo_l=Entry(frame_2, font="20", fg="Black", bg="white")
    entrada_bajo_l.place(x=410, y=350)
    entrada_vol=Entry(frame_2, font="20", fg="Black", bg="white")
    entrada_vol.place(x=600, y=350)
    def siguiente2 ():
        raiz.withdraw()
        frame_3=tkinter.Toplevel(bg="black", width="800", height="500") 
        def switch ():
            switcher=[
                1:if int(entrada_comedor.get()) >= 1 : #Mismo proceso para todos
                     for numero_de_losas in range (1, int(entrada_comedor.get())): #Nota: Con el ciclo While crashea
                         tx_cantidad_losas_comedor=Label (frame_3, text="Losas de Comedor y Hab", font="20", fg="white", bg="black")
                         tx_cantidad_losas_comedor.place(x=100, y=50)
                2:



                ]











        if int(entrada_comedor.get()) >= 1 : #Mismo proceso para todos
            for numero_de_losas in range (1, int(entrada_comedor.get())): #Nota: Con el ciclo While crashea
                tx_cantidad_losas_comedor=Label (frame_3, text="Losas de Comedor y Hab", font="20", fg="white", bg="black")
                tx_cantidad_losas_comedor.place(x=100, y=50)
                def siguiente3():
                     raiz.withdraw()
                     frame_3=tkinter.Toplevel(bg="black", width="800", height="500") 
                     tx_cantidad_losas_comedor=Label (frame_3, text="Losas de Comedor y Hab", font="20", fg="white", bg="black")
                     tx_cantidad_losas_comedor.place(x=100, y=50)
                boton_siguiente3=Button(frame_3, text="Siguiente", fg="white", command= siguiente3)
                boton_siguiente3.place(x=700, y=400)
                boton_siguiente3.pack

            else:
             tx_cantidad_losas_baño=Label (frame_2, text="Losas de Baño", font="20", fg="white", bg="black")
             tx_cantidad_losas_baño.place(x=100, y=50)
    boton_siguiente2=Button(frame_2, text="Siguiente", fg="white", command= siguiente2)
    boton_siguiente2.place(x=700, y=400)
    boton_siguiente2.pack
boton_siguiente=Button(frame_1, text="Siguiente", fg="white", command= siguiente)
boton_siguiente.place(x=700, y=400)
boton_siguiente.pack
raiz.mainloop ()