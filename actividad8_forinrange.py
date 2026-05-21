# %%
#For in range forma 1
suma = 0
while True:
    cantidad = int(input("¿Cuántas notas desea ingresar? "))
    if cantidad > 0:
        break
    else:
        print("La cantidad debe ser mayor a 0.")
for i in range(cantidad):
    while True:
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        if nota > 0:
            break
        else:
            print("La nota debe ser mayor a 0.")
    suma += nota
promedio = suma / cantidad
print("El promedio es:", promedio)
#For in range con inicio y fin
numero=int(input("Ingrese un número: "))
liminf=int(input("Ingrese el límite inferior: "))
limsup=int(input("Ingrese el límite superior: "))
for i in range (liminf,limsup+1):
    print (f"{numero} x {i} = {numero*i}")
# %%
notas = [5, 8, 9, 7, 10]
suma = 0
for i in range(1, 4):
    suma = suma+notas[i]
promedio = suma / 3
print("El promedio es:", promedio)
#%%
#For in range con incremento
numero = int(input("Ingrese un número: "))
for i in range (9,0, -2):
    print(f"{numero} x {i} = {numero*i}")
