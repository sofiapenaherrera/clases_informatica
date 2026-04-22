"""Evaluación 1
Nombre: Sofía Peñaherrera  :)
Fecha: 2025-04-22"""



# ===== PARTE A =====
# Respuesta 1:
"""Observa el siguiente código:
nombre = "Lucía"
edad = 16
promedio = 9.75
cursos = ["Python", "HTML", "CSS"]
print(type(nombre))
print(type(edad))
print(type(promedio))
print(type(cursos))
print(len(nombre))
Responde:
a) Indica el tipo de dato de cada variable.
b) Escribe qué mostraría el programa en pantalla.
c) Explica qué hace len(nombre)."""

#a) El tipo de dato de la variable nombre es str (cadena de texto), de la variable edad es int (entero), de la variable promedio es float (número decimal) y de la variable cursos es una lista (list) conformada por cadenas de texto.
#b) El programa mostraría en pantalla:  
#<class 'str'>
#<class 'int'>
#<class 'float'>
#<class 'list'>
#5
#c) La función len(nombre) devuelve la longitud de la cadena de texto almacenada en la variable nombre, es decir, el número de caracteres que tiene la palabra "Lucía". En este caso, len(nombre) devolvería 5 porque "Lucía" tiene 5 caracteres (L, u, c, í, a).  

# Respuesta 2:
"""Responde con tus palabras:
a) ¿Qué diferencia hay entre print() e input()?
b) ¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo?
c) Explica la diferencia entre /, // y %.
d) Escribe una instrucción que permita comprobar la versión de Python que se está usando.
e) Escribe una instrucción que permita consultar las palabras reservadas de Python.
"""
#a) La función "print()" se utiliza para mostrar información en la pantalla, mientras que la función "input()" se utiliza para solicitar al usuario que ingrese datos desde el teclado. "print()" no requiere interacción del usuario, únicamente imprime el contenido indicado; mientras que "input()" espera a que el usuario proporcione una entrada antes de continuar con la ejecución del programa.
#b) Un dato ingresado con "input()" se considera una cadena de texto str por defecto, incluso si el usuario ingresa un número. Si se intenta usar este dato directamente en un cálculo sin convertirlo a un tipo numérico como int o float, se producirá un error de tipo de dato porque no se pueden realizar operaciones matemáticas con cadenas de texto.
#c) El operador / realiza una división normal y devuelve un resultado de tipo float. Por otro lado,el operador // realiza una división entera y devuelve el cociente sin la parte decimal, es decir, redondea hacia abajo al número entero más cercano. El operador % devuelve el resto de la división entre dos números, es decir, lo que sobra después de dividir el primer número para el segundo.
#d) Para comprobar la versión de Python que se está usando, se utiliza "python --version" en la terminal de Git Bash.
#e) help('keywords')




# ===== PARTE B =====
"""El siguiente programa tiene errores. Reescríbelo de forma correcta para que funcione.
ancho = input("Ingrese el ancho del terreno: ")
largo = input("Ingrese el largo del terreno: ")
precio = input("Ingrese el precio por metro cuadrado: ")
area = ancho * largo
costo = area * precio
print("Área total: " + area)
print("Costo estimado: " + costo)
Luego responde:
a) ¿Cuáles eran los errores principales?
b) ¿Por qué tu corrección sí permite obtener resultados válidos?
"""
# %% 
#Corrección del programa
ancho = float(input("Ingrese el ancho del terreno: "))
largo = float(input("Ingrese el largo del terreno: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))
area = ancho * largo
costo = area * precio
print("El área total es: " + str(area))
print("El costo estimado es: " + str(costo))
#a) Los errores principales eran que las variables ancho, largo y precio se estaban almacenando como cadenas de texto (str) debido a la función input(), lo que causaba un error al intentar realizar operaciones matemáticas con ellas. Además, al imprimir el área y el costo, se intentaba unir un número (float) con una cadena de texto sin convertir el número a cadena, lo que también generaba un error.
#b) Mi corrección permite obtener resultados válidos porque se convierte la entrada del usuario a tipo float, lo que permite realizar las operaciones matemáticas correctamente. Además, al imprimir el área y el costo, se convierte el resultado a cadena de texto utilizando str(), lo que permite manipular la información sin errores.
# %%
"""Escribe un fragmento de código que haga lo siguiente:
1. Cree la variable frase con el texto "Tecnología para todos".
2. Muestre la frase en mayúsculas.
3. Muestre la cantidad de caracteres de la frase.
4. Verifique si la palabra "Python" está dentro de la frase.
5. Reemplace "Tecnología" por "Programación".
6. Divida la frase en palabras usando split()."""
frase = "Tecnología para todos"
print(frase.upper())
print(len(frase))
print("Python" in frase)
print(frase.replace("Tecnología", "Programación"))
print(frase.split())



# ===== PARTE C =====
# Programa integrador
"""Una tienda desea generar un resumen de presupuesto para cubrir una pared rectangular con
papel decorativo.
Desarrolla un programa que:
1. Solicite al usuario: Nombre, apellido, país, ancho de la pared, alto de la pared, precio por
metro cuadrado
o Calcule: área de la pared, costo total estimado
2. Cree la variable nombre_completo.
1. Muestre un reporte final que incluya:
o nombre completo, país, área calculada, costo total (La impresión del reporte
final debe realizarse usando f-strings.)
3. Muestre además:
o nombre_completo en mayúsculas
o la longitud de nombre_completo
o si la letra "a" está presente en nombre_completo
o si el costo total es mayor que 100 dólares"""
# %% 
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país: ")
ancho = float(input("Ingrese el ancho de la pared: "))
alto = float(input("Ingrese el alto de la pared: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))

nombre_completo = nombre+" "+apellido
area = ancho * alto
costo_total = area * precio

print(f"El nombre completo es: {nombre_completo}")
print(f"País: {pais}")
print(f"El área calculada es: {area}")
print(f"El costo total es: {costo_total}")

print(f"El nombre completo en mayúsculas es: {nombre_completo.upper()}")
print(f"La longitud del nombre completo es: {len(nombre_completo)}")
print(f"¿Está presente la letra 'a' en el nombre completo? { 'a' in nombre_completo }")
print(f"¿El costo total es mayor que 100 dólares? {costo_total > 100}")