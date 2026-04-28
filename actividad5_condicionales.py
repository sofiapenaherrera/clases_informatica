a=3 
if a>0: 
    print(f"{a} es positivo")
else:
    print(f"{a} es negativo")
print("Gracias por utilizar el programa")
# Actividad 1: Crear un programa que solicite una calificacion (1-100) y devolver si equivalente cualitativo.
# 90-100: A, 80-89: B, 70-79: C, 70<: D
#Utilice if anidados para resolver el problema.
calificacion = float(input("Ingrese su calificación (1-100): "))
if calificacion >= 90:
    print("Su calificación es A")
else:
    if calificacion >= 80:
        print("Su calificación es B")
    else:
        if calificacion >= 70:
            print("Su calificación es C")
        else:
            print("Su calificación es D")
# %%
# Actividad 2: Crear un programa que solicite un numero y devuelva si es cero, par positivo o negativo o impar positivo o negativo.
numero = int(input("Ingrese un número: "))
if numero == 0:
    print("El número es cero")
else:    
    if numero > 0:
        if numero % 2 == 0:
            print("El número es par positivo")
        else:
            print("El número es impar positivo")
    else:
        if numero % 2 == 0:
            print("El número es par negativo")
        else:
            print("El número es impar negativo")

# Ahora con elif
# %%
numero = int(input("Ingrese un número: "))
if numero == 0:
    print("El número es cero")
elif numero > 0 and numero % 2 == 0:
    print("El número es par positivo")
elif numero > 0 and numero % 2 != 0:
    print("El número es impar positivo")
elif numero < 0 and numero % 2 == 0:
    print("El número es par negativo")
else:
    print("El número es impar negativo")
# %%
# Ahora con shorthand
numero = int(input("Ingrese un número: "))
print("El número es cero" if numero == 0 else "El número es par positivo" if numero > 0 and numero % 2 == 0 else "El número es impar positivo" if numero > 0 and numero % 2 != 0 else "El número es par negativo" if numero < 0 and numero % 2 == 0 else "El número es impar negativo")
#%%
# DEBER - 
# Ejercicios: Nivel 1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Tienes la edad suficiente para aprender a conducir.")
else:
    faltan = 18 - edad
    print(f"Necesitas {faltan} años más para aprender a conducir.")
# %%
my_age = int(input("Ingrese mi edad: "))
your_age = int(input("Ingrese su edad: "))

if your_age > my_age:
    diferencia = your_age - my_age
    if diferencia == 1:
        print("Eres 1 año mayor que yo.")
    else:
        print(f"Eres {diferencia} años mayor que yo.")
else:
    if my_age > your_age:
        diferencia = my_age - your_age
        if diferencia == 1:
            print("Soy 1 año mayor que tú.")
        else:
            print(f"Soy {diferencia} años mayor que tú.")
    else:
        print("Tenemos la misma edad.")
# %%
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")
# %%
# Ejercicios: Nivel 2
puntaje = int(input("Ingrese su puntaje: "))

if 90 <= puntaje <= 100:
    print("A")
elif 80 <= puntaje <= 89:
    print("B")
elif 70 <= puntaje <= 79:
    print("C")
elif 60 <= puntaje <= 69:
    print("D")
elif 0 <= puntaje <= 59:
    print("F")
else:
    print("Puntaje inválido")
# %%
mes = input("Ingrese el mes: ").lower()

if mes in ["septiembre", "octubre", "noviembre"]:
    print("Otoño")
elif mes in ["diciembre", "enero", "febrero"]:
    print("Invierno")
elif mes in ["marzo", "abril", "mayo"]:
    print("Primavera")
elif mes in ["junio", "julio", "agosto"]:
    print("Verano")
else:
    print("Mes inválido")
# %%
fruits = ['banana', 'orange', 'mango', 'lemon']

fruta = input("Ingrese una fruta: ").lower()

if fruta in fruits:
    print("Esa fruta ya existe en la lista")
else:
    fruits.append(fruta)
    print("Lista actualizada:", fruits)
# Ejercicios: Nivel 3
edad = int(input("Ingrese la edad del estudiante: "))
promedio = float(input("Ingrese el promedio académico: "))
permiso = input("¿Tiene permiso de sus padres? (si/no): ").lower()

if edad < 12:
    if permiso == "si":
        print("Puede ingresar con supervisión")
    else:
        print("No puede ingresar a la plataforma")

elif 12 <= edad <= 17:
    if promedio >= 8.5:
        print("Acceso completo a cursos avanzados")
    elif promedio >= 7:
        print("Acceso a cursos intermedios")
    else:
        print("Acceso solo a cursos básicos")

else:
    print("Acceso libre a la plataforma")