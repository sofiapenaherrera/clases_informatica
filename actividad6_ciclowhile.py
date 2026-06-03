numero=0
while numero < 5:
    print(f"Esta es la vuelta {numero}")
    numero += 1
print("El ciclo ha terminado")
#%%
clave = " "
while clave != "sofy":
    clave = input("Ingrese la clave: ")
print("¡Clave correcta!")
#%%
opcion = " "
while opcion != "C":
    print("Menú de opciones:")
    print("Opción A: Saludar")
    print("Opción B: Mostrar mensaje")
    print("Opción C: Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "A":
        print("Hola")
    elif opcion == "B":
        print("Estamos aprendiendo ciclos while")
    elif opcion == "C":
        print("Saliendo del programa")
    else:
        print("Opción no válida")
#%%
clave_correcta = "python123"
clave = ""
while clave != clave_correcta:
    clave = input("Ingrese la clave de acceso: ")
    if clave == clave_correcta:
        print("Acceso permitido")
    else:
        print("Clave incorrecta. Intente nuevamente.")
print("Bienvenido al sistema de habilitación para el reto final de Python")
temas = ["variables", "cálculos", "input", "print", "f-string", "condicionales", "ciclos"]
print("Temas evaluados en la unidad:")
for tema in temas:
    print(f"- {tema}")
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes a revisar: "))
for i in range(cantidad_estudiantes):
    print(f"Registro del estudiante {i + 1}")
    nombre = input("Ingrese el nombre del estudiante: ")
    nota_basicos = float(input("Ingrese la nota de ejercicios básicos: "))
    nota_condicionales = float(input("Ingrese la nota de condicionales: "))
    nota_ciclos = float(input("Ingrese la nota de ciclos: "))
    practicas = int(input("Ingrese la cantidad de prácticas completadas: "))
    promedio = (nota_basicos + nota_condicionales + nota_ciclos) / 3
    if promedio >= 9:
        if practicas >= 5:
            estado = "Habilitado con nivel alto"
        else:
            estado = "Pendiente por prácticas"
    elif promedio >= 7:
        if practicas >= 4:
            estado = "Habilitado"
        else:
            estado = "Pendiente por prácticas"
    else:
        estado = "Requiere refuerzo"
    print("Reporte del estudiante")
    print(f"Nombre: {nombre}")
    print(f"Promedio final: {promedio}")
    print(f"Prácticas completadas: {practicas}")
    print(f"Estado académico: {estado}")
print("Proceso finalizado")
