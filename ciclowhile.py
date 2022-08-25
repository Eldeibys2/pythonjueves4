'''
numero = 5
while(numero<10):
    print("Estoy adentro de la cuerda")
    numero+=1
else:
    print("adiossssssss")   

print("Estoy por fuera de la cuerda")
'''

opcion = 1
print("******Menu******")
print("1.Sumar")
print("2.Restar")
print("0.salir")
while(opcion !=0):
    opcion = int(input("Digite una opcion: "))
    if(opcion==1):
        print("Sumando")
    elif(opcion==2):
        print("Restando")
    elif(opcion==0):
        break    
    else:
        print("Digite una opcion valida")        
