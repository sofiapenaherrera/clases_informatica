# EJERCICIO LISTAS

notas = [8.5, 6.0, 9.0, 7.0, 5.5]
suma = 0
aprobados = 0
reprobados = 0
for nota in notas:
    suma += nota
    if nota >= 7:
        aprobados += 1
    else:
        reprobados += 1
promedio = suma / 5
print("Suma total:", suma)
print("Promedio:", promedio)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)

# EJERCICIO STRING

contraseña = "Python2026"
letras = 0
numeros = 0
cantidad = 0
for caracter in contraseña:
    if caracter >= 'A' and caracter <= 'Z' or caracter >= 'a' and caracter <= 'z':
        letras += 1
    if caracter >= '0' and caracter <= '9':
        numeros += 1
    if caracter == 'o':
        cantidad += 1
print("Cantidad de letras:", letras)
print("Cantidad de números:", numeros)
print("Cantidad de letras o:", cantidad)

# EJERCICIO CON SET

productos = {"teclado", "mouse", "monitor", "mouse", "impresora"}
cantidad_productos = 0
mas_6 = 0
for producto in productos:
    cantidad_productos += 1
    contador = 0
    for letra in producto:
        contador += 1
    if contador > 6:
        mas_6 += 1
print("Productos únicos:", cantidad_productos)
print("Productos con más de 6 letras:", mas_6)

# EJERCICIO CON BREAK

correo = input("Ingrese su correo: ")
usuario = ""
for caracter in correo:
    if caracter == "@":
        break
    usuario += caracter
print("Nombre de usuario:", usuario)

# EJERCICIO CON CONTINUE

telefono = input("Ingrese su teléfono: ")
telefono_limpio = ""
for caracter in telefono:
    if caracter == " " or caracter == "-":
        continue
    telefono_limpio += caracter
print("Teléfono limpio:", telefono_limpio)