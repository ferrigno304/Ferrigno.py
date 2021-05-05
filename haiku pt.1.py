from guizero import *
import matplotlib.pyplot as plt



def grafico():
    f = open(paramA.value, 'r')

    coordX = []
    coordY = []



app = App(title="INTERFACCIA HAIUKU",width=600, height=400 )
etichettaA = Text(app, text="")
paramA = TextBox(app, width=30)

pushA = PushButton(app, text="Genera il tuo haiku",command=grafico, width=60, height=5)
app.display()
