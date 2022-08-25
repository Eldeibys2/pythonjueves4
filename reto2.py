#variable de control
from ast import While


contador = 0

#contador de negativos
contadorNegativos=0

while(contador<5):
        numero = int(input("Digita un número"))
        if(numero<0):
            contadorNegativos=contadorNegativos+1
        else:
            contadorNegativos=contadorNegativos
        contador=contador+1

print(f'El numero de negativos ingresados fue de {contadorNegativos}')