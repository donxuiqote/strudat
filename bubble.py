import time
import random
start_time = time.time()
angka = []
for _ in range(5000):
    angka.append(random.randint(0,12345))
print(angka)
print( "\n\nJumlah angka pada list ini adalah : ", (len(angka)))

def bubbleSort(angka):
    swapped = False
    for n in range(len(angka)-1, 0, -1):
        for i in range(n):
            if angka[i] > angka[i + 1]:
                swapped = True
                angka[i], angka[i + 1] = angka[i + 1], angka[i]       
        if not swapped:
            return

print("\nSorting data menggunakan algoritma bubble sort : ")
bubbleSort(angka)
print(angka)
print("\nProses Selesai Dalam %s Detik" % (time.time() - start_time))