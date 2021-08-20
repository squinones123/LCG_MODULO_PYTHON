#Autor = Samuel Quiñones Galeana.
#Fecha = 18/08/2021.
#Objetivo = Obtener los cortes del índice A al B y del C al D de una cadena de texto.

string=input("Inserte la cadena de texto: ") #Pedimos que se inserte el texto.
slice_a = int(input("Inserta el extremo izquierdo del corte 1: ")) #Se pide el índice A.
slice_b = int(input("Inserta el extremo derecho del corte 1: "))   #Se pide el índice B.
slice_c = int(input("Inserta el extremo izquierdo del corte 2: ")) #Se pide el índice C.
slice_d = int(input("Inserta el extremo derecho del corte 2: "))   #Se pide el índice D.

print(string[slice_a:slice_b+1]+" "+string[slice_c:slice_d+1]) #Se imprimen los cortes del índice A al B y del C al D de la cadena de texto.