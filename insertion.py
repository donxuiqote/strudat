import time
import random
start_time = time.time()
angka = []
for _ in range(5000):
    angka.append(random.randint(0,12345))
print(angka)
print( "\n\nJumlah angka pada list ini adalah : ", (len(angka)))


def selectionSort(angka, jumlah):
	for ind in range(jumlah):
		min_index = ind
		for j in range(ind + 1, jumlah):
			if angka[j] < angka[min_index]:
				min_index = j
		(angka[ind], angka[min_index]) = (angka[min_index], angka[ind])

jumlah = len(angka)
selectionSort(angka, jumlah)
print("\nSorting data menggunakan algoritma selection sort : ")
print(angka)
print("\nProses Selesai Dalam %s Detik" % (time.time() - start_time))