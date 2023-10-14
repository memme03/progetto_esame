# progetto_esame
Questa repository contiene i vari file del progetto richiesto per l'esame

Il contenuto descrive il funzionamento di uno spettrometro di massa, usato per studiare la composizione di un composto. Lo spettrometro è formato da una sorgente contenente gli elementi del composto, due fenditure, una regione compresa tra le due fenditure sottoposta ad una differenza di potenziale, una regione in cui è presente del campo magnetico uniforme e una lastra fotografica.  
Il funzionamento è il seguente:
    - gli isotopi nella sorgente, una volta attraversata la prima fenditura vengono        accelerati dalla differenza di potenziale presente;
    - quelli con un moto approssimativamente lineare vengono selezionati dalla seconda fenditura ed entrano nella regione in cui è presente il campo magnetico;
    - in questa regione il campo magnetico comporta l'applicazione di una forza di Lorentz alle particelle in movimento che ne curva la traiettoria;
    - dopo aver descritto un semicerchio approssimativo, questi atomi finiscono il loro percorso sulla lastra fotografica.

L'utilità di questo strumento è il fatto di poter studiare la composizione di un composto:
gli atomi (o isotopi che siano) con diversa massa in presenza del campo magnetico descrivono dei semicerchi con diverso raggio di curvatura, così da finire in diversi punti dello schermo. La quantità di atomi presenti in quel punto viene mostrata come composizione percentuale del composto in funzione del rapporto carica-massa dell'isotopo/atomo considerato.

Gli script presenti sono tre:
    - funzioni_fisiche.py serve per individuare le funzioni fisiche da utilizzare nei vari casi;
    - funzionamento_spettrometro1.py e funzionamento_spettrometro2.py usano le funzioni definite nel primo script per simulare il funzionamento dello spettrometro e compiere le richieste del progetto.

L'ordine di esecuzione degli script è (per come è stato definito funzioni_fisiche.py, lo si può considerare un modulo e quindi non ha necessità di essere eseguito):
    - funzionamento_spettrometro1.py;
    - funzionamento_spettrometro2.py.

Analizziamo questi file separatamente. Dall'esecuzione del primo script si otterranno dei grafici che rispondono alle prime due richieste del progetto: questi mostrano l'andamento della distanza tra seconda fenditura e punto d'impatto delle particelle sullo schermo dello spettrometro in funzione del numero di massa dell'atomo lanciato, della differenza di potenziale presente tra le due fenditure, dell'intensità del campo magnetico uniforme e della carica delle particelle. Di questi quattro grafici il primo è stato ottenuto con la considerazione di valori costanti di differenza di potenziale, di intensità del campo magnetico e di carica, mentre negli altri tre si sono fatte variare una ad una le grandezze in gioco, considerando nel mentre costanti le altre, e sono state rappresentate le distanze per tre valori diversi di numero di massa, cioè H1, H2, H3 (idrogeno, deuterio e trizio).
Nel secondo script quello che si ottiene sono i grafici che mostrano il punto d'arrivo degli elementi di determinati composti sullo schermo e l'abbondanza isotopica degli stessi nel composto. I composti che sono stati studiati hanno le seguenti composizioni:
    - K39 (93%), K41 (7%);
    - Ir191 (7.4%), Ir197 (12.6%), Pt194 (26.4%), Pt195 (27.2%), Pt196 (20%), Pt198 (5.6%).

L'abbondanza isotopica mostrata nel grafico non è uguale a quella reale per l'utilizzo di funzioni randomiche nello script. Il risultato si può però considerare in buona approssimazione accettabile e simile ai valori reali di percentuale immessi nel codice. Per aumentare la precisione in questo caso si possono aumentare il numero di particelle totali del composto da considerare nello script funzionamento_spettrometro2.py. Inoltre le particelle con stesso numero di massa non cadono tutte alla stessa distanza perché si deve tenere conto anche del fatto che il loro vettore velocità può non essere perpendicolare al piano della seconda fenditura, così da formare variazioni minime nella traiettoria assunta dalla particella in presenza di campo magnetico, che è quindi diversa rispetto a quella che si avrebbe se il vettore velocità fosse perfettamente perpendicolare a tale piano. In tal caso, con una seconda fenditura larga 3.18mm e supponendo che le particelle attraversino una prima fenditura larga 4mm, vi è una probabilità del 2% che una particella superi la seconda fenditura e una probabilità che del 2,5‰ che essa finisca nel punto sbagliato dello schermo dello spettrometro, cioè al di fuori del range di distanza proprio del numero di massa della stessa. Quindi la probabilità totale che una particella ha di finire fuori da questo range di distanza partendo dalla prima fenditura è dello 0.005% circa, un valore molto piccolo per cui la precisione dello strumento si può considerare molto buona.