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