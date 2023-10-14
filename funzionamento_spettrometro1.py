import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import time
import math
from funzioni_fisiche import raggio_di_curvatura, conversione_num_massa, velocità_finale, passaggio, traiettoria

"""		In questo script python si definisce il funzionamento dello spettrometro di massa:			(questa è la prima parte del programma;
		con le funzioni definite nello script 'funzioni fisiche', se ne simula il funzionamento.		 la seconda parte verrà mostrata in un
		Gli isotopi carichi presenti della sorgente dello strumento, con una velocità considerata		 altro script python)
		trascurabile, passando la prima fenditura vengono accelerati dalla differenza di potenziale
		presente tra questa e la seconda fenditura. Una volta superata anche questa, gli isotopi 
		entrano in una regione dove è presente del campo magnetico uniforme: il moto degli stessi 
		fa si che questi siano sottoposti ad una forza di Lorentz che permette loro di curvarne la 
		traiettoria, così da finire il loro percorso impattando su una lastra fotografica.
		Supponendo di conoscere il potenziale e il campo magnetico e che la lastra sia costituita
		da sensori discreti (pixel), la risoluzione di questa dipende da:
			- larghezza della seconda fenditura,
			- grandezza dei sensori/pixel.
		Ogni pixel del rivelatore produce un segnale elettrico proporzionale agli ioni che lo raggiungono,
		così da poter contare il numero di ioni per pixel.

		Consideriamo in tal caso che la differenza di potenziale tra le due fenditure sia deltaV = 1kV,
		che l'intensità del campo magnetico sia B = 0.1T, che la risoluzione dello schermo sia tale da 
		risolvere isotopi con una differenza di numero di massa pari ad deltaA = 1 in un intervallo di
		masse [1, 210] e che ogni isotopo abbia carica +e, data dalla perdita di un elettrone per atomo.
		Si può usare una simulazione Monte Carlo per considerare il numero di isotopi che attraversano la
		seconda fenditura, tra quelli che partono dalla prima.
"""

V = 1000	# costanti
B = 0.1
q = 1.6e-19

"""		Supponiamo che la sorgente e lo spazio tra le due fenditure sia bidimensionale.
		La probabilità di attraversare la seconda fenditura dipende dalla posizione iniziale dell'isotopo
		all'interno della regione tra le fenditure, dalla direzione e dal verso del vettore velocità corrispondente allo stesso.
		Supponiamo quindi di considerare solo gli isotopi che hanno attraversato la prima fenditura: questi si trovano 
<<<<<<< HEAD
		nei pressi di tale apertura una volta superata la stessa. Consideriamo che le dimensioni della
		regione tra le due fenditure siano (20x20)mm^2, che la prima fenditura sia larga 5mm e che la seconda
		sia larga 2mm.
=======
		nei pressi di tale apertura una volta superata la stessa. Consideriamo che la lunghezza della
		regione tra le due fenditure sia 5cm, che la prima fenditura sia larga 4mm e che la seconda
		sia larga 3.18mm.
>>>>>>> 353652e (Added)

		Tramite le funzioni 'passaggio' e 'traiettoria' importate dallo script "funzioni_fisiche", possiamo simulare
		l'attraversamento della seconda fenditura e il successivo percorso semicircolare con impatto sullo schermo
		degli isotopi.

		Analizziamo la distanza dalla fenditura al punto in cui impatta l'isotopo. Consideriamo il range
		di numeri di massa [1, 210] e per ogni valore simuliamo la partenza di 20000 isotopi dalla regione 
		tra le due fenditure.  
"""

isotopo = np.arange(1, 211)
distanze = errori = np.empty(0)
for i in range(210):
	arrivo = np.empty(0)
	for j in range(20000):
		a = passaggio(isotopo[i], V, q)
		b = traiettoria(a, V, B, q)
		if b != 0:
			arrivo = np.append(arrivo, b)		# in questo array teniamo conto solo degli isotopi
								# che hanno attraversato la seconda fenditura
	sum = n = sum2 = 0
	for j in range(len(arrivo)):				# calcoliamo la media delle distanze tra la seconda
		sum = sum + arrivo[j]				# fenditura e il punto d'impatto degli isotopi nella
		n = n + 1					# lastra fotografica. Questo per ogni valore del
								# numero di massa

	distanze = np.append(distanze, sum/n)
	for j in range(len(arrivo)):				# con questo ciclo for calcoliamo l'errore che si ha per 
		sum2 = sum2 + (arrivo[j] - distanze[-1])**2	# ogni distanza tra fenditura e punto d'impatto dell'isotopo
	errori = np.append(errori, np.sqrt(sum2/len(arrivo)))

