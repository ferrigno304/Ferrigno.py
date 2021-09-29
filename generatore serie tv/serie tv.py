class serietv:

    def __init__(self,titolo,genere,produttore):

        self.titolo = titolo
        self.genere = genere
        self.produttore = produttore
    

    def scheda(self):
        return f'\ntitolo: "{self.titolo}"\n genere: {self.genere}\n produttore: {self.produttore}'
    
giovanni = serietv("La casa di carta","thriller","Alex Pina")

marco = serietv("Lucifer","giallo", "DC" )

print("Il tipo di variabile costruita è:")
print(giovanni)
print(marco)

print("\nLa singola serie tv è:")
print (giovanni.scheda())
print (marco.scheda())

print("\n\naltro metodo per visualizzare le informazioni (__dict__):")

print(giovanni.__dict__)
print(marco.__dict__)
