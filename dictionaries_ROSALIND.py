#Autor = Samuel Quiñones Galeana.
#Fecha = 19/08/2021.
#Objetivo = Contar el número de veces que aparece una palabra en una cadena de texto.

Nombre_Arch=input("Inserte el nombre del archivo: ") #Pedimos que se inserte el nombre del archivo.
string = open(Nombre_Arch, 'r') #Abrimos el archivo.
string = string.read() #Nos permite manejar el contenido de nuestro archivo como un string.
diccionario={} #Declaramos nuestro diccionario vacío.

count_letters=0 #Contador de letras.
for word in string.split(' '): #Recorremos el string separado por espacios.
    count_letters=count_letters+len(word) #Calculamos la cantidad de letras totales.


if count_letters <= 10000: #Verificamos que el string no tenga más de 10000 letras.
    for word in string.split(' '): #Recorremos el string separado por espacios.
        count=0 #Inicializamos contador.
        for i in string.split(' '): #Volvemos a recorrer el string separado por espacios.
            if word == i: #Comparamos si existen palabras iguales.
                count=count+1 # Si son iguales sumamos uno al contador.
        diccionario[word]=count # A la llave se le asigna las veces que está repetida esa palabra.

    print(diccionario) #Imprimimos el diccionario.
else:
    print("Tu texto tiene más de 10000 letras, vuelva a intentarlo") #Imprimimos advertencia.
