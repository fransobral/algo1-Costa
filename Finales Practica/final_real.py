def crear_dict_ordenado(archivo: str) -> dict:
    diccionario_ordenado = dict()
    try:  # aca utilizo un try except ya que si no exsiste stock.txt se rompe el programa.
        with open(archivo, "r") as archivo:
            for linea in archivo:
                linea_separada = linea.split(",")
                diccionario_ordenado[linea_separada[0]] = [linea_separada[1], linea_separada[2], linea_separada[3], linea_separada[4],
                                                           linea_separada[5], linea_separada[6], linea_separada[7], linea_separada[8], linea_separada[9], linea_separada[10]]
        print("Archivo procesado con exito!\n")
    except FileNotFoundError:
        print("El archivo stock no exsiste, inetnte nuevamente.")

    return diccionario_ordenado


def crear_archivo_ochenta(lista_ordenada: list) -> None:

    try:  # aca uso try except por si ocurre algun problema al crear el archivo.
        with open("ochenta.txt", 'w') as ochenta:
            for tupla in lista_ordenada:
                texto = f"{tupla[0]};{tupla[1]};{tupla[2]};{tupla[3]}"
                ochenta.write(f"{texto}\n")
        print("Archivo creado con exito.")
    except:
        print("Error creando el archivo.")


def promedio_por_talle(stock: dict) -> tuple:
    promedio_talle = list()
    talles = list()
    total = 0

    for datos in stock.values():
        if datos[5] not in talles:
            talles.append(datos[5])

    for talle in talles:
        total_talle = 0
        for datos in stock.values():
            if datos[5] == talle:
                datos[7] = float(datos[7])
                total_talle += datos[7]
                total += datos[7]
        promedio_talle.append([talle,total_talle])

    for item in promedio_talle:
        item[1] = (item[1]/total*100)

    return promedio_talle

def calculador_stock(stock: dict) -> list:
    #stock[key][6] = ingresadas
    #stock[key][7] = vendidas
    stock_final = list()

    for sku, datos in stock.items():
        stock[sku][6] = int(stock[sku][6])
        stock[sku][7] = int(stock[sku][7])
        stock_actual = stock[sku][6] - stock[sku][7]
        if stock_actual > 0:
            stock_final.append(
                [datos[0], datos[1], datos[2], datos[3], datos[4], stock_actual])

    return stock_final

def stock_por_equipo(stock: dict) -> None:
    ventas_equipos = list()
    stock_actual = calculador_stock(stock)
    stock_actual.sort(reverse=True, key=lambda x: x[0])
    item_anterior = stock_actual[0]
    total = 0
    contador = 0

    for item in stock_actual:
        contador += 1
        if item[1] == item_anterior[1]:
            total += item[5]
            item_anterior = item
        else:
            if item_anterior[1] not in ventas_equipos:
                ventas_equipos.append([item_anterior[1], int(total)])
            total = item[5]
            item_anterior = item
        if contador == len(stock_actual):
            ventas_equipos.append([item_anterior[1], int(total)])


    ventas_equipos.sort(reverse=True, key=lambda x: x[1])

    for i in range(3):
        print(f"{i+1}. {ventas_equipos[i][0]} con {ventas_equipos[i][1]}.\n")

def distribución_porcentual_ventas(stock: dict) -> None:
    i = 0
    promedio_talle = promedio_por_talle(stock)
    
    promedio_talle.sort(reverse=True, key=lambda x: x[1])

    print("\nPorcentajes de ventas:\n")
    for tupla in promedio_talle:
        i += 1
        print(f"{i}. Talle {tupla[0]}, %{tupla[1]}.")

def ordenar_dict_anios(stock: dict) -> list:
    anios_list = list()
    for datos in stock.values():
        anios_list.append([datos[3], datos[5], datos[7]])
    anios_list.sort(reverse=True, key=lambda x: x[1])
    return anios_list

def calcular_antiguedad_promedio(stock: dict) -> None:
    stock_ordenado_anio = ordenar_dict_anios(stock)
    anio_anterior = stock_ordenado_anio[0]
    total = 0
    anio = 0
    anios_lista = list()

    for item in stock_ordenado_anio:
        if item[2] != 0:
            if item[0] == anio_anterior:
                total += 1
                anio_anterior = item[0]
            else:
                anios_lista.append([anio, int(total)])
                anio += 1
                total = 1

    anios_lista.sort(reverse=True, key=lambda x: x[0])
    numerador = 0
    dividendo = 0

    for datos in anios_lista:
        numerador += datos[0] * datos[1]
        dividendo += datos[1]
    promedio_ponderado = round(numerador/dividendo, 2)
    print(f"El promedio ponderado de antiguedad es de {promedio_ponderado}.\n")

def stock_valorizado(stock: dict) -> None:
    stock_por_valor = list()
    ochenta_porciento = list()
    valor_total = 0
    suma_porcentaje = 0
    contador = 0
    ochenta_porciento = list()

    for sku, datos in stock.items():
        datos[8] = float(datos[8])
        datos[6] = int(datos[6])
        datos[7] = int(datos[7])
        valor = round((datos[8] * (datos[6] - datos[7])), 2)
        valor_total += valor
        stock_por_valor.append([sku, (datos[6] - datos[7]), valor])

    stock_por_valor.sort(reverse=True, key=lambda x: x[2])

    for items in stock_por_valor:
        items.append(round(items[2]/valor_total*100, 2))

        while suma_porcentaje < 80:
            ochenta_porciento.append(stock_por_valor[contador])
            suma_porcentaje += items[3]
            contador += 1

    crear_archivo_ochenta(ochenta_porciento)


def elecciones(stock: dict, eleccion: int) -> str:
    """if len(stock) == 0:
        stock = crear_dict_ordenado("stock.txt")"""
    if eleccion == 1:
        print("Archivo procesado con exito.\n")
    elif eleccion == 2:
        stock_por_equipo(stock)
    elif eleccion == 3:
        distribución_porcentual_ventas(stock)
    elif eleccion == 4:
        calcular_antiguedad_promedio(stock)
    elif eleccion == 5:
        stock_valorizado(stock)

    seguir = input("Desea seguir utilizando el programa? (s/n): ")

    return seguir


def main() -> None:
    stock = dict()
    seguir = "s"

    while seguir == "s":
        print("""
    1) Procesar archivo.
    2) Mostrar por pantalla los 3 Equipos de los cuales se tienen mayor cantidad de unidades en stock.
    3) Mostrar por pantalla la distribución porcentual de ventas respecto a talles.
    4) Mostrar por pantalla la antigüedad promedio ponderada del stock actual.
    5) Determinar que artículos conforman al menos el 80% del stock valorizado.
    """)
        eleccion = int(input("Seleccione la opcion: "))
        stock = crear_dict_ordenado("stock.txt")
        seguir = elecciones(stock, eleccion)


main()
