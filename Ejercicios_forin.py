# Ejercicio 1
numbers=[0,1,2,3,4,5]
for number in numbers:
    print(number)
# Ejercicio 2
notas = [8, 7, 9, 10, 6]
suma = 0
contador=0
for nota in notas:
    suma = suma + nota
    contador+=1
promedio = suma / contador
print(f"El promedio es: {promedio}")
# Ejercicio 3
language = "S o f y "
for letter in language:
    print(letter)
# Ejercicio 4
palabra = input("Ingrese una palabra: ")
vocales = 0
consonantes = 0
for letra in palabra.lower():
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        vocales += 1
    else:
        consonantes += 1
print(f"La palabra '{palabra}' tiene {vocales} vocales y {consonantes} consonantes, tiene {consonantes + vocales} caracteres en total")
# Ejercicio 5
it_companies = {'Facebook','Facebook'}
for company in it_companies:
    print(company)
# Ejercicio 6
numbers=[0,1,2,3,4,5]
usuario=int(input("Ingrese un número: "))
for number in numbers:
    if number == usuario:
        print("Número encontrado")
        break 
else:
    print("Numero no encontrado")
# Ejercicio 8
cedula = input("Ingrese su cédula: ")
cedulaLimpia = ""
for caracter in cedula:
    if caracter == '-' or caracter == " ":
        continue
    cedulaLimpia += caracter
print(cedulaLimpia)
