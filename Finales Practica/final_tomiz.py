import csv

ACCIONES = ["Procesar archivos 'Ventas.csv' y 'Gastos.csv'",
            "Agregar o eliminar un gasto del archivo gastos.csv",
            "Mostrar la cantidad de dinero recaudado, informando si el mismo alcanza para cubrir los gastos del mes, en el caso de no alcanzar mostrar el importe faltante para llegar",
             "Mostrar por pantalla el top 3 de los productos más comprados por clientes",
             "Listar ordenado descendentemente el % que representa cada uno de los gastos sobre el total de los mismos",
             "Mostrar la incidencia en porcentaje de cuánto representa cada uno de los artículos vendidos sobre el total de los gastos"]

HEADER_VENTAS = ["ID producto", "nombre", "precio por kilo", 
                "cantidad por kilo en stock", "cantidad por kilo vendida", "cantidad de clientes que compraron"]

HEADER_GASTOS = ["Concepto","importe"]

def procesar_archivo_ventas()->dict:
    lista_de_ventas = list()
    ventas = dict()

    with open("ventas.csv","r") as archivo_csv:
        leer = csv.reader(archivo_csv, delimiter=',')
        for linea in leer:
            if linea[0] != HEADER_VENTAS[0]:
                lista_de_ventas.append(linea)

    for venta in lista_de_ventas:
        id = venta[0]
        nombre = venta[1]
        precio_x_kg = venta[2]
        stock = venta[3]
        vendido = venta[4]
        n_de_clientes_que_compraron = venta[5]
        ventas[id] = {"Nombre": nombre, "Precio por Kilo": precio_x_kg, "Cantidad por kilo en stock":stock, 
                        "Cantidad por kilo vendida": vendido, "Cantidad de clientes que compraron":n_de_clientes_que_compraron}
    
    return ventas


def procesar_archivo_gastos()->dict:
    lista_de_gastos = list()
    gastos = dict()

    with open("gastos.csv","r") as archivo_csv:
        leer = csv.reader(archivo_csv, delimiter=',')
        for linea in leer:
            if linea[0] != HEADER_GASTOS[0]:
                lista_de_gastos.append(linea)

    for gasto in lista_de_gastos:
        concepto = gasto[0]
        importe = gasto[1]
        gastos[concepto] = importe

    return gastos


def top3(ventas:dict)->None:
    diccionario_de_n_clientes = dict()
    lista_de_n_clientes = list()
    
    for informacion in ventas.values():
        diccionario_de_n_clientes[informacion["Nombre"]] = informacion["Cantidad de clientes que compraron"]

    for informacion in diccionario_de_n_clientes.items():
        lista_de_n_clientes.append(informacion)
    lista_de_n_clientes.sort(key=lambda x:x[1],reverse=True)
    
    while len(lista_de_n_clientes) > 3:
        lista_de_n_clientes.pop()

    print(f"El top 3 productos mas vendidos es {lista_de_n_clientes}")


def porcentaje_gastos(gastos:dict)->None:
    dicc_porcentajes = dict()
    lista_porcentajes = list()
    gasto_total=0

    for gasto in gastos.values():
        gasto_total += int(gasto)

    for concepto in gastos:
        dicc_porcentajes[concepto] = int(gastos[concepto])*100/gasto_total
        
    for informacion in dicc_porcentajes.items():
        lista_porcentajes.append(informacion)
    lista_porcentajes.sort(key=lambda x:x[1],reverse=True)
    
    print(lista_porcentajes)

def agregar_gastos()->None:
    concepto = input("Que concepto queres agregar? ")
    valor = input("Cual es el valor del concepto? ")
    linea =[concepto,valor]

    with open("gastos.csv","a",newline="") as archivo_csv:
        escribir = csv.writer(archivo_csv)
        escribir.writerow(linea)

    print("Gasto agregado con exito!") 


def borrar_gastos()->None:
    lineas = list()
    concepto = input("Que concepto queres eliminar? ")

    with open("gastos.csv","r") as archivo_csv:
        leer = csv.reader(archivo_csv)
        for linea in leer:
            lineas.append(linea)
        for informacion in lineas:
            if informacion[0] == concepto:
                lineas.remove(informacion)
    
    with open("gastos.csv","w",newline="") as archivo_csv:
        escribir = csv.writer(archivo_csv)
        escribir.writerows(lineas)

    print("Gasto eliminado con exito!")


def modificar_gastos():
    gastos = dict()
    seleccionador = int(input("1. Agregar Datos, 2. Borrar Datos -> "))
    
    if seleccionador == 1:

        agregar_gastos()   
        gastos = procesar_archivo_gastos()
        
    if seleccionador ==2:
        
        borrar_gastos()
        gastos = procesar_archivo_gastos()

    return gastos

def dinero_recaudado(gastos:dict,ventas:dict)->None:
    recaudado = 0
    gastado = 0

    for gasto in gastos:
        gastado += int(gastos[gasto])

    for informacion in ventas.values():
        recaudado += int(informacion["Cantidad por kilo vendida"]) * int(informacion["Precio por Kilo"])

    if recaudado - gastado >0:
        print(f"Recaudamos {recaudado}$ y alcanza para cubrir los gastos del mes")
    else:
        print(f"Recaudamos {recaudado}$ pero no alcanza para cubrir los gastos del mes por {gastado - recaudado}$")


def ingresar_opcion(opciones:list)->int:
    print("")
    for x in range(len(opciones)):
        print(f"{x + 1} - {opciones[x]}")
    opcion = int(input("Ingrese una opción: "))
    return opcion


def main()->None:
    ventas = dict()
    gastos = dict()

    opcion = ingresar_opcion(ACCIONES)

    while opcion <= len(ACCIONES) and opcion > 0:
        if opcion == 1:
            try:
                ventas = procesar_archivo_ventas() #Por si el archivo no existe
                gastos = procesar_archivo_gastos()
                print("Archivos Procesados!")
            except:
                print("Error: El/Los archivo/s no se ha/han podido procesar")
            opcion = ingresar_opcion(ACCIONES)

        if opcion == 2:
            gastos = modificar_gastos()
            opcion = ingresar_opcion(ACCIONES)

        if opcion == 3:
            dinero_recaudado(gastos,ventas)
            opcion = ingresar_opcion(ACCIONES)

        if opcion == 4:
            top3(ventas)
            opcion = ingresar_opcion(ACCIONES)

        if opcion == 5:
            porcentaje_gastos(gastos)
            opcion = ingresar_opcion(ACCIONES)

        if opcion == 6:
            pass
            opcion = ingresar_opcion(ACCIONES)
        
    print("Cerrando...")
main()