plt.figure(20)							# rappresentiamo graficamente la distanza media percorsa
fig = plt.gcf()							# da ogni isotopo al variare del numero di massa
fig.set_size_inches(12, 6)
plt.title('Grafico distanza - numero di massa')
plt.xlabel('Numero di massa')
plt.ylabel("Distanza tra fenditura e punto d'impatto dell'isotopo (m)")
plt.errorbar(isotopo, distanze, yerr=errori, color='black')
plt.plot(isotopo, distanze, 'o-')
plt.show()

"""		Ora vediamo cosa succede se modifichiamo il valore dei parametri iniziali, quali la differenza di
		potenziale presente tra le fenditure, l'intensità del campo magnetico e la carica degli isotopi.
		Consideriamo un set di valori per le tre grandezze:

			V = [200, 2000] V
			B = [0.02, 0.2] T
			q = [1.6e-19, 1.6e-18] C

		e come coppie di isotopi consideriamo A = [1, 2, 3], cioè idrogeno, deuterio e trizio.
		Nella regione tra le due fenditure consideriamo 20000 isotopi per ogni valore di numero di massa.
"""

isotopo2 = np.arange(1, 4)
V2 = np.arange(100, 2000, 100)
B2 = np.arange(0.01, 0.2, 0.01)
q2 = np.arange(0.8e-19, 1.6e-18, 0.8e-19)

"""		Supponiamo che B e q rimangano costanti e uguali ai valori precedenti e calcoliamo le distanze
		per ogni A nell'intervallo [1, 3] e per ogni V nell'intervallo [100, 2000].
"""

distanzeV2_1 = distanzeV2_2 = distanzeV2_3 = np.empty(0)
for i in range(len(V2)):
	arrivo1 = arrivo2 = arrivo3 = np.empty(0)
	for j in range(20000):
		a1 = passaggio(isotopo2[0], V2[i], q)
		a2 = passaggio(isotopo2[1], V2[i], q)
		a3 = passaggio(isotopo2[2], V2[i], q)
		b1 = traiettoria(a1, V2[i], B, q)
		b2 = traiettoria(a2, V2[i], B, q)
		b3 = traiettoria(a3, V2[i], B, q)
		if b1 != 0:
			arrivo1 = np.append(arrivo1, b1)
		if b2 != 0:
			arrivo2 = np.append(arrivo2, b2)
		if b3 != 0:
			arrivo3 = np.append(arrivo3, b3)

	sum1 = sum2 = sum3 = n1 = n2 = n3 = 0
	for j in range(len(arrivo1)):
		sum1 = sum1 + arrivo1[j]
		n1 = n1 + 1
	distanzeV2_1 = np.append(distanzeV2_1, sum1/n1)

	for j in range(len(arrivo2)):
		sum2 = sum2 + arrivo2[j]
		n2 = n2 + 1
	distanzeV2_2 = np.append(distanzeV2_2, sum2/n2)

	for j in range(len(arrivo3)):
		sum3 = sum3 + arrivo3[j]
		n3 = n3 + 1
	distanzeV2_3 = np.append(distanzeV2_3, sum3/n3)

"""		Ora supponiamo che siano V e q a rimanere costanti e uguali ai valori precedenti e calcoliamo
		le distanze per A nell'intervallo [1, 3] e per un campo magnetico B con intensità nell'intervallo
		[0.01, 0.2].
"""

