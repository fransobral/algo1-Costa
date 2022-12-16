def procesar_txt(archivo: str) -> dict:
    lista_ordenada = list()
    try:  # aca utilizo un try except ya que si no exsiste nav.txt se rompe el programa.
        with open(archivo, "r") as archivo:
            for linea in archivo:
                linea_separada = linea.split(",")
                lista_ordenada.append(linea_separada)
        print("Archivo creado con exito.\n")
    except FileNotFoundError:
        print("El archivo stock no exsiste, inetnte nuevamente.")

    return lista_ordenada

def crear_archivo_txt(nombre:str,estado:list,costo_portuario:float) -> None:
    try:  # aca uso try except por si ocurre algun problema al crear el archivo.
        with open(nombre, 'w') as archivo:
            for tupla in estado:
                archivo.write(f"{tupla[0]},{tupla[1]},{tupla[2]},{tupla[3]},{tupla[4]},{tupla[5]},{tupla[6][:-1]}\n")
            archivo.write(f"El costo portuario total es de ${costo_portuario}.")
        print("Archivo creado con exito.")
    except:
        print("Error creando el archivo.")

def top_3_ciudades_puertos(nav:list) -> None:
    nav.sort(reverse=True, key=lambda x: x[2])
    lista_repeticiones = list()
    cantidad_repeticiones = 0
    origen_anterior = nav[0][2]
    
    for info in nav:
        if info[2] == origen_anterior:
            cantidad_repeticiones += 1
            origen_anterior = info[2]
        else:
            lista_repeticiones.append([origen_anterior,cantidad_repeticiones])
            cantidad_repeticiones = 1
            origen_anterior = info[2]
    lista_repeticiones.sort(reverse=True, key=lambda x: x[1])

    for i in range(3):
        print(f"{lista_repeticiones[i][0]}, {lista_repeticiones[i][1]} viajes.\n")

def buscar_viaje_demorado(nav:list) -> None:
    lista_rango_horario = list()
    for info in nav:
        info[3] = int(info[3])
        if (info[3] >= 700) and (info[3] <= 745) and info[6] == " demorado\n": 
            lista_rango_horario.append(info)

    lista_rango_horario.sort(reverse=True, key=lambda x: x[5])
    for item in lista_rango_horario:
        print(f"Viaje Nª {item[0]}, Eslora {item[5]}")

def informacion_por_empresa(nav:list) -> None: 
    lista_empresa = list()
    total_pasajeros = 0
    empresa = input("Por favor ingrese la empresa para brindarle la informacion: ")

    for info in nav:
        info[4] = int(info[4])
        total_pasajeros += info[4]
        info[1] = info[1].strip(" ")
        if empresa == info[1]:
            lista_empresa.append(info)

    promedio_pasajeros = round(total_pasajeros/len(nav),2)

    for info in lista_empresa:
        if info[4] > promedio_pasajeros:
            print(f"\nViaje Nª: {info[0]}, Empresa: {info[1]}, Origen:{info[2]}, Hra LLegada:{info[3]},  Pasajeros: {info[4]}, Eslora:{info[5]}, Estado:{info[6][:-1]}")
        
def calcular_costo_portuario(lista_estado:list)-> float:
    costo_portuario = float()
    for info in lista_estado:
        costo_portuario += (2000 + (33.22 * float(info[5])))
        
    return round(costo_portuario,2)

def crear_archivos_por_estado(nav:list) -> None:
    estimado = list()
    demorado = list()
    arribando = list()
    for info in nav:
        if info[6] == " estimado\n":
            estimado.append(info)
        elif info[6] == " arribando\n":
            arribando.append(info)
        elif info[6] == " demorado\n":
            demorado.append(info)

    costo_portuario_estimado = calcular_costo_portuario(estimado)
    costo_portuario_demorado = calcular_costo_portuario(demorado)
    costo_portuario_arribando = calcular_costo_portuario(arribando)

    crear_archivo_txt("estimado.txt",estimado,costo_portuario_estimado)
    crear_archivo_txt("demorado.txt",demorado,costo_portuario_demorado)
    crear_archivo_txt("arribando.txt",arribando,costo_portuario_arribando)
    
def elecciones(nav:list,eleccion:int) -> str:       
    if eleccion == 2:
        top_3_ciudades_puertos(nav)
    elif eleccion == 3:
        buscar_viaje_demorado(nav)
    elif eleccion == 4:
        informacion_por_empresa(nav)
    elif eleccion == 5:
        crear_archivos_por_estado(nav)

    seguir = input("\nDesea seguir utilizando el programa? (s/n): ")

    return seguir


def main() -> None:
    seguir = "s"
    nav = list()
    while seguir == "s":
        print("""
1- Procesar el archivo “nav.txt” y volcarlo en una estructura que luego le
permita iniciar la resolución del resto de puntos.
2- Determinar el top 3 de ciudades son las más utilizadas como puertos de
origen para cualquiera de los cruceros que llegan a Taormina.
3- Buscar todos los arribos entre las 0700 y las 0745 y que estén demorados.
Desplegar Viaje nro y eslora, ordenado por eslora de mayor a menor.
4- Permitir al usuario ingresar una empresa naviera y que el programa liste por
pantalla toda la información de los viajes que tienen una cantidad de pasajeros mayor
al promedio general de todos los viajes.
5- Crear 3 archivos de textos uno por cada estado, que contenga la información
de todas las embarcaciones ordenadas por horario. La última línea de cada archivo debe
indicar el costo total de operación portuaria. Los archivos se deberán llamar,
estimado.txt, demorado.txt y arribando.txt
    """)

        eleccion = int(input("Seleccione la opcion: "))
        if eleccion == 1:
            nav = procesar_txt("nav.txt")
            eleccion = int(input("Seleccione que opcion desea realizar: "))
        elif len(nav) == 0:
            print("\nUsted no proceso el archivo, lo haremos por usted.\n")
            nav = procesar_txt("nav.txt")

        seguir = elecciones(nav,eleccion)

main()
