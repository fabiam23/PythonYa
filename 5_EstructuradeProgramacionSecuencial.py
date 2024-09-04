"""# Realizar la carga de dos numeros enteros por teclado e imprimir su suma y su producto
numero1 = int(input('Ingrese el primer valor: '))
numero2 = int(input('Ingrese el segundo valor: '))
suma = numero1 + numero2
producto = numero1 *  numero2
print("La suma es:", suma)
print("El producto es:", producto)
print()

# Realizar la carga del precio de un producto y la cantidad a llevar.
# Mostrar cuando se debe pagar (se ingresa un valor entero en el precio)
precio  = int(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad a llevar: "))
costo = precio * cantidad
print("Usted debe pagar la suma de:", costo)
"""

# PROBLEMAS PROPUESTOS

# Realizar la carga del lado de un cuadrado, mostrar por pantalla, el perimetro del mismo
# El perimetro de un cuadrado se calcula multiplicando el valor del lado por cuatro

lado = int(input("Ingrese el tamano del lado, para calcular el perimetro del mismo: "))
perimetro = lado * 4
print("El Perimetro del cuadrado es:", perimetro) 
print()

# Escribir un programa con el cual se ingresen cuatro numeros, calcular e informar las suma de los primeros dos
# y el producto del tercero y cuarto

numero1 = int(input("Ingrese el valor: "))
numero2 = int(input("Ingrese el valor: "))
numero3 = int(input("Ingrese el valor: "))
numero4 = int(input("Ingrese el valor: "))
suma1 = numero1 + numero2
producto1 = numero3 * numero4
print("la suma del primero con respecto al segundo es:",suma1)
print("el producto del tercero con respecto al segundo es:", producto1)
print()

# Realizar un programa que lea cuatro valores numeros e informar su suma y promedio
# se toman las variables del ejercicio anterior
suma2 = numero1 + numero2 + numero3 + numero4
promedio1 = suma2 / 4
print("La suma de los numeros es:", suma2)
print("El promedio de los numeros es:", promedio1)
print()

# Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora
horas = int(input("Ingrese el total de horas trabajadas: "))
valorHoras = int(input("Ingrese el valor por hora: "))
sueldo = horas * valorHoras
print("El sueldo mensual de un operario es:", sueldo)