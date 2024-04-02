
""" 
La funzione map() è una funzione che applica una funzione a cascun elemento di un iterabile 
(come una lista, tupla, set) e restituisce un nuovo iterabile contenete i risultati.

map(funzione, iterabile)

dove funzione è la funzione che si desidera applicare a ogni elemento dell'iterabile
dove iterabile è l'iterabile di cui si desidera applicare la funzione. 

""" 

# es: 

def doppio(x):
    
    return x *2

numeri = [2,4,6]

numeri_quadrati = map(doppio, numeri)

print(list(numeri_quadrati))

# Applica la funzione doppio() su ogni elemento della lista numeri