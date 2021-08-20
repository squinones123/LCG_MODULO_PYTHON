#Autor = Samuel Quiñones Galeana.
#Fecha = 19/08/2021.
#Objetivo = Calcular la suma de todos los números impares desde A hasta B. 

while True: #Este while cicla hasta que el usuario inserte valores de A y B válidos.
    A=int(input("Inserte un número positivo: ")) #Pido el valor de A.
    B=int(input("Inserte otro número positivo mayor que el anterior y menor de 10000: ")) #Pido el valor de B.
    if A < B < 10000: #Comprueba las condiciones solicitadas por el problema.
        break #Si se cumple rompo el ciclo.
    print("Alguna de las condiciones solicitadas no se cumplió, vuelva a intentarlo") #Si las condiciones no se cumplen se imprime esta advertencia.

suma=0 #Inicializo una variable que acumulará la suma.
for i in range(A,B+1,1): #i toma cada uno de los valores desde A hasta B.
    if i % 2 != 0: #Compruebo si es un número impar.
        suma=suma+i #Si es impar, se sumará con la suma acumulada.

print("La suma de los impares desde {} hasta {} es: {}".format(A,B,suma)) #Imprimo el resultado
