# Nombre del estudiante: David Lisandro Palacios Molina
# Grupo: 213022_915
# Programa: Ingeniería de sistemas
# Codigo Fuente: Autor

# [ID, Nombre, Stock Actual, Stock Mínimo]
articulos = [
  ["A1","Lapicero",5,10],
  ["A2","Cuaderno",12,10],
  ["A3","Goma",2,5],
  ["A4","Regla",10,10],
  ["A5","Tinta",0,3]
]

# Función para calcular la cantidad a pedir
def pedir(stock_actual, stock_min):
    return max(0, stock_min - stock_actual)

# Función principal
def main():
    # Imprimir el encabezado
    for _, nombre, stock, minimo in articulos:
        cantidad = pedir(stock, minimo)
        if cantidad:
            print(f"Artículo: {nombre}, Cantidad a pedir: {cantidad}")
        elif stock >= minimo:
            print(f"Artículo: {nombre}, No es necesario pedir.")

if __name__ == "__main__":
    main()
    