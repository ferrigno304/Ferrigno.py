Stringa = sorted((input("Scrivi una parola --> ")).upper())
Dict_Letters = {}
for i in Stringa:
    if i not in Dict_Letters:
        Dict_Letters[i] = 1
    else:
        Dict_Letters[i] += 1
massimo = max(Dict_Letters.values())
maggiori = []
intermedio = " "
for Key in Dict_Letters:
    if Dict_Letters[Key] == massimo:
            maggiori.append(Key)
Intermedio = " "
print(f"Le lettere che appaiono più spesso sono{Intermedio.join(Dict_Letters)}")
