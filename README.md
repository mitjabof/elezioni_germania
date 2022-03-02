# elezioni_germania
Modello predittivo della coalizione di governo basato sulle differenze programmatiche ex manifesto-project

File contenuti:
- mpgermany.xlsx: subset del database 2021a di Manifesto Project (https://manifesto-project.wzb.eu/)
- mpgermany_script.py

Manifesto Project categorizza ogni unità semantica (quasi-sentence) presente nei programmi politici di ogni ogni partito avente ottenuto almeno un seggio alla Camera bassa
in oltre 50 Paesi dal 1945. Le variabili del database solo la percentuale di quasi-sentences per tipologia di statement politico (e.g. "per101 = 1.79" significa che l'1.79%
delle quasi-sentences del programma politico del partito sono state catalogate come statement relativi a "Foreign Special Relationships: Positive"). Si veda il codebook
a https://manifesto-project.wzb.eu/down/data/2021a/codebooks/codebook_MPDataset_MPDS2021a.pdf .

Lo script tratta ogni partito come un punto in uno spazio n-dimensionale (con n = numero di variabili "posizionali ideologiche"); Vengono considerate 3 possibili coalizioni 
di governo (+1, "coalizione di sinistra", priva però di maggioranza assoluta): Traffic Light (SPD + Greens + FDP), Jamaica (CDU + Greens + FDP), Grand Coalition (CDU + SPD);
Viene individuato un baricentro ideologico (punto nello spazio n-dimensionale avente coordinate medie tra i partiti facenti parte della coalizione); Viene calcolata la distanza
dei singoli partiti dal baricentro, per dare la cifra di quanto ogni partito debba "cedere" in un governo di coalizione; viene fornita una somma delle distanze dei partiti dal
baricentro di coalizione.
Quanto quest'ultimo dato può essere impiegato come proxy della propensione alla formazione di una coalizione?

RISULTATI:

COALIZIONE: Distanza totale

['SPD', 'G', 'FDP'] :  19.35025738588404 (Traffic Light)

['CDU', 'G', 'FDP'] :  21.202163586735086 (Jamaica)

['CDU', 'SPD'] :  14.48513890164675 (Grand Coalition)

['SPD', 'G', 'LINKE'] :  18.330898427661197 (Sinistra)
