# 1. Definición de la función con parametros
def calcular_area_rectangulo(base, altura):
    # proceso: calcular el área
    area = base * altura

    # 2. Uso de la palabra clave ´return´
    return area
# --- Bloque principal del programa ---

# Entradas (puedes pedirlas al usuario o definirlas)
b = 10.5
h = 5.0

# Llamada a la función pasando los parámetros
resultado = calcular_area_rectangulo(b, h)

# 4. Mostrar el resultadoen pantalla
print(f"El área del rectángulo con base {b} y altura {h} es {resultado}")