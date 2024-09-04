# Estructura condicional simple

sueldo = int(input("Ingrese cual es su sueldo: "))
if sueldo > 3000:
    print("Esta persona debe abonar impuestos")


# Estructura condicional compuesta varios caminos

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
print("El valor mayor es")
if num1 > num2:
    print(num1)
else:
    print(num2)

print()

"""
Operadores Relacionales
    == Igualdad
    != Desigualdad
    < Menor
    > Mayor
    <= Menor Igual
    >= Mayor Igual


Operadores Matematicos
    + Suma
    - Resta
    * Multiplicacion
    / Division Flotante
    // Divion Enteros
    % Resto de una division
    ** Exponenciacion
"""

# PROBLEMAS PROPUESTOS

# Realizar un programa que solicite la carga por teclado de dos numeros, si el primero es mayor al segundo
# informar su suma y diferencia, en caso contrario informar el producto y la division del primero respecto al segundo

valor1 = int(input("Ingrese el valor: "))
valor2 = int(input("Ingrese el valor: "))

if valor1 > valor2:
    print("suma: ", valor1 + valor2)
    print("resta: ", valor1 - valor2)
else:
    print("producto: ", valor1 * valor2)
    print("division:", valor1 // valor2)

print()

# Se ingresan 3 notas de un alumno, si el promedio es mayor o igual a 7 mostrar un mensaje "promocionado"

nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segundo nota: "))
nota3 = int(input("Ingrese la tercer nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print("promedio: ", promedio)
if promedio >= 7:
    print
    print("Promocionado")

print()

# Se ingresa por teclado un numero positivo de uno o dos digitos(1..99) mostrar un mensaje indicando si el numero
# tiene uno o dos digitos
# (Tener en cuenta que solo debe cumplirse que tenga uno o dos digitos)

unoDos = int(input("Ingrese el valor para calcular los digitos: "))
if unoDos < 10:
    print("Tiene un digito")
else:
    print("Tiene dos digitos")