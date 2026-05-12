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
