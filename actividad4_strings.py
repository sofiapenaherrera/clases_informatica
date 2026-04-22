stringVariasLineas = """
Sofía Peñaherrera
Ruta 3
"""
print(stringVariasLineas)

# Método 1
colegio="ISM"
longitud = len(colegio)
print(longitud)
# Método 2
print(len(colegio))
# Método 3
print(len("San Francisco de Quito"))
#%%
nombre = "Sofía"
apellido = "Peñaherrera"
nombre_completo = nombre + " " + apellido
print(nombre_completo)
print("Mi nombre completo es" + " " + nombre_completo+".")
print("Mi nombre completo es",nombre_completo+".")
print(nombre_completo*3)
#%%
#Modificadores de strings
print("python\nchallenge")
print("nombre\tSemana1\tSemana2\tSemana3")
print("simbolo(\\)")
#Nueva técnica de print
print(f"Mi nombre es : {nombre} y mi apellido es : {apellido}")
#desempaquetado de caracteres
a,b,c,d,e = nombre
print(a)
print(b)
print(c)
print(d)
print(e)
#indexación de strings
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])
print(nombre[-1])
primerosTres=nombre[0:3]  #No cuenta el 3, es decir solo me dará el 0, 1 y 2.
print(primerosTres)
#Método 1
últimosTres=nombre[2:5]  #No cuenta el 2, es decir solo me dará el 3, 4 y 5.
print(últimosTres)
#Método 2
últimosTres=nombre[-3:]  #Me dará los últimos 3 caracteres sin importar la longitud del string.
print(últimosTres)
# Para invertir un string
print(nombre[::-1])
# Para saltarme caracteres
print(nombre[0:5:2])  # Me dará los caracteres en las posiciones 0, 2 y 4. 0=inicio, 5=fin, 2=salto/incremento

#%%
#Métodos de strings
print(nombre.capitalize())  #Convierte el primer carácter a mayúscula y el resto a minúscula
print(nombre.count("a"))  #Cuenta cuántas veces aparece el carácter "a" en el string
print(nombre.find("f"))  #Devuelve la posición del primer carácter "f" en el string, si no lo encuentra devuelve -1
print(nombre.replace("a", "o"))  #Reemplaza todas las apariciones de "a" por "o" en el string
print(nombre.split("a"))  #Divide el string en una lista usando "a" como separador
print(nombre.strip())  #Elimina los espacios en blanco al inicio y al final del string
print(nombre.upper())  #Convierte el string a mayúsculas
print(nombre.lower())  #Convierte el string a minúsculas

#DEBER
#Nivel 1
texto = "Programación Para Todos"
#%%
print(texto)
print("Cantidad de caracteres:", len(texto))
#%%
#Nivel 2
print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.capitalize())
#%%
#Nivel 3
print(texto.startswith("Programación"))
print(texto.endswith("Todos"))
print(texto.find("Para"))
print("Python" in texto)
# %%
#Nivel 4
print(texto.replace("Programación", "Python"))

palabras = texto.split()
print(palabras)

print(" - ".join(palabras))
#%%
# Nivel 5
print(texto[0])
print(texto[-1])
print(texto[5])
#%%
#Nivel 6
nombre_completo = "Sofía Peñaherrera"

print(f"Hola, mi nombre es {nombre_completo})

# Acrónimo
nombre = "Sofía"
apellido = "Peñaherrera"

print(nombre[0] + apellido[0])
