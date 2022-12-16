import csv

def procesar_csv(archivo:str):
    datos = list()
    try:
        with open(archivo, newline='', encoding="UTF-8") as archivo_csv:
            csv_reader = csv.reader(archivo_csv, delimiter=',')
            for row in csv_reader:
                datos.append(row)
    except FileNotFoundError:
        print("El archivo csv es inexsistente. Intente nuevamente.")
    return datos

def crear_csv_lista(lista:list,archivo:str):
    with open(archivo,'w', newline='') as fd:
        writer = csv.writer(fd)
        writer.writerows(lista)

def agregar_gasto(gastos:list):
    concepto = input("Por favor ngrese el concepto del gasto: ")
    importe = int(input("Por favor ingrese el importe del gasto: "))
    gastos.append([concepto,importe])
    with open('Gastos.csv','a') as fd:
        fd.write(f"{concepto}, {importe}")

def eliminar_gasto(gastos:list):
    concepto = input("Por favor ngrese el concepto del gasto a eliminar: ")
    for item in gastos:
        if item[0] == concepto:
            gastos.remove(item)

    with open('Gastos.csv','w', newline='') as fd:
        writer = csv.writer(fd)
        writer.writerows(gastos)

def calcular_dinero_recaudado_y_gastos(ventas:list,gastos:list):
    total = 0
    gastos_mes = 0
    for item in ventas:
        total += (item[4]*item[2])

    for item in gastos:
        item[1] = item[1].strip(" ")
        item[1] = int(item[1])
        gastos_mes += item[1]

    if total >= gastos_mes:
        print(f"\nEl total de dinero recaudado es de ${total} y alcanza para cubrir los gastos del mes.\n")
    else:
        print(f"\nEl total de dinero recaudado es de ${total} y no alcanza para cubrir los gastos del mes. Estarian faltando ${gastos_mes-total}.\n")

def sacar_espacio_a_int(lista:list,item_a_modificar:int):
    for item in lista:
        item[item_a_modificar] = item[item_a_modificar].strip(" ")
        item[item_a_modificar] = int(item[item_a_modificar])

def top_prod_mas_comprados(ventas:list):
    sacar_espacio_a_int(ventas,4)
    ventas.sort(reverse=True, key=lambda x: x[4])   

    for i in range(3):
        print(f"{[ventas[i]]}")

def porcentajes_gastos(gastos:list):
    total = 0
    sacar_espacio_a_int(gastos,1)

    for item in gastos:
        total += item[1]
    for item in gastos:
        item.append(round(item[1]/total*100,2))
    gastos.sort(reverse=True, key=lambda x: x[2])  
    for item in gastos:
        print(item)
    
def indicencia_vendidos_gastos(ventas:list,gastos:list):
    total = 0
    sacar_espacio_a_int(gastos,1)

    for item in gastos:
        total += item[1]
    
    for info in ventas:
        info[4] = int(info[4])
        info[2] = int(info[2])
        total_vendido = info[4]*info[2]
        info.append(round(total_vendido/total*100,2))
    ventas.sort(reverse=True, key=lambda x: x[6])
    for item in ventas:
        print(item)

def elecciones(ventas:list,gastos:list,eleccion:int) -> str:
    if len(ventas) == 0:
        ventas = procesar_csv("Ventas.csv")
        gastos = procesar_csv("Gastos.csv")
    if eleccion == 1:
        print("Archivo procesado con exito.\n")
    elif eleccion == 2:
        opciones = int(input("""
        1. Agregar gasto.
        2. Borrar Gasto
        Que desea hacer?: """))
        if opciones == 1:
            agregar_gasto(gastos)
        elif opciones == 2:
            eliminar_gasto(gastos)
    elif eleccion == 3:
        calcular_dinero_recaudado_y_gastos(ventas,gastos)
    elif eleccion == 4:
        top_prod_mas_comprados(ventas)
    elif eleccion == 5:
        porcentajes_gastos(gastos)
    elif eleccion == 6:
        indicencia_vendidos_gastos(ventas,gastos)

    seguir = input("Desea seguir utilizando el programa? (s/n): ")

    return seguir


def main() -> None:
    seguir = "s"
    ventas = list()
    gastos = list()
    while seguir == "s":
        print("""
1. Procesar el archivo "Ventas.csv" y Gastos.csv” (cargarlo en el programa).
2. Permitir agrega o eliminar un gasto del archivo gastos.csv
3. Mostrar por pantalla la cantidad de dinero recaudado, informando si el mismo
alcanza para cubrir los gastos del mes, en el caso de no alcanzar mostrar el
importe faltante para llegar.
4. Mostrar por pantalla el top 3 de los productos más comprados por clientes.
5. Listar ordenado descendentemente el % que representa cada uno de los gastos
sobre el total de los mismos.
6. Mostrar la incidencia en % de cuánto representa cada uno de los artículos
vendidos sobre el total de los gastos.
    """)

        eleccion = int(input("Seleccione la opcion: "))
        seguir = elecciones(ventas,gastos,eleccion)

main()
