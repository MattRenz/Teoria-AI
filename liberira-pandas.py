import pandas
import matplotlib.pyplot as plt

""" 
Pandas è una libreria per la manipolazione di dati in fomrato sequneziale o tabbellare. 

pandas.read_csv(file)
Permette di leggere file CSV e convertiri in un DataFrame (una struttura dati tabbellare bidimensionale)


Tramite questi dati possiamo usare la libreria matplotlib.pyplot per creare un grafico a Dispersione
che accetta due valori plt.scatter(x, y) dove x e y sono i punti che andrà a disegnare
"""

file = ""
data = pandas.read_csv(file)

plt.scatter(data['x'], data['y'])
plt.show()


"""
Come caricare vari formati di dati in python
"""

# CSV
df = pandas.read_csv('data.csv')

df = pandas.read_csv(file, sep=",", header=None) 

# file è il file csv
# sep= specifica il separatore del file csv
# header= prima riga di intestazione, None nel caso il file csv non c'è l'abbia

# Excel
df = pandas.read_excel('data.xlsx')

# JSON
df = pandas.read_json('data.json')

# Normale file di testo
with open('data.txt', 'r') as f:
    data = f.read()


from pandas import DataFrame

# DataFrame struttura dati bidimensionale e tabulare 
# costituita da colonne e righe. Simile a una tabella di folgio di calcolo

# Esempio di dati
data = {'Nome': ['Alice', 'Bob', 'Charlie'],
        'Età': [25, 30, 35],
        'Città': ['Roma', 'Milano', 'Napoli']}

df = DataFrame(data) # in questo modo creiamo il DataFrame

df.head("n") # restituisce le prime n righe del Dataframe. Se non specificato restituisce le prime 5 di default

df.tail("n") # restiuisce le prime n righe del DataFrame. Se non specificato restituisce le prime 5 di default

df.info() # restituisce un riepilogo del DataFrame, num righe, tipi di da dati, memoria.

# Esempio (print) sul nostro DataFrame: 
    #     Nome  Età   Città
    # Data columns (total 3 columns):
    #    Column  Non-Null Count  Dtype
    # ---  ------  --------------  -----
    #  0   Nome    3 non-null      object
    #  1   Età     3 non-null      int64
    #  2   Città   3 non-null      object
    # dtypes: int64(1), object(2)
    # memory usage: 204.0+ bytes


df.describe() # calcola statistiche di base per le colonne numeriche del DataFrame

df.describe().max() # massimo 
df.describe().min() # minimo
df.describe().mean() # media
# ecc ecc

df.shape # restituisce una tupla contenenre il numero di righe e il numero di colonne

df.columns.tolist() # restituisce l'elenco dei nomi delle colonne di un DF (i labels) 
# Esempio: ['Nome', 'Eta', 'Città']


df.columns # restiuisce una lista contenente un elenco delle colonne del DataFrame

df.dtypes # restituisce i tipi di dati delle colonne del DataFrame

df.loc # [row_labe, col_labe] permette di specificare un subset di dati specificando righe e colonne

# MUOVERSI TRA RIGHE E COLONNE

df.loc [1:, 'Nome', 'Città'] # Risultato: 
# 1      Bob   30  Milano
# 2  Charlie   35  Napoli

# Perchè gli diciamo parti da 1 (riga) e dicci Nome e Città (colonne)


df.iloc # [row_labe, col_label] stesso principio di prima, solo che possiamo muoverci atraverso gli indici di righe e colonne

df.iloc[1,1:] # Esempio:

# Età 30
# Città Milano

# Questo perchè 1 è la riga ('Bob') e 1: la colonna (parti da 1 colonna 1 cioè le città e dimmi il resto) quindi 30 e milano

