from tkinter import *

raiz=Tk()

miframe=Frame(raiz)

miframe.pack()

#-------------------pantalla---------------------------

pantalla=Entry(miframe)
pantalla.grid(row=1,column=1, padx=10, pady=10, columnspan=4) #columnspan hace que la pantalla ocupe 4 columnas
pantalla.config(background="black", fg="#03f943", justify="right",)



#-------------------fila 1-----------------------------

boton7=Button(miframe, text="7", width=3)
boton7.grid(row=2,column=1)


boton8=Button(miframe, text="8", width=3)
boton8.grid(row=2,column=2)

boton9=Button(miframe, text="9", width=3)
boton9.grid(row=2,column=3)

botonDiv=Button(miframe, text="/", width=3)
botonDiv.grid(row=2,column=4)



#-------------------fila 2-----------------------------

boton4=Button(miframe, text="4", width=3)
boton4.grid(row=3,column=1)


boton5=Button(miframe, text="5", width=3)
boton5.grid(row=3,column=2)

boton6=Button(miframe, text="6", width=3)
boton6.grid(row=3,column=3)

botonMult=Button(miframe, text="x", width=3)
botonMult.grid(row=3,column=4)



#-------------------fila 3-----------------------------

boton1=Button(miframe, text="1", width=3)
boton1.grid(row=4,column=1)


boton2=Button(miframe, text="2", width=3)
boton2.grid(row=4,column=2)

boton3=Button(miframe, text="3", width=3)
boton3.grid(row=4,column=3)

botonRest=Button(miframe, text="-", width=3)
botonRest.grid(row=4,column=4)



#-------------------fila 4-----------------------------

boton0=Button(miframe, text="0", width=3)
boton0.grid(row=5,column=1)


botonComa=Button(miframe, text=",", width=3)
botonComa.grid(row=5,column=2)

botonSuma=Button(miframe, text="+", width=3)
botonSuma.grid(row=5,column=3)

botonRest=Button(miframe, text="-", width=3)
botonRest.grid(row=5,column=4)


#-------------------fila 4-----------------------------

botonIgual=Button(miframe, text="=", width=12)
botonIgual.grid(row=6, column=1, columnspan=4)











raiz.mainloop()
