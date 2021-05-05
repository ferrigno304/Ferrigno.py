import random 
lista_a = ["notte di luna", "dietro il velo di nubi", "cantan le rane"]
lista_b = ["Fiume di stelle", "Attraversa il buio", "accecandoci"]
lista_c = ["Mare azzurro", "È agitato per via", "Del vento forte"]
 
def estrazione(lista): 
    p=random.randint(0,len(lista)-1) 
    x=lista[p] 
    lista.remove(x) 
    return x 
  
x=estrazione(lista_a) 
y=estrazione(lista_b)
z=estrazione(lista_c)

print (x)
print (y)
print (z)
