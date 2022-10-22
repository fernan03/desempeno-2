from funciones.menu import menu
from funciones.anotarCiclista import  anotarCiclista
from funciones.compararTiempo import compararTiempo


opcion=0
ciclistas1=[]

menu()
while opcion !=-1:
    opcion=int(input("digite la opcion: "))

    if(opcion==1):
        ciclistas.append(anotarCiclista())
    elif(opcion==2):
        compararTiempo(ciclistas)
    elif(opcion==0):
        break
    else:
        print("digite una opcion valida: ")
            
