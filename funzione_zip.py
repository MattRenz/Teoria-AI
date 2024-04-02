"""  
La funzione zip() in python serve per unire due o più sequenze (liste, tuple, set, etc..) 
in un unica sequenza di tuple, contenete gli elementi corrispondenti delle sequenze originali 

"""

numeri1 = [1, 2, 3, 4, 5]
numeri2 = [10, 20, 30, 40, 50]

# Si usa la funzione zip per unire le due liste in una lista di tuple contenente gli elementi corrispondenti

numeri_uniti = zip(numeri1, numeri2)

# <[(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]>