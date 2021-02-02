from guizero import *
import matplotlib.pyplot as plt


def grafico():
    f = open(paramA.value, 'r')

    coordX = []
    coordY = []

    # da notare che posso fare un ciclo all'interno di un file
    # direttamente sulle righe

    for riga in f:
        valori = str(riga)  # converto in stringa la riga
        Nval = len(valori)          # conto il numero di caratteri
        valori = valori.strip('\n') # elimino i lterminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y
    f.close()  # chiudiamo il file
    coordX.sort()
    coordY.sort()
    plt.scatter(coordX,coordY)
    plt.ylabel('some numbers')
    plt.show()


app = App(title="INTERFACCIA GRAFICA",width=400, height=75 )
etichettaA = Text(app, text="Leggi File")
paramA = TextBox(app, width="fill")

pushA = PushButton(app, text="Genera grafico",command=grafico, width="fill")
app.display()
