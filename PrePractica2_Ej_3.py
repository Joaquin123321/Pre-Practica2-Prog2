#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
num1 = int(input("Ingresar el primer número: "))
num2 = int(input("Ingresar el segundo número: "))
print("El resultado de la división del primer número por el segundo es:", num1 / num2)
print("El resultado de la división del segundo número por el primero es:", num2 / num1)

try:
    div1 = num1 / num2
    div2 = num2 / num1
except ZeroDivisionError as exception:
    print(f"Ocurrió un error. No se puede dividir por 0 | {exception}")


#FIN
