import matplotlib.pyplot as plt 

#Una libereria per la creazione di grafici e visualizzazioni di dati. 

plt.show() # Serve per mostrare i grafici 

plt.title() # Il titolo del grafico 

plt.xlabel() # testo sull'asse X

plt.ylabel() # testo sull'asse Y

plt.legend(["", ""]) #legenda grafici

fig, ax = plt.subplot() 
# semplifica la creazione di una figura e un set di assi voti per i sottografi, fornendo un interfaccia semplice e flessibile. 



# GRAFICO A DISPERSIONE / scatter() 

""" 
I grafici a dispersione vengono usati per osservare la relazione tra le variabili
utlizzando i punti per rappresentare la relazione tra di esse.

"""
plt.scatter()  # scatter accetta 2 valori (x,y) dove x e y sono i punti che andrà a disegnare

x = [5, 10, 30]
y = [20, 40, 60]

plt.scatter(x,y, c="red") # c= "" è il colore dei punti
plt.show()



# GRAFICO A DISPERSIONE CASALE / plot()
""" 
Per testare più dati su un algoritmo possiamo usare numpy per la creazione di dati casuali
"""
import numpy

x = numpy.random.normal(5.0, 1.0, 200) # creiamo 500 valori sull'asse X saranno concentrati su 5 e "lontani" da 1.0
y = numpy.random.normal(10.0, 2.0, 200) #creiamo 500 valori sull'asse Y saranno concentrati su 10.00 e "lontani" da 2.0

plt.scatter(x, y) # avremo una concetnrazione di punti sull'asse X a 5 e sull'asse Y a 10

plt.show()



# GRAFICO A LINEE / plot() 

""" 
I dati sono rappresentati come una serie di punti connessi da linee
"""

plt.plot() # grrafico a linee

x = [1, 2, 3, 4, 5, 7, 8]
y = [2, 4, 6, 8, 10, 20, 10]

plt.plot(x, y)

""" Tipi di linee 

-- = tratteggiata
: = ....
:- = --.--.--.
or- = punti e linee

c = "colori"
b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white
"""
plt.show()


# GRAFICO A BARRE / bar()

""" 
La funzione bar() viene usata per tracciare un grafico a barre rappresenta
la categoria di dati con barre rettangolari e con lunghezze e altezze proporzionali 
ai valori che rappresentano (che diamo noi)
"""

citta_x = ["Roma", "Napoli", "Milano", "Firenze"]
popolazione_y = [2.873,1.352,0.972130,0.382258]

plt.bar(citta_x,popolazione_y, color="maroon", width=0.6)

# color = "colore" // width = 0.5 grandezza delle barre

plt.show()


