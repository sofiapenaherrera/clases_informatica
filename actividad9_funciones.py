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
print("=== SISTEMA DE COMPRA ===")
subtotal = 0
for i in range(1, 4):
    print(f"\nProducto {i}")
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
print("\n=== RESUMEN DE COMPRA ===")
print(f"Subtotal: ${subtotal}")
print(f"IVA (15%): ${iva}")
print(f"Total a pagar: ${total_pagar}")
