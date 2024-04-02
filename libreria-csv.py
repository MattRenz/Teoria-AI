import csv

# LETTURA FILE CSV con reader() e next()

fileProva = "fileTest.csv"

with open(fileProva, "r") as file:
    
    reader = csv.reader(file) # con csv.reader() leggiamo un file CSV
    
    primariga = next(reader) # con next() andaimo avanti la riga del file
    secondariga = next(reader)
    




    
 