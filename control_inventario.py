# Estudiante: David Santiago Ortegon Serrano
# Grupo: 213022B_2204
# Programa: Ingeniería de Sistemas
# Fase 5 - Evaluación Final POA
# Problema 3: Control de inventario

# Matriz de inventario:
# [Código, Nombre, Stock actual, Stock mínimo]

inventario = [
    ["A001", "Teclado", 8, 15],
    ["A002", "Mouse", 20, 10],
    ["A003", "Monitor", 3, 8],
    ["A004", "Impresora", 12, 12],
    ["A005", "Audífonos", 4, 10]
]


# Función para calcular la cantidad por solicitar
def calcular_reabastecimiento(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad


# Recorrer la matriz y mostrar los resultados
print("REPORTE DE REABASTECIMIENTO DE INVENTARIO")
print("------------------------------------------")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad = calcular_reabastecimiento(
        stock_actual, stock_minimo
    )

    print(f"Artículo: {nombre}")
    print(f"Código: {codigo}")
    print(f"Cantidad por solicitar: {cantidad}")
    print("------------------------------------------")