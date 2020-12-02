def Risolvi1():
    # Inizio acquisizione elementi di primo grado primo membro
    print("PRIMO MEMBRO:")
    print("Inserire i coefficienti degli elementi di primo grado (Premi invio ogni volta e concludi scrivendo 'fine')")
    coeff1= []
    while True:
        a = input()
        if a == "fine":
            break
        else:
            coeff1.append(int(a))
    sum1m1g = 0
    for i in coeff1:
        sum1m1g += i 
    #Inizio acquisizione termini noti primo membro
    print("Inserire i termini noti al primo membro (Premi invio ogni volta e concludi scrivendo 'fine'")
    tnoti1=[]
    while True:
        b = input()
        if b == "fine":
            break
        else:
            tnoti1.append(int(b))
    sumn1=0
    for i in tnoti1:
        sumn1 += i 

    #Acquisizione elementi di primo grado secondo membro
    print("")
    print("SECONDO MEMBRO")
    print("Inserire i coefficienti degli elementi di primo grado (Premi invio ogni volta e concludi scrivendo 'fine'")
    coeff2= []
    while True:
        c = input()
        if c == "fine":
            break
        else:
            coeff2.append(int(c))
    sum2m1g = 0
    for i in coeff2:
        sum2m1g += i 
    # Inizio acquisizione termini noti primo membro
    print("Inserire i termini noti al primo membro (Premi invio ogni volta e concludi scrivendo 'fine'")
    tnoti2=[]
    while True:
        d = input()
        if d == "fine":
            break
        else:
            tnoti2.append(int(d))
    sumn2=0
    for i in tnoti2:
        sumn2 +=i
    #Risoluzione dell'equazione:
    print(sumn1,sumn2,sum1m1g,sum2m1g)
    return (sumn2-sumn1)/(sum1m1g-sum2m1g)

print("                                          Benvenuto in EquSolver 1.0!")
print("EquSolver permette di risolvere equazioni di primo e secondo grado.")
print("Selezionare il genere di equazione:")
print("1 Equazione di primo grado")
print("2 Equazione di secondo grado")
print("")
tipsel=input()

if tipsel=='1':
    sol = Risolvi1()
    print("La soluzione dell'equazione è ", sol)