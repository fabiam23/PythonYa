# Los Errores Sintacticos, son aquellos errores tipograficos, como por ejemplo, el nombre incorrecto de la funcion, falta de parentesis,
# palabras claves mal escritas, etc

# Los Errores logicos, son mas dificiles de localizar, puesto que son aquellos, que estan mal estructurados.

# Problema
# Hallar la superficie de un cuadrado conociendo el valor de un lado

# lado es la variable. Una variable es una caja en donde se puede almacenar un dato.

lado = int(input("Ingrese la medida del lado del cuadrado: "))
superficie = lado * lado
print("La superficie del cuadrado es")
print(superficie)
print()

# Programa con un error logico
lado = int(input("Ingrese la medida del lado del cuadrado: "))
superficie = lado * lado * lado
print("La superficie del cuadrado es")
print(superficie)
print()
# Error logico la superficie se calcula, lado * lado, no lado * lado * lado

# Programa con un error sintactico2
lado = int(input("Ingrese la medida del lado del cuadrado: "))
superficie = lado * lado
print("La superficie del cuadrado es")
print(Superficie)
# superficie mal escrita, la variable debe colocarse tal cual es declarada