distanzeB2_1 = distanzeB2_2 = distanzeB2_3 = np.empty(0)
for i in range(len(B2)):
	arrivo1 = arrivo2 = arrivo3 = np.empty(0)
	for j in range(20000):
		a1 = passaggio(isotopo2[0], V, q)
		a2 = passaggio(isotopo2[1], V, q)
		a3 = passaggio(isotopo2[2], V, q)
		b1 = traiettoria(a1, V, B2[i], q)
		b2 = traiettoria(a2, V, B2[i], q)
		b3 = traiettoria(a3, V, B2[i], q)
		if b1 != 0:
			arrivo1 = np.append(arrivo1, b1)
		if b2 != 0:
			arrivo2 = np.append(arrivo2, b2)
		if b3 != 0:
			arrivo3 = np.append(arrivo3, b3)

	sum1 = sum2 = sum3 = n1 = n2 = n3 = 0
	for j in range(len(arrivo1)):
		sum1 = sum1 + arrivo1[j]
		n1 = n1 + 1
	distanzeB2_1 = np.append(distanzeB2_1, sum1/n1)

	for j in range(len(arrivo2)):
		sum2 = sum2 + arrivo2[j]
		n2 = n2 + 1
	distanzeB2_2 = np.append(distanzeB2_2, sum2/n2)

	for j in range(len(arrivo3)):
		sum3 = sum3 + arrivo3[j]
		n3 = n3 + 1
	distanzeB2_3 = np.append(distanzeB2_3, sum3/n3)

"""		Infine supponiamo che siano V e B a rimanere costanti ai valori precedenti e calcoliamo le
		distanze per A nell'intervallo [1, 3] e per valori di q nell'intervallo [0.8e-19, 1.6e-18].
"""

distanzeq2_1 = distanzeq2_2 = distanzeq2_3 = np.empty(0)
for i in range(len(q2)):
	arrivo1 = arrivo2 = arrivo3 = np.empty(0)
	for j in range(20000):
		a1 = passaggio(isotopo2[0], V, q2[i])
		a2 = passaggio(isotopo2[1], V, q2[i])
		a3 = passaggio(isotopo2[2], V, q2[i])
		b1 = traiettoria(a1, V, B, q2[i])
		b2 = traiettoria(a2, V, B, q2[i])
		b3 = traiettoria(a3, V, B, q2[i])
		if b1 != 0:
			arrivo1 = np.append(arrivo1, b1)
		if b2 != 0:
			arrivo2 = np.append(arrivo2, b2)
		if b3 != 0:
			arrivo3 = np.append(arrivo3, b3)

	sum1 = sum2 = sum3 = n1 = n2 = n3 = 0
	for j in range(len(arrivo1)):
		sum1 = sum1 + arrivo1[j]
		n1 = n1 + 1
	distanzeq2_1 = np.append(distanzeq2_1, sum1/n1)
	
	for j in range(len(arrivo2)):
		sum2 = sum2 + arrivo2[j]
		n2 = n2 + 1
	distanzeq2_2 = np.append(distanzeq2_2, sum2/n2)
	
	for j in range(len(arrivo3)):
		sum3 = sum3 + arrivo3[j]
		n3 = n3 + 1
	distanzeq2_3 = np.append(distanzeq2_3, sum3/n3)

#		Rappresentiamo l'andamento della distanza in funzione di V, B e q

for i in range(3):
	plt.figure(20)
	fig = plt.gcf()
	fig.set_size_inches(12, 6)
	plt.ylabel("Distanza tra la fenditura e il punto d'impatto dell'isotopo (m)")
	lb = ['Idrogeno', 'Deuterio', 'Trizio']
	if i == 0:
		plt.title('Grafico distanza - V')
		plt.xlabel('Differenza di potenziale (V)')
		plt.plot(V2, distanzeV2_1, 'o-', label=lb[0], color='orange')
		plt.plot(V2, distanzeV2_2, 'o-', label=lb[1], color='limegreen')
		plt.plot(V2, distanzeV2_3, 'o-', label=lb[2], color='darkblue')
	elif i == 1:
		plt.title('Grafico distanza - B')
		plt.xlabel('Intensità del campo (T)')
		plt.plot(B2, distanzeB2_1, 'o-', label=lb[0], color='blue')
		plt.plot(B2, distanzeB2_2, 'o-', label=lb[1], color='pink')
		plt.plot(B2, distanzeB2_3, 'o-', label=lb[2], color='purple')
	else:
		plt.title('Grafico distanza - q')
		plt.xlabel("Intensità di carica dell'isotopo (C)")
		plt.plot(q2, distanzeq2_1, 'o-', label=lb[0], color='red')
		plt.plot(q2, distanzeq2_2, 'o-', label=lb[1], color='darkred')
		plt.plot(q2, distanzeq2_3, 'o-', label=lb[2], color='slategrey')
	plt.legend()
	plt.show()
