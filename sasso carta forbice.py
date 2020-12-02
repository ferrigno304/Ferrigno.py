print("come ti chiami?")
nome = input()
print("ciao " + nome)
print("n\nvuoi giocare a morra cinese??")
risposta_scelta1 =["si","no"]
for risposta_scelte1 in risposta_scelta1:
  print(risposta_scelte1)
print("premi 0 per si, oppure 1 per no")
numero_scelto = int(input())
risposta_scelta2 = risposta_scelta1[numero_scelto]
print("hai scelto: " + risposta_scelta2)
risposta_scelta3 = ""
if(risposta_scelta2 == "no"):
   print ("ok, grazie del tuo tempo alla prossima ")

if(risposta_scelta2 == "si"):
   print("ok, allora incominciamo subito")
armi = ["carta","forbici","sasso"]
for arma in armi:
  print(arma)
print("premi 0 per carta, 1 per forbici o 2 per sasso")
numero_scelto2 = int(input())
risposta_scelta3 = armi[numero_scelto2]
print("hai scelto "+ risposta_scelta3)

arma_bot = ""
if(risposta_scelta3 == "carta"):
  arma_bot = "forbice"
if(risposta_scelta3 == "forbice"):
  arma_bot = "sasso"
if(risposta_scelta3 == "sasso"):
  arma_bot = "carta"
print("...anche io ho fatto la mia scelta")
print("\npremi invio per scoprire se hai vinto o meno")
input()
print("io ho scelto "+ arma_bot)
print(nome + " HAI PERSO!!, ritenta sarai più fortunato")


  

