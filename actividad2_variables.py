# Actividad 3 - Python
"""Nombre: Sofía Peñaherrera
Fecha: 2025-04-15
ACTIVIDAD 3 - PYTHON"""
# %%
#Declarar una variable llamada nombre y asignarle un valor.  
nombre="Sofía"
# %%
#Declarar una variable llamada apellido y asignarle un valor.  
apellido="Peñaherrera"
# %%
#Declarar una variable llamada nombreCompleto y asignarle un valor.  
nombrecompleto="Sofía Peñaherrera"
# %%
#Declarar una variable llamada pais y asignarle un valor.  
pais="Ecuador"
# %%
#Declarar una variable llamada ciudad y asignarle un valor.
ciudad="Quito"
# %%
#Declarar una variable llamada edad y asignarle un valor.
edad=16
# %%
#Declarar una variable llamada anio y asignarle un valor.
anio="2026"
# %%
#Declarar una variable llamada estaCasado y asignarle un valor.
estaCasado="No"
# %%
#Declarar una variable llamada esVerdadero y asignarle un valor.
esVerdadero="Sí"
# %%
#Declarar una variable llamada luzEncendida y asignarle un valor.
luzEncendida="Sí"
# %%
#Declarar varias variables y asignarles valores.
comidaFavorita, ruta, dia="Pizza", "Ruta 1", "Miércoles"
# %%
# NIVEL 2
# Imprimir el tipo de dato de cada variable utilizando la función type().
print(type (nombre))
print(type (apellido))
print(type (nombrecompleto))
print(type (pais))
print(type (ciudad))
print(type (edad))
print(type (anio))
print(type (estaCasado))
print(type (esVerdadero))
print(type (luzEncendida))
print(type (comidaFavorita))
print(type (ruta))
print(type (dia))
# Usando la función integrada len(), encuentra la longitud de tu variable nombre.  
print(len(nombre))
# Compara la longitud de tu nombre con la longitud de tu apellido.
print(len(nombre) > len(apellido))
print(len(nombre) < len(apellido))
print(len(nombre) == len(apellido))
# %%
# Declarar 5 como numeroUno y 4 como numeroDos.  
numeroUno = 5
numeroDos = 4
# %%
# Sumar numeroUno y numeroDos y asignar el resultado a una variable llamada total.  
total= numeroUno + numeroDos
print(total)
# %%
# Restar numeroDos de numeroUno y asignar el resultado a una variable llamada diferencia.
resta= numeroDos - numeroUno
print(resta)
# %%
# Multiplicar numeroUno por numeroDos y asignar el resultado a una variable llamada producto.  
multiplicacion= numeroDos * numeroUno
print(multiplicacion)
# %%
# Dividir numeroUno entre numeroDos y asignar el resultado a una variable llamada division.
division= numeroUno / numeroDos
print(division)
# %%
# Encontrar el módulo de numeroDos dividido por numeroUno y asignar el resultado a una variable llamada modulo.
modulo= numeroDos % numeroUno
print(modulo)
# %%
# Encontrar la potencia de numeroUno elevado a numeroDos y asignar el resultado a una variable llamada potencia.
potencia= numeroUno ** numeroDos
print(potencia)
# %%
# Encontrar la división entera de numeroUno entre numeroDos y asignar el resultado a una variable llamada divisionEntera.
divisionEntera= numeroUno // numeroDos
print(divisionEntera)
# %%
# El radio de un círculo es de 30 metros.  
radioEnMetros = 30
# %%
#Calcular el área de un círculo y asignar el valor a una variable llamada areaCirculo.  
areaDelCirculo = 3.14 * radioEnMetros ** 2
print(areaDelCirculo)
# %%
#Calcular la circunferencia de un círculo y asignar el valor a una variable llamada circunferenciaCirculo.  
circunferenciaDelCirculo = 2 * 3.14 * radioEnMetros
print(circunferenciaDelCirculo)
# %%
#Toma el valor del radio como entrada del usuario y calcula el área.  
radio=float(input("Ingrese el radio del círculo en metros: "))
areaDelCirculo = 3.14 * radio ** 2
print("El área del círculo es:", areaDelCirculo)
# %%
#Utiliza la función input() para obtener el nombre, apellido, país y edad de un usuario y almacena cada valor en su variable correspondiente.  
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
pais = str(input("Ingrese su país: "))
edad = int(input("Ingrese su edad: "))
# %%
#Ejecuta help('keywords') en la consola de Python o en tu archivo para comprobar las palabras reservadas de Python. 
help('keywords')