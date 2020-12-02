nome = input("Come ti chiami?  ")
print("Ciao " + nome)


risposta_scelta = input("\nVuoi concatenare delle parole? (Si/No) ")


if(risposta_scelta == "no" or risposta_scelta == "No"):
   print ("Ok, grazie del tuo tempo alla prossima ")
   exit
elif(risposta_scelta == "si" or risposta_scelta == "Si"):
   print("Ok, allora incominciamo subito")
else:
  print("Scusa non ho capito")
  exit

variabile1 = []
variabile2 = int(input("Quante parole vuoi concatenare? "))

for i in range (variabile2):
  variabile3 = input("Scrivi una parola  ")
  variabile1.append(variabile3)

variabile4 = ""
for nome in variabile1:
  variabile4 = variabile4 + nome
print(variabile4)