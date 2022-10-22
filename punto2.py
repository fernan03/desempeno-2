from ast import Lambda


numero1 = int(input("Agrege el primer numero: "))
numero2 = int(input("Agrege el segundo numero numero: "))

mayor = lambda numero1, numero2 : 1 if numero1 > numero2 else -1

Mostrar = lambda numero : "el primer numero es mayor" if numero == 1 else "el segundo numero es mayor"

print(Mostrar(mayor(numero1,numero2)))