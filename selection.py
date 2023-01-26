import time
import random
start_time = time.time()
angka = []
for _ in range(5000):
    angka.append(random.randint(0,12345))
print(angka)
print( "\n\nJumlah angka pada list ini adalah : ", (len(angka)))

def insertionSort(angka):
    for a in range(1, len(angka)):
        b = angka[a]
        j = a - 1
        while j >= 0 and b < angka[j]:
            angka[j + 1] = angka[j]
            j = j - 1
        angka[j + 1] = b

        
print("\nSorting data menggunakan algoritma bubble sort : ")
insertionSort(angka)
print(angka)
print("\nProses Selesai Dalam %s Detik" % (time.time() - start_time))