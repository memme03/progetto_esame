import numpy as np
<<<<<<< HEAD
=======
import math
>>>>>>> 7b5229e (Modified)

"""		in questo script sono presenti le equazioni da utilizzare nel progetto. Le principali sono quelle corrispondenti a:
			- velocità finale della particella all'istante dell'impatto sullo schermo
			- raggio di curvatura della particella sotto l'influenza del campo magnetico
			- rapporto carica-massa della particella in esame
			- conversione del numero di massa della particella in massa effettiva della stessa
"""

def velocità_finale(m, V, q):
	return np.sqrt(2*q*V/m)

def raggio_di_curvatura(m, V, B, q):
	return np.sqrt((2*m*V)/(q*B**2))

def carica_massa(nm, V, B, q):
	massa = conversione_num_massa(nm)
	raggio = raggio_di_curvatura(massa, V, B, q)
	return 2*V/(raggio**2*B**2)

def conversione_num_massa(m):
	rapporto = 1/(6.022e23)
	return m*rapporto/1000

"""		Definiamo altre equazioni utili al nostro scopo. Qui sotto vi è una funzione che definisce il numero di isotopi che
		attraversano la seconda fenditura. Teniamo conto che la lunghezza supposta della regione tra le fenditure sia di
		5cm, della prima fenditura larga 4mm e della seconda larga 3.18mm. Il parametro iniziale che si immette è il 
		numero di massa dell'isotopo considerato di cui si vuole studiare l'andamento all'interno della regione tra le fenditure.
		Dopo aver convertito tale numero in massa dell'isotopo, la sua conoscenza ci permette di calcolare la velocità che
		l'isotopo ha in vicinanza della seconda fenditura. Tali operazioni si possono compiere con le equazioni definite in
		precedenza. I risultati che si ottengono dalla funzione sono:

			- la massa dell'isotopo;
			- una variabile booleana che indica se l'isotopo abbia attraversato o meno la fenditura;
			- l'angolo che si viene a formare tra la perpendicolare alla fenditura e il vettore velocità dell'isotopo
			  stsso.
"""

def passaggio(m_isotopo, V, q):
	y = np.random.uniform(low=-0.002, high=0.002)
	m_isotopo2 = conversione_num_massa(m_isotopo)
	vel = velocità_finale(m_isotopo2, V, q)
<<<<<<< HEAD
	velx = np.random.uniform(low=0, high=vel)
	vely = np.sqrt(vel**2 - velx**2)
	yf = y + vely*(0.05/velx)
	alpha = np.arctan(vely/velx)
=======
	alpha = np.random.uniform(low=-math.pi/2, high=math.pi/2)
	velx = vel*np.cos(alpha)
	vely = vel*np.sin(alpha)
	yf = y + vely*(0.05/velx)
>>>>>>> 7b5229e (Modified)
	attraversamento = False
	if -0.00159 < yf < 0.00159:
		attraversamento = True
	return m_isotopo, attraversamento, alpha

"""		Successivamente definiamo una funzione che descrive la traiettoria degli isotopi che hanno superato la seconda fenditura.
		Si deve tenere conto del fatto che i vettori velocità degli isotopi possono non essere perpendicolari a tale fenditura e
		che quindi, una volta superatala, il loro moto può non descrivere un semicerchio perfetto. Però gli angoli presenti per
		gli isotopi che attraversano la seconda fenditura sono molto piccoli e non influenzano in maniera significativa il loro
		moto. Tale funzione sfrutta i codici della funzione precedente che permette di ottenere in maniera semplice il raggio di
		curvatura degli isotopi. I parametri da immettere nella funzione corrisponde ad un array che contiene la massa
		dell'isotopo, la variabile booleana col significato definito nella precedente funzione e l'angolo che si viene a formare
		tra la perpendicolare alla fenditura e il vettore velocità dell'isotopo stesso, la differenza di potenziale presente tra
		le due fenditure, l'intensità del campo magnetico e la carica dell'isotopo considerato. Il risultato che si ottiene,
		invece, è un valore che indica la distanza tra fenditura e punto d'impatto dell'isotopo nella lastra fotografica.
"""

def traiettoria(info, V, B, q):
	if info[1] == True:
		m_isotopo = conversione_num_massa(info[0])
		raggio = raggio_di_curvatura(m_isotopo, V, B, q)
		distanza_impatto = raggio*np.cos(info[2])*2
		return distanza_impatto
	else:
		return 0

"""		Ora definiamo una funzione che simula la partenza dallo spettrometro di due elementi di un composto formato da K39 per
		il 93% e K41 per il 7%.
"""

def estrazione1():
	isotopo = 0
	c = np.random.random()*100
	if c < 93:
		isotopo = 39
	else:
		isotopo = 41
	return isotopo

"""		Infine definiamo una funzione che simula la partenza dallo spettrometro di sei elementi appartenenti ad un composto
		con queste percentuali:
			- Ir191 --> 7.4%
			- Ir197 --> 12.6%
			- Pt194 --> 26.4%
			- Pt195 --> 27.2%
			- Pt196 --> 20%
			- Pt198 --> 5.6%
"""

def estrazione2():
	isotopo = 0
	c = np.random.random()*100
	if c < 7.4:
		isotopo = 191
	elif 7.4 <= c < 20:
		isotopo = 197
	elif 20 <= c < 46.4:
		isotopo = 194
	elif 46.4 <= c < 73.6:
		isotopo = 195
	elif 73.6 <= c < 93.6:
		isotopo = 196
	elif 93.6 <= c < 99.2:
		isotopo = 198
	else:
		isotopo = 0
	return isotopo
