import numpy as np
import matplotlib.pyplot as plt
import math
from funzioni_fisiche import raggio_di_curvatura, conversione_num_massa, velocità_finale, carica_massa, passaggio, traiettoria, estrazione1, estrazione2

"""		In questo script riprendiamo il funzionamento dello spettrometro di massa e mostreremo
		come ottenere dei grafici delle risposte simulate dello strumento per materiali con 
		una determinata composizione isotopica. Consideriamo gli stessi valori costanti per 
		V, B e q usati precedentemente
"""

V = 1000
B = 0.1
q = 1.6e-19

"""		Dopo aver implementato le funzioni dello script precedente (passaggio e traiettoria) che
		ci permettevano di vedere se l'isotopo considerato superasse la seconda fenditura (la prima)
		e la distanza dalla fenditura alla quale impattavano gli isotopi (la seconda), possiamo 
		simulare l'ottenimento di dati per materiali costituiti da determinati elementi. 
		Il primo che analizziamo è un materiale costituito per il 93% da K39 e per il 7% da K41.

		Simuliamo la partenza degli elementi K39 e K41 dalla sorgente, ipotizzando che il materiale
		sia composto da 500000 isotopi. Oltre a vedere a quale distanza dalla fenditura impattano gli
		isotopi sulla lastra, mostriamo anche l'abbondanza isotopica del composto supponendo di non conoscerla
"""

arrivo1 = arrivo2 = mq = np.empty(0)
isotopi = np.arange(1, 211, 0.5)
sum = 0
n = np.zeros(420)
for i in range(1000000):
	a = estrazione1()
	b = passaggio(a, V, q)
	c = traiettoria(b, V, B, q)
	if b[1] == True:
		mq = np.append(mq, carica_massa(b[0], V, B, q))
		for j in range(len(isotopi)):
			if mq[-1] == carica_massa(isotopi[j], V, B, q):		# usiamo qui un array di confronto per vedere quanti e quali
				n[j] = n[j] + 1					# elementi abbondano di più: se l'elemento i-esimo è presente
				sum = sum + 1					# allora aumentiamo di uno il valore nel corispondente array
	if c != 0:								# delle quantità, indicato con n, dove ogni elemento 
		arrivo1 = np.append(arrivo1, c)					# rappresenta la quantità di isotopi con numero di massa pari ad i
		arrivo2 = np.append(arrivo2, a)

elem = mq1 = np.empty(0)
for i in range(len(n)):
	if n[i] != 0:
		elem = np.append(elem, n[i])
		mq1 = np.append(mq1, carica_massa(isotopi[i], V, B, q)/1000)

for i in range(2):
	img = plt.subplots(1, figsize=(12, 6))
	if i == 0:
		plt.title('Grafico distanza - numero di massa')
		plt.xlabel('Numero di massa')
		plt.ylabel("Distanza fenditura - punto d'impatto (m)")
		plt.plot(arrivo2, arrivo1, 'o', alpha=0.2)
	elif i == 1:
		plt.title('Grafico abbondanza isotopica - rapporto q/m')
		plt.ylabel('Abbondanza isotopica (%)')
		plt.xlabel('Rapporto q/m (C/g)')
		plt.plot(mq1, elem/sum*100, 'o', color='orange')
		plt.plot(carica_massa(isotopi, V, B, q)/1000, n/sum*100, color='blue')
	plt.show()

img, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].set_title('Grafico distanza - numero di massa')
ax[0].set_xlabel('Numero di massa')
ax[0].set_ylabel("Distanza fenditura - punto d'impatto (m)")
ax[0].plot(arrivo2, arrivo1, 'o', alpha=0.2)
ax[1].set_title('Grafico abbondanza isotopica - rapporto q/m')
ax[1].set_ylabel('Abbondanza isotopica (%)')
ax[1].set_xlabel("Rapporto q/m (C/g)")
ax[1].plot(mq1, elem/sum*100, 'o', color='orange')
ax[1].plot(carica_massa(isotopi, V, B, q)/1000, n/sum*100, color='blue')	# dividendo la quantità di isotopi con un determinato valore
plt.show()									# di numero di massa con la quantità totale degli isotopi che
										# hanno attraversato la seconda fenditura si ottiene 
										# l'abbondanza isotopica per quel tipo di isotopi


"""		Ora consideriamo di analizzare un composto costituito da Ir191, Ir197, Pt194, Pt195, Pt196 e Pt198,
		con un numero di isotopi pari a 2x10^6. Con lo stesso procedimento di prima, simuliamo la partenza 
		di questi elementi dalla sorgente, vediamo a quale distanza impattano dalla seconda fenditura e
		troviamo l'abbondanza isotopica per ogni elemento del composto.
"""

arrivo1 = arrivo2 = mq = np.empty(0)
sum = 0
n = np.zeros(420)
for i in range(5000000):
	a = estrazione2()
	if a != 0:
		b = passaggio(a, V, q)
		c = traiettoria(b, V, B, q)
		if b[1] == True:
			mq = np.append(mq, carica_massa(b[0], V, B, q))
			for j in range(len(isotopi)):
				if mq[-1] == carica_massa(isotopi[j], V, B, q):
					n[j] = n[j] + 1
					sum = sum + 1
		if c != 0:
			arrivo1 = np.append(arrivo1, c)
			arrivo2 = np.append(arrivo2, a)

elem = mq1 = np.empty(0)
for i in range(len(n)):
	if n[i] != 0:
		elem = np.append(elem, n[i])
		mq1 = np.append(mq1, carica_massa(isotopi[i], V, B, q)/1000)

for i in range(2):
	img = plt.subplots(1, figsize=(12, 6))
	if i == 0:
		plt.title('Grafico distanza - numero di massa')
		plt.xlabel('Numero di massa')
		plt.ylabel("Distanza fenditura - punto d'impatto (m)")
		plt.plot(arrivo2, arrivo1, 'o', alpha=0.2)
	elif i == 1:
		plt.title('Grafico abbondanza isotopica - rapporto q/m')
		plt.xlabel('Rapporto q/m (C/g)')
		plt.ylabel('Abbondanza isotopica (%)')
		plt.plot(mq1, elem/sum*100, 'o', color='orange')
		plt.plot(carica_massa(isotopi, V, B, q)/1000, n/sum*100, color='blue')
	plt.show()

img, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].set_title('Grafico distanza - numero di massa')
ax[0].set_xlabel('Numero di massa')
ax[0].set_ylabel("Distanza fenditura - punto d'impatto (m)")
ax[0].plot(arrivo2, arrivo1, 'o', alpha=0.2)
ax[1].set_title('Grafico abbondanza isotopica - rapporto q/m')
ax[1].set_xlabel('Rapporto q/m (C/g)')
ax[1].set_ylabel('Abbondanza isotopica (%)')
ax[1].plot(mq1, elem/sum*100, 'o', color='orange')
ax[1].plot(carica_massa(isotopi, V, B, q)/1000, n/sum*100, color='blue')
plt.show()
