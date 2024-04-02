import seaborn 

""" 
La  libreria seaborn è una libreria di visualizzazione dei dati Python, che si integra con Pandas e matpolib 
crea grafici, e diagrammi di rappresenttazione
"""

seaborn.load_dataset() 
# permette agli utenti di caricare rapidamente un dataset di esempio dalla libreria e utilizzarlo per analisi e visualizzazione di dati

seaborn.pairplot() 
# funzione che permette di creare facilmente un grafico a matrice di scatterplot per esplorare i dati e individuare eventuali correlazioni tra le variabili

seaborn.heatmap() 
# funzione che permette di creare rapidamente una mappa di calore a due dimensioni per visualizzare i dati e analizzare la correlazione tra le varaibili in un dataframe di Pandas.

seaborn.pairplot()
# Crea grafici a griglia a dispersione che mostrano la relazione bivariata tra coppie di varaibli, si possono individare eventualii correlazioni tra le variabili.



# HEATMAP (mappe di calore)
"""
Mappa di calore: Una heatmap è una rappresentazione grafica bidimensionale dei dati in cui i 
valori sono rappresentati da colori diversi. Le heatmap possono essere utilizzate per 
visualizzare la correlazione tra le diverse caratteristiche di un set di dati. Ad esempio, il 
codice seguente traccia una heatmap della matrice di correlazione per il set di dati Iris
"""

# esempio: 
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
iris_df = seaborn.load_dataset("iris")
corr = iris_df.corr(numeric_only = True)
seaborn.heatmap(corr, annot=True, cmap="YlGnBu")
plt.show()


# GRAFICO A VIOLINO 
"""
Grafico a violino: Un violin plot è una combinazione di boxplot e density plot, dove il box 
rappresenta l'intervallo interquartile e il density plot mostra la distribuzione dei dati. I 
violin plot possono essere utilizzati per confrontare la distribuzione di diverse 
caratteristiche o classi in un set di dati. Ad esempio, il codice seguente traccia un violin 
plot della lunghezza dei sepali per ogni specie nel set di dati Iris:
"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
iris_df = seaborn.load_dataset("iris")
seaborn.violinplot(x="species", y="sepal_length", data=iris_df)
plt.show()


# DENDROGRAMMA
"""
Un dendrogramma è un diagramma che mostra la relazione gerarchica tra oggetti, 
gruppi o cluster. È comunemente usato nell'analisi dei dati, nel clustering e 
nella classificazione per rappresentare visivamente le somiglianze e le differenze
tra gli elementi.

Per creare un dendrogramma, è necessario eseguire un'analisi di clustering 
gerarchico sui dati. Ciò comporta il raggruppamento degli oggetti in base 
alla loro somiglianza o dissimilarità e la successiva fusione di questi gruppi 
in altri più grandi, fino a quando tutti gli oggetti si trovano in un unico cluster.

La struttura gerarchica risultante può essere rappresentata come un diagramma ad 
albero, con i singoli oggetti in basso e i cluster in alto. L'altezza di ogni 
ramo dell'albero rappresenta il grado di dissimilarità tra gli oggetti o i cluster.
"""

