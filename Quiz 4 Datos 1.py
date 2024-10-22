import time
import random 
import timeit

def listaAleatorios(n):
      lista = [0] * n
      for i in range(n):
          lista[i] = random.randrange(0,10000)
      return lista

aleatorios1000=listaAleatorios(1000)
aleatorios2000=listaAleatorios(2000)
aleatorios3000=listaAleatorios(3000)
aleatorios4000=listaAleatorios(4000)
aleatorios5000=listaAleatorios(5000)

start_time = time.time()

def bubble_sort(arr):

    for n in range(len(arr) - 1, 0, -1):

        for i in range(n):
            if arr[i] > arr[i + 1]:

                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


arr = aleatorios5000
print("La lista desordenada es:")
print(arr)

bubble_sort(arr)

print("La lista ordenada es:")
print(arr)

end_time=time.time()

execute_time = end_time - start_time

print(f"El código tardó {execute_time} segundos en ejecutarse ")
"""




def partition(array, low, high):

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1



def quickSort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)


data = aleatorios1000
print("La lista desordenada")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('La lista ordenada es:')
print(data)



"""