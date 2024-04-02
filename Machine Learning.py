# Machine Learning Supervisionato / Non supervisionato / Cluestering (Raggrppamento)

"""
Machine Learning Supervisionato: 
Tecnica di apprendimento automatico, che prevede l'utilizzo di dati training (dati di cui si conosce già il risultato atteso)
per addestrare un modello matematico che sarà in grado di effetturare previsioni su dati non ancora visti


Regressione: Serie di punti che cerco di calcolare se questi punti soddisfando una certa tendenza, 
Capire dove staranno questi punti. Per esempio addestrarlo a prevedere il prezzo di un'abitazione in base alle sue caratteristiche


Classificassione: Poter individurae una categoria di utenti per distribuire il prodotto in modo ottimale, 
per esempio addestrarlo a dstinguere tra immagini di gatti e immagini di cani
graficizzazione dei risultai aiuta a fare ciò.



Machine Learning Non Supervisionato:
L'algoritmo deve lavorare su dati non etichettati, ovvero dati che non sono categorizzati o classificati in alcun modo


Clustering (Raggruppamento):
quando i gruppi non sono noti a priori ma devono essere appresi dal dataset, per esempio un supermercato con 1000 clienti, se osserviamo
i dati di questi 1000 clienti sono tutti diversi, ma possiamo dividerli in 4 o 5 gruppi. Per esempio l'anziano che compra poche cose, 
o le persone che fanno la spesa per tutta la settimana il sabato ecc.. L'obbeittivo della cluster analysis è individuare questi gruppi
e passare da 1000 a 4 o 5 unità. I gruppi non sono noti, ma vanno appresi dai dati. 
Si chiama Market basket analysis (è quel processo di analisi di affinità che analizza le abitudini di acquisto dei clienti nella vendita 
al dettaglio, trovando associazioni su diversi prodotti comprati, tale processo è utile per l'adozione di strategie di marketing ad hoc.)

"""

# Machine Learning 

"""  
L'uso del computer è quello di implementare algoritmi che eseguono procedure. 
dato un input x e una funziona nota F siamo il computer per calcolare F(x) ovvero y

Un esempio di ciò è quando facciamo il bilglietto del treno, inseriamo dei dati (x)
l'outpt (y) è il biglietto, e F la procedura che ci porta da x a y


Il Machine Learning ha come punto di partenza i cosidetti Big Data, ci occuppiamo di come estrarre informazioni utili dai Big Data, 
una serie di problematiche sono associate all gestione fisica di GRANDI masse di dati

"""


# Regressione Lineare e Coefficente di relazione (R)
""" 
La regressione lineare utilizza la relazione che c'è tra i punti dati (presenti nel grafico) per tracciare una linea retta
attraverso tutti loro

la regressione infatti è proprio quando si tenta di trovare una RELAZIONE tra le variabili 
Nel machine lerning questa relazione viene usata per prevenire l'avvenimento di eventi futuri


Come abbiamo detto prima la regressione lineare avvine se c'è una relazione tra le variabili. 
Se non ci sono relazione tra le variabili la regressione lineare non può prevedere nulla

Il coefficente di relazione è chiamato R, può assumere i seguenti valori: 
0 = nessuna relazione 
-1 a 1 = 100% correlato

più si avvicina a zero, più c'è una pessima relazione 
più si avvicina a -1 o a 1 più c'è una possibile relazione
"""