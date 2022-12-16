#alumnos.csv ----> Padrón, Nombre, Apellido, Carrera, Año de Ingreso 
#materias.csv ----> Padrón, materia1, nota1, materia2, nota2, materia3, nota3, … , materiaN , notaN 
import csv


def antiguedad_promedio(carreras:list):
    datos = list()
    lista_promedios = list()

    with open("alumnos.csv", newline='', encoding="UTF-8") as archivo_csv:
        csv_reader = csv.reader(archivo_csv, delimiter=',')
        next(csv_reader) #Evitamos leer el header
        for row in csv_reader:
            datos.append([row[3],int(row[4])])
    for carrera in carreras:
        total = 0
        contador = 0
        for tupla in datos:
            if tupla[0] == carrera:
                total += tupla[1]
                contador += 1
        lista_promedios.append([carrera,(total/contador)])

    for tupla in lista_promedios:
        print(f"{tupla[0]}: {tupla[1]}.")

def mejor_alumno():
    datos = list()
    prom_alumno =list()
    alumnos_list = list()

    with open("materias.csv", newline='', encoding="UTF-8") as archivo_csv:
        csv_reader = csv.reader(archivo_csv, delimiter=',')
        next(csv_reader) #Evitamos leer el header
        for row in csv_reader:
            datos.append(row)
    for tupla in datos:
        notas = list()
        for i in range(len(tupla)):
            if i != 0 and i % 2 == 0:
                notas.append(int(tupla[i]))
        promedio = sum(notas)/len(notas)
        prom_alumno.append([tupla[0],promedio])    

    prom_alumno.sort(reverse=True, key=lambda x: x[1])

    with open("alumnos.csv", newline='', encoding="UTF-8") as alumnos:
        csv_reader = csv.reader(alumnos, delimiter=',')
        next(csv_reader) #Evitamos leer el header
        for row in csv_reader:
            alumnos_list.append([row[0],row[1],row[2]])

    for alumno in alumnos_list:
        if alumno[0] == prom_alumno[0][0]:
            print(f"El alumno {alumno[1]} {alumno[2]} tiene el mejor promedio y es de {prom_alumno[0][1]}")

def procesar_csv(archivo:str):
    datos = list()
    with open(archivo, newline='', encoding="UTF-8") as archivo_csv:
        csv_reader = csv.reader(archivo_csv, delimiter=',')
        next(csv_reader) #Evitamos leer el header
        for row in csv_reader:
            datos.append(row)

    return datos

def convertir_list_int(lista:list):
    for elemento in lista:
        for i in range(len(elemento)):
            if i != 0 and i % 2 == 0:
                elemento[i] = int(elemento[i])
    return lista

def promedio_aprobadas():
    carrera = input("Por favor ingrese que carrera desea buscar?: ")
    alumnos_csv = procesar_csv("alumnos.csv")
    materias_csv = procesar_csv("materias.csv")
    padrones = list()
    notas_carrera = list()
    promedios = list()

    for alumno in alumnos_csv:
        if alumno[3] == carrera:
            padrones.append(alumno[0])

    for alumno in materias_csv:
        for padron in padrones:
            if alumno[0] == padron:
                notas_carrera.append(alumno)

    notas_carrera_int = convertir_list_int(notas_carrera) #convierto todo a int

    for tupla in notas_carrera_int:
        aprobado = 0
        desaprobado = 0
        for i in range(len(tupla)):
            if i != 0 and i % 2 == 0:
                if tupla[i] >= 6:
                    aprobado += 1 
                else:
                    desaprobado += 1
        promedio = (aprobado/(aprobado + desaprobado))*100
        promedios.append(promedio)
    
    
    print(f"El promedio de materias aprobadas por alumno es de {sum(promedios)/len(promedios)}%")
                    
#alumnos.csv ----> Padrón, Nombre, Apellido, Carrera, Año de Ingreso 
#materias.csv ----> Padrón, materia1, nota1, materia2, nota2, materia3, nota3, … , materiaN , notaN 

def dep_mayor_aprobacion(carreras:list):
    alumnos_csv = procesar_csv("alumnos.csv")
    materias_csv = procesar_csv("materias.csv")
    promedios_carrera = list()
    materias_csv = convertir_list_int(materias_csv) #convierto todo a int

    for carrera in carreras:
        aprobadas = 0
        for alumno in alumnos_csv:
            for tupla in materias_csv:
                if alumno[3] == carrera:
                    if alumno[0] == tupla[0]:
                        for i in range(len(tupla)):
                            if i != 0 and i % 2 == 0:
                                if tupla[i] >= 6:
                                    aprobadas += 1 

        promedios_carrera.append([carrera,aprobadas])
    
    promedios_carrera.sort(reverse=True, key=lambda x: x[1])
    print(f"La mayor cantidad de materias aprobadas la tiene {promedios_carrera[0][0]} con {promedios_carrera[0][1]}.")


def main():
    carreras = [" Ing. en Informática"]
    print("""
    a- Procesar información de entrada
    b- Determinar la antigüedad promedio por carrera de los alumnos activos
    indicando la fecha actual
    c- Indicar cual es el mejor alumno activo de la facultad (en base a su promedio)
    d- Determinar el promedio de materias aprobadas de los alumnos de una
    carrera que se le solicita al usuario
    e- Indicar cual es el departamento con mayor cantidad de materias aprobadas.""")

    eleccion = int(input("Que opcion desea realizar?: "))
    if eleccion == 1:
        pass
    elif eleccion == 2:
        antiguedad_promedio(carreras)
    elif eleccion == 3:
        mejor_alumno()
    elif eleccion == 4:
        promedio_aprobadas()
    elif eleccion == 5:
        dep_mayor_aprobacion(carreras)
main()