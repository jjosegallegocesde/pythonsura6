#CICLO MIENTRAS

#DECLARAR UNA VARIABLE CENTINELA
#O VARIABLE DE CONTROL PARA EVALUAR
#LA EJECUCCIÓN DE MI CICLO

'''

'''

from difflib import Match
import math


i=0
num1 = 0
num2 = 0
suma = 0
resta= 0
multiplicacion =0
raiz = 0

#MENU DE OPCIONES
print("***MENU***")
print("1. SUMAR 2 NUMEROS")
print("2. RESTAR 2 NUMEROS")
print("3. ENCONTRAR LA RAIZ CUADRADA DE UN NUMERO")
print("4. MULTIPLICAR 2 NUMEROS")
print("5. salir")
#programar la estructura del ciclo mientras
while(i!=5):
    i=int(input("Digite una opción del menú: "))
    
    if(i==1):
        num1 = int(input("Ingrese el primer número"))
        num2 = int(input("Ingrese el segundo número"))
        suma = num1 + num2
        print("El resultado es: ", suma)
    elif(i==2):
        num1 = int(input("Ingrese el primer número"))
        num2 = int(input("Ingrese el segundo número"))
        resta = num1 - num2
        print("El resultado es: ", resta)
        
    elif(i==3):
        num1 = int(input("Ingrese el primer número"))
        num2 = int(input("Ingrese el segundo número"))
        multiplicacion = num1 * num2
        print("El resultado es: ", multiplicacion)
        
    elif(i==4):
        num1 = int(input("Ingrese el número"))
        raiz = math.sqrt(num1)
        print("El resultado es: ", raiz)    
    elif(i==5):
        break
    else:
        print("Digita una opcion valida")
    
print("salimos del while")