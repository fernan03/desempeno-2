from Cuenta import Cuenta
from Cliente import Cliente

cliente1 = Cliente()
cliente1.nombre = 'Luis'
cliente1.apellido = 'Sucerquia'
cliente1.cedula = '1001457299'
cliente1.ciudad = 'Medellín'

cuenta1 = Cuenta()
cuenta1.numeroCuenta = '123456'
cuenta1.saldo = '5000'

opcion  = 100


print("Menu")
print("1.Consultar Saldo")
print("2. Ingresar ")
print("3.Retirar")
print("0. Salir")

while opcion!=0:
    
    opcion = int(input("Digita una opcion: "))
    if opcion ==1:
         print(f"El saldo es:  $" + (cuenta1.saldo) )
         
    elif opcion ==2:
         dinero = int(input("Digita el monto: "))
         suma = dinero + int(cuenta1.saldo)
         cuenta1.saldo = suma
         print(suma)
    
    elif opcion ==3:
         dinero2 = int(input("Digita el monto a restar: "))
         resta =int(cuenta1.saldo) - dinero2 
         cuenta1.saldo =  resta
         print(resta)

    
    elif opcion ==0:
         print()

        
    elif opcion ==0:
        break
    else:
        print("no valido")

else:
    print("Terminé")