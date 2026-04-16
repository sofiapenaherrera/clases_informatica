"""Actividad 3.- Operadores en Python
Nombre: Sofía Peñaherrera
Fecha: 2025-04-16"""
# Operadores en Python
# %%
# Declara tu edad como una variable de tipo entero.  
edad=16
# %%
# Declara tu altura como una variable de tipo flotante.
estatura=1.55
# %%
# Escribe un programa que solicite al usuario la base y la altura de un triángulo y calcule su área
base=float(input("Ingrese la base del triángulo: "))
altura=float(input("Ingrese la altura del triángulo: "))
area=(base*altura)/2
print("El área del triángulo es:", area)
# %%
# Escribe un programa que solicite al usuario los lados a, b y c de un triángulo y calcule su perímetro.
lado_a=float(input("Ingrese el lado a del triángulo: "))
lado_b=float(input("Ingrese el lado b del triángulo: "))
lado_c=float(input("Ingrese el lado c del triángulo: "))
perimetro=lado_a+lado_b+lado_c
print("El perímetro del triángulo es:", perimetro)
# %%
#Obtén la longitud y el ancho de un rectángulo usando un prompt. Calcula su área y su perímetro.
longitud=float(input("Ingrese la longitud del rectángulo: "))
ancho=float(input("Ingrese el ancho del rectángulo: "))
area_rectangulo=longitud*ancho
perimetro_rectangulo=2*(longitud+ancho)
print("El área del rectángulo es:", area_rectangulo)
print("El perímetro del rectángulo es:", perimetro_rectangulo)
# %%
# Obtén el radio de un círculo usando un prompt. Calcula el área y la circunferencia.
radio=float(input("Ingrese el radio del círculo: "))
area_circulo=3.14*radio**2
circunferencia_circulo=2*3.14*radio
print("El área del círculo es:", area_circulo)
print("La circunferencia del círculo es:", circunferencia_circulo)
# %%
"""La pendiente se calcula como: 
(m = (y₂ - y₁) / (x₂ - x₁)) 
Encuentra la pendiente y la distancia euclidiana entre los puntos (2, 2) y (6, 10)."""
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia_euclidiana = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("La pendiente entre los puntos es:", pendiente)
print("La distancia euclidiana entre los puntos es:", distancia_euclidiana)
# %%
"""Calcula el valor de y en la función: 
y = x² + 6x + 9 
Prueba con diferentes valores de x y determina para qué valor de x, y es igual a 0.  """
x = -3
y = x**2 + 6*x + 9
print(y)
# %%
#Encuentra la longitud de las palabras “python” y “dragón” y realiza una comparación booleana (verdadero/falso).  
longitud_python = len("python")
longitud_dragon = len("dragón")
comparacion = longitud_python == longitud_dragon
print("¿La longitud de 'python' es igual a la longitud de 'dragón'?", comparacion)
# %%
"""Usa el operador in para verificar si la palabra “jerga” está en la siguiente oración: 
“Espero que este curso no esté lleno de jerga.”  """
oracion = "Espero que este curso no esté lleno de jerga."
palabra = "jerga"
verificacion = palabra in oracion
print("¿La palabra 'jerga' está en la oración?", verificacion)
# %%
# Usa el operador and para verificar si "on" se encuentra tanto en "python" como en "dragon". 
palabra1 = "python"
palabra2 = "dragon"
verificacion_and = "on" in palabra1 and "on" in palabra2
print("¿'on' se encuentra tanto en 'python' como en 'dragon'?", verificacion_and)
# %%
# Encuentra la longitud del texto “python” y convierte ese valor a tipo float y luego a tipo string.  
longitud_python = len("python")
longitud_float = float(longitud_python)
longitud_string = str(longitud_float)
print("Longitud de 'python' como entero:", longitud_python)
print("Longitud de 'python' como float:", longitud_float)
print("Longitud de 'python' como string:", longitud_string)
# %%
# Verifica si la división entera de 7 entre 3 es igual al valor entero de 2.7.  
division_entera = 7 // 3
valor_entero = int(2.7)
comparacion_division = division_entera == valor_entero
print("¿La división entera de 7 entre 3 es igual al valor entero de 2.7?", comparacion_division)
# %%
#Verifica si el tipo de dato de “10” es igual al tipo de dato de 10.  
tipo_cadena = type("10")
tipo_entero = type(10)
comparacion_tipo = tipo_cadena == tipo_entero
print("¿El tipo de dato de '10' es igual al tipo de dato de 10?", comparacion_tipo)
# %%
# Verifica si int('9.8') es igual a 10.  
valor_int = int(float('9.8'))
comparacion_int = valor_int == 10
print("¿int('9.8') es igual a 10?", comparacion_int)
# %%
# Escribe un programa que solicite al usuario ingresar las horas trabajadas y la tarifa por hora. Calcula el pago total.  
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
pago_total = horas_trabajadas * tarifa_por_hora
print("El pago total es:", pago_total)
# %%
# Escribe un programa que solicite al usuario ingresar el número de años que ha vivido. Calcula la cantidad de segundos que ha vivido.
años_vividos = int(input("Ingrese el número de años que ha vivido: "))
segundos_vividos = años_vividos * 365 * 24 * 60 * 60
print("La cantidad de segundos que ha vivido es:", segundos_vividos)
# %%
"""Escribe un programa en Python que muestre la siguiente tabla:  

1 1 1 1 1 
2 1 2 4 8 
3 1 3 9 27 
4 1 4 16 64 
5 1 5 25 125 """
print("1 1 1 1 1") 
print("2 1 2 4 8") 
print("3 1 3 9 27") 
print("4 1 4 16 64") 
print("5 1 5 25 125") 