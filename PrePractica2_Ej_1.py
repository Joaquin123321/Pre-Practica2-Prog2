#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO

from operator import index


lista = []

for x in range(5):
   valor = int(input(f"Ingrese el valor del índice {x}: "))
   lista.append(valor)

maximo = max(lista)
print(f"El valor máximo es: {maximo}")

  
mayor = lista[0]
 
for y in range(5):    
    if lista[y] > mayor:
        mayor = lista[y]

print(f"El mayor es: {mayor}")

#FIN