#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO

lista = []
lista2 = []

for x in range(3):
    valor = int(input(f"Ingresar el valor del índice {x}: "))
    lista.append(valor)

    impar = valor % 2

    if impar != 0:
        lista2.append(valor)

print(f"La lista de números originales es {lista}")
print(f"La lista de números impares es {lista2}")
        


#FIN