stringVariasLineas = """
Sofía Peñaherrera
Ruta 3
"""
print(stringVariasLineas)

# Método 2
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