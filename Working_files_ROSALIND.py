#Autor = Samuel Quiñones Galeana.
#Fecha = 19/08/2021.
#Objetivo = Guardar en un archivo las líneas pares de un texto.

import os #Importamos os

Nombre_Archivo= input("Inserte el nombre del archivo: ") #Pedimos al usuario que inserte el nombre del archivo.

Texto = open(Nombre_Archivo, 'r') #Abrimos el archivo sobre el cual se trabajará.
Texto2= open("Nuevo_Archivo.txt","w") #Creamos el archivo donde guardaremos las líneas pares.

cont_lines=0 #Contador de líneas.
for line in Texto: #Este for me permite recorrer todas las líneas del archivo.
    cont_lines = cont_lines + 1 #Va contando las líneas del archivo.

if cont_lines <= 1000: #El archivo debe tener como máximo 1000 líneas.
    cont=1 #Índice de la líena
    Texto = open(Nombre_Archivo, 'r') #Abrimos el archivo para poder trabajar de nuevo con él.
    for line2 in Texto: #Este for recorre todas las líneas del archivo.
        if cont % 2 == 0: #Verifica si la línea es par.
            Texto2.write(line2.strip() + "\n") #Escribimos en el nuevo_archivo las líneas pares.
        cont = cont + 1 #Aumentamos el índice.
    print("El archivo se guardó en la dirección: {} con el nombre de: {}".format(os.getcwd(),"Nuevo_Archivo.txt")) #Imprimimos la dirección y el nombre del archivo en donde se guardaron las líneas pares.
else:
    print("El archivo tiene más de 1000 líneas, vuelva a intentarlo") #Imprimimos la advertencia.