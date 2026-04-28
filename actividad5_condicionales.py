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