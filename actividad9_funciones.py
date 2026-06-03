def mostrar_estudiante(nombre, curso):
    print("Estudiante registrado:")
    print("Nombre:", nombre)
    print("Curso:", curso)
    print("-------------------")
def mensaje_final():
    print("Fin del programa")
cantidad = int(input("¿Cuántos estudiantes desea ingresar?: "))
contador = 1
while contador <= cantidad:
    print("\nRegistro del estudiante", contador)
    nombre = input("Ingrese el nombre del estudiante: ")
    curso = input("Ingrese el curso del estudiante: ")
    mostrar_estudiante(nombre, curso)
    contador += 1
mensaje_final()
#%%
def calcular_promedio (nombre, apellido, nota1, nota2, nota3):
    print (f"Tu nombre es {nombre}, y tu apellido es {apellido}")
    promedio = (nota1 + nota2 + nota3) / 3
    print (f"Tu promedio es: {promedio}")
nombre = input ("Ingresa tu nombre : ")
apellido = input ("Ingresa tu apellido: ")
nota1 = float(input("Ingrese la primera nota: ")) 
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
calcular_promedio (nombre, apellido, nota1, nota2, nota3)
#%%
def obtener_mensaje():
    mensaje = "Bienvenido al sistema"
    return mensaje
def generar_nombre_completo():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    nombreCompleto = nombre + " " + apellido
    return nombreCompleto
print(obtener_mensaje())
print(generar_nombre_completo())
#%%
def calcular_total_producto(precio, cantidad):
    return precio * cantidad
print("SISTEMA DE COMPRA")
subtotal = 0
for i in range(1, 4):
    print(f"Producto {i}")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    while precio <= 0:
        print("Precio no válido. Debe ser mayor que 0.")
        precio = float(input("Ingrese nuevamente el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad comprada: "))
    while cantidad <= 0:
        print("Cantidad no válida. Debe ser mayor que 0.")
        cantidad = int(input("Ingrese nuevamente la cantidad comprada: "))
    total_producto = calcular_total_producto(precio, cantidad)
    subtotal += total_producto
    print(f"Producto registrado: {nombre}")
    print(f"Total del producto: ${total_producto}")
iva = subtotal * 0.15
total_pagar = subtotal + iva
print("RESUMEN DE COMPRA")
print(f"Subtotal: ${subtotal}")
print(f"IVA (15%): ${iva}")
print(f"Total a pagar: ${total_pagar}")
#%%
def metros_a_centimetros(metros):
    return metros * 100
def metros_a_milimetros(metros):
    return metros * 1000
def metros_a_kilometros(metros):
    return metros / 1000
def metros_a_pulgadas(metros):
    return metros * 39.3701

metros = float(input("Ingrese una cantidad en metros: "))
print("\nMenú de conversión")
print("1. Centímetros")
print("2. Milímetros")
print("3. Kilómetros")
print("4. Pulgadas")
opcion = int(input("Seleccione una opción (del 1 al 4): "))
if opcion == 1:
    resultado = metros_a_centimetros(metros)
    print(f"{metros} metros = {resultado} centímetros")
elif opcion == 2:
    resultado = metros_a_milimetros(metros)
    print(f"{metros} metros = {resultado} milímetros")
elif opcion == 3:
    resultado = metros_a_kilometros(metros)
    print(f"{metros} metros = {resultado} kilómetros")
elif opcion == 4:
    resultado = metros_a_pulgadas(metros)
    print(f"{metros} metros = {resultado} pulgadas")
else:
    print("Opción no válida.")
#%%
def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3
def obtener_mayor(n1, n2, n3):
    return max(n1, n2, n3)
def obtener_menor(n1, n2, n3):
    return min(n1, n2, n3)
def determinar_estado(promedio):
    if promedio >= 7: 
        return "Aprobado"
    else:
        return "Reprobado"
nota1 = float(input("Introduce la primera calificación: "))
nota2 = float(input("Introduce la segunda calificación: "))
nota3 = float(input("Introduce la tercera calificación: "))
while True:
    print("\n--- MENÚ DE CALIFICACIONES ---")
    print("1. Calcular el promedio")
    print("2. Mostrar la nota mayor")
    print("3. Mostrar la nota menor")
    print("4. Determinar si aprueba o reprueba")
    print("5. Salir del programa")
    opcion = input("Selecciona una opción (del 1 al 5): ")
    if opcion == "1":
        prom = calcular_promedio(nota1, nota2, nota3)
        print(f"El promedio de las calificaciones es: {prom}")
    elif opcion == "2":
        mayor = obtener_mayor(nota1, nota2, nota3)
        print(f"La calificación más alta es: {mayor}")
    elif opcion == "3":
        menor = obtener_menor(nota1, nota2, nota3)
        print(f"La calificación más baja es: {menor}")
    elif opcion == "4":
        prom = calcular_promedio(nota1, nota2, nota3)
        estado = determinar_estado(prom)
        print(f"El estado del estudiante es: {estado}")
    elif opcion == "5":
        print("Ha salido del programa")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
