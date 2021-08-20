#Autor = Samuel Quiñones Galeana.
#Fecha = 18/08/2021.
#Objetivo = Calcular el cuadrado de la hipotenusa dado dos catetos.


while True: #Este while cicla hasta que el usuario inserta dos números menos de 1000.
    A=int(input("Inserte un entero positivo menor de 1000: ")) #Pido el cateto A.
    B=int(input("Inserte otro entero positivo menor de 1000: ")) #Pido el cateto B.
    if A < 1000 and B < 1000 : #Se comprueba si los dos números son menores de 1000.
        break #Si los dos son menores de 1000, entonces el break me permite romper el while.
    print("Alguno de los dos o los dos números insertados son iguales o mayores a 1000") #Imprimo una advertencia.

C= A**2+B**2 #Obtengo el cuadrado de la hipotenusa.
print("El cuadrado de la hipotenusa dado los catetos {} y {} es: {}".format(A,B,C)) #Imprimo el resultado.