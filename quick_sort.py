#importar cronometro
import time
import random

def quick_sort(arr): #funcion quick sort, recibe un arreglo
    if len(arr) <= 1: #comprobar si el arreglo tiene 1 o menos elementos
        return arr # si es asi regresa el arreglo como tal
    pivote = arr[len(arr) // 2] #se selecciona el pivote, el elemento que esta en la mitad de la lista
    
    #se divide la lista en 3
    #izquierda valores menores del pivote
    izquierda = [valor_menor for valor_menor in arr if valor_menor < pivote]

    #medio valores iguales al pivote
    medio = [valor_igual for valor_igual in arr if valor_igual == pivote]
    print(f"pivote {pivote}")
    
    #derecha valores mayores al pivote
    derecha = [valor_mayor for valor_mayor in arr if valor_mayor > pivote]
    
    #se aplica recursion sobre la funcion quick_sort para devolver todos los numeros
    return quick_sort(izquierda) + medio + quick_sort(derecha)

# Ejemplo de uso:

n = int(input("ingrese el numero de datos"))
#arreglo de ejemplo
arr = [random.randint(1, 1000) for x in range(n)]

#lista original
print("Lista original:", arr)

start_time = time.time() # Registro del tiempo de inicio
sorted_arr = quick_sort(arr) #se realiza la ejecucion
end_time = time.time() # Registro del tiempo de finalización

print("Lista ordenada:", sorted_arr)

#tiempo
print("Tiempo de ejecución:", end_time - start_time, "segundos")
