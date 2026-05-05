"""Ejercicio 1: IF ANIDADOS
Enunciado: Sistema de becas
Una universidad asigna becas según promedio, ingreso familiar y participación
extracurricular.
Reglas:
• Si el promedio ≥ 8:
o Si ingreso familiar ≤ 400:
▪ Si participa en actividades → “Beca completa”
▪ Si no participa → “Media beca”
o Si ingreso familiar > 400:
▪ Si participa en actividades → “Media beca”
▪ Si no participa → “Sin beca”
• Si el promedio < 8:
o Si ingreso familiar ≤ 400:
▪ Si participa → “Media beca”
▪ Si no participa → “Sin beca”
o Si ingreso familiar > 400:
▪ “Sin beca”
Condiciones:
• Usar solo if dentro de if
• No usar elif
• No usar AND ni OR"""
# Solicitar datos al usuario
promedio = float(input("Ingrese el promedio académico: "))
ingreso_familiar = float(input("Ingrese el ingreso familiar mensual: "))
participa = input("¿Participa en actividades extracurriculares? (si/no): ").lower()
# Evaluar condiciones para asignar beca
if promedio >= 8:
    if ingreso_familiar <= 400:
        if participa == "si":
            print("Beca completa")
        else:
            print("Media beca")
    else:
        if participa == "si":
            print("Media beca")
        else:
            print("Sin beca")
else:
    if ingreso_familiar <= 400:
        if participa == "si":
            print("Media beca")
        else:
            print("Sin beca")
    else:
        print("Sin beca")
"""Ejercicio 2: ELIF
Enunciado: Sistema de multas de tránsito
Un radar detecta la velocidad de un vehículo y clasifica la infracción.
Reglas:
• Velocidad ≤ 50 → “Sin infracción”
• Velocidad ≤ 70 → “Infracción leve”
• Velocidad ≤ 90 → “Infracción grave”
• Velocidad ≤ 110 → “Multa económica + puntos”
• Velocidad > 110 → “Retención de licencia”
Luego, según la categoría obtenida:
• Si es “Multa económica + puntos” → mostrar: “Debe pagar multa y pierde
10 puntos”
• Si es “Retención de licencia” → mostrar: “Licencia suspendida”"""
ingresa_velocidad = float(input("Ingrese la velocidad del vehículo (km/h): "))
if ingresa_velocidad <= 50:
    print("Sin infracción")
elif ingresa_velocidad <= 70:
    print("Infracción leve")
    
