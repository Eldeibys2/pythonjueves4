
#Variable control
numero=0


#acomulador
suma = 0



while (numero>=0):
    numero = int(input("Digita un numero entero: "))
    if(numero>=0):
        suma =suma+numero
    else:
        print(f'la suma fue: {suma}') 
        break   
print(f'la suma fue: {suma}')     
