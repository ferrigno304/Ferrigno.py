while True:
    print('''
    Benvenuto al programma calcolatrice!
    
    
        print('\nHai Scelto: Sottrazione\n')
        a = float(input('Inserisci il Primo Numero -> '))
        b = float(input('Inserisci il Secondo Numero -> '))
        print('Il risultato della Sottrazione è: ' + str(a - b))
    elif scelta == "3":
        print('\nHai scelto: Moltiplicazione\n')
        a = float(input('Inserisci il Primo Numero -> '))
        b = float(input('Inserisci il Secondo Numero -> '))
        print('Il risultato della Moltiplicazione è: ' + str(a * b))
    elif scelta == "4":
        print('\nHai scelto: Divisione\n')
        a = float(input('Inserisci il Primo Numero -> '))
        b = float(input('Inserisci il Secondo Numero -> '))
        print('Il risultato della Divisione è: ' + str(a / b))
    elif scelta == "5":
        print('\nHai scelto: Calcolo Esponenziale\n')
        a = float(input('Inserisci la Base -> '))
        b = float(input('Inserisci l\'Esponente -> '))
        print('Il risultato del Calcolo Esponenziale è: ' + str(a ** b))
    elif scelta == "ESC":
        print('''L'applicazione verrà ora chiusa!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        break

    loop = input('\nDesideri continuare ad usare l\'applicazione? S/N ')
    if loop == "S" or loop == "s":
        print('''Sto tornando al Menù principale!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        continue
    else:
        print('''Grazie e arrivederci!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        break
