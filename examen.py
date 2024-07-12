#importamos librerias necesarias para el funcionamiento del codigp
import csv
import random
import math

#creamos la lista con los nombres de los empleados
trabajadores = ['Juan Pérez','Maria Garcia','Carlos Lopez',
                'Ana Martinez','Pedro Rodriguez','Laura Hernandez',
                'Miguel Sanchez','Isabel Gomez','Francisco Diaz',
                'Elena Fernandez']

#reamos un diccionario donde se almacenara por clave valor los empleados con sus respectivos sueldos
dicc_trabajadores = {'Juan Perez':0,'Maria Garcia':0,'Carlos Lopez':0,
                    'Ana Martinez':0,'Pedro Rodriguez':0,'Laura Hernandez':0,
                    'Miguel Sanchez':0,'Isabel Gomez':0,'Francisco Diaz':0,
                    'Elena Fernandez':0}

#definimos variables para su uso posterios (buenas practicas)
key = 0
sueldo = 0

#definimos la funcion de asignar sueldos
def asignar_sueldos():
    for trabajador in dicc_trabajadores:   #por cada trabajador dentro del diccionario:
        sueldo = random.randint(300000, 2500000)   #vamos a generar un sueldo aleatorio entre 300.000 y 2.500.000 y lo guardamos
        dicc_trabajadores[trabajador] = sueldo   #en el diccionario vamos a buscar por clave [trabajador] y en el valor, agregamos el sueldo
    print('\nsueldos asignados, listando..\n')
    for trabajador in dicc_trabajadores:   #por cada trabajador dentro del diccionario:
        print(f'{trabajador} -${dicc_trabajadores[trabajador]}')   #vamos a imprimir cada trabajador con su respectivo sueldo

#definimos la funcion de asignar sueldos
def clasificar_sueldos():
    lista_menor = []   #creamos 3 listas que se vacian cada vez que llamamos la funcion, para que no se acumulen datos
    lista_entre = []
    lista_mayor = []
    total_sueldos = sum(dicc_trabajadores[x] for x in dicc_trabajadores)   #funcion para sumar todos los sueldos en una variable
    for trabajador in dicc_trabajadores:   #por cada trabajador dentro del diccionario
        if dicc_trabajadores[trabajador] < 800000:   #vamos a agregar a una lista de sueldos menores a 800.000
            lista_menor.append(trabajador)
        elif dicc_trabajadores[trabajador] >= 800000 and dicc_trabajadores[trabajador] < 2000000:   #vamos a agregar a una lista de sueldos entre 800.000 y 2.000.000
            lista_entre.append(trabajador)
        elif dicc_trabajadores[trabajador] >= 2000000:   #vamos a agregar a una lista de sueldos mayores a 2.000.000
            lista_mayor.append(trabajador)
    print('\nsueldos clasificados, listando..')
    total = len(lista_menor)   #funcion para leer cuantos trabajadores estan en la lista
    print(f'\nsueldos menores a $800.000    TOTAL: {total}')
    for x in lista_menor:  #por cada trabajador en lista_menor: 
        print(f'{x} -${dicc_trabajadores[x]}')   #se imprime el nombre junto a su sueldo
    total = len(lista_entre)
    print(f'\nSueldos entre $800.000 y $2.000.000    TOTAL: {total}')
    for x in lista_entre:
        total = len(lista_entre)
        print(f'{x} -${dicc_trabajadores[x]}')
    total = len(lista_mayor)
    print(f'\nsueldos mayores a $2.000.000    TOTAL: {total}')
    for x in lista_mayor:
        total = len(lista_mayor)
        print(f'{x} -${dicc_trabajadores[x]}')
    print(f'\nTotal suma sueldos: ${total_sueldos}')    #se imprime el sueldo total de la empresa

#funcion para ver estadisticas
def ver_estadisticas():
    sueldo_menor = min(dicc_trabajadores, key=lambda x: dicc_trabajadores[x])   #busca el trabajador con menor sueldo dentro del diccionario, cuando lo encuentre lo guarda en sueldo_menor
    sueldo_mayor = max(dicc_trabajadores, key=lambda x: dicc_trabajadores[x])   #lo mismo pero busca el trabajador con mayor sueldo
    promedio_sueldo = sum(dicc_trabajadores[x] for x in dicc_trabajadores) / len(dicc_trabajadores)   #calcula el promedio de todos los sueldos, se suman todos los sueldos y se divide por la cantidad de trabajadores
    producto_sueldo = math.prod(dicc_trabajadores[x] for x in dicc_trabajadores)   #calcula el producto de todos los sueldos
    media_geometrica = producto_sueldo ** (1/len(dicc_trabajadores))   #calcula la media geometrica con el producto calculado
    print('\nestadisticas listas, mostrando..')   #imprime las estadisticas
    print(f'\nSueldo mas bajo: {sueldo_menor} -${dicc_trabajadores[sueldo_menor]}')
    print(f'\nSueldo mas alto: {sueldo_mayor} -${dicc_trabajadores[sueldo_mayor]}')
    print(f'\npromedio de sueldos: ${promedio_sueldo}')
    print(f'\nMedia Geometrica: - {media_geometrica:.2f}')   #acorta la respuesta del producto a 2 digitos despues del punto

#funcion para generar un reporte a traves de un archivo csv
def generar_reporte():
    with open('reporte_sueldos.csv', 'w') as file:   #abriremos un archivo csv en modo escritura
        write = csv.writer(file)
        write.writerow(['Nombre emmpleado','Sueldo base','Descuento salud','Descuento AFP','Sueldo liquido'])   #escribimos dentro del archivo todos los parametros que vamos a guardar
        for trabajador in dicc_trabajadores:      #por cada trabajador dentro del diccionario:
            dcto_salud = dicc_trabajadores[trabajador] * 0.07   #calcula el descuento de salud del trabajador
            dcto_afp = dicc_trabajadores[trabajador] * 0.12   #calcula el descuento de afp del trabajador
            dcto_salud = round(dcto_salud,2)   #redondea la respuesta a  digitos despues del punto
            dcto_afp = round(dcto_afp,2)
            sueldo_liquido = dicc_trabajadores[trabajador] - dcto_salud - dcto_afp   #calculamos el sueldo liquido del trabajador, restando su sueldo base menos los descuentos
            write.writerow([trabajador,dicc_trabajadores[trabajador],dcto_salud,dcto_afp,sueldo_liquido])   #agregamos los datos en una nueva linea
    print('\nreporte generaqdo exitosamente')

#inicio del menu
while True:
    print('''\n--MENU SUELDO DE EMPLEADOS--
1) ASIGNAR SUELDOS ALEATORIOS
2) CLASIFICAR SUELDOS
3) VER ESTADISTICAS
4) GENERAR REPORTE
9) SALIR DEL PROGRAMA
    ''')

    try: key = int(input('\ningrese una opcion: ')) #intentara almacenar un numero dentro de la variable
    except Exception: print('ingrese una opcion valida') #excepto que no sea numero, lanzara un mensaje
    if key == 1:   #preguntara por cada opcion
        asignar_sueldos()
    elif key == 2:
        clasificar_sueldos()
    elif key == 3:
        ver_estadisticas()
    elif key == 4:
        generar_reporte()
    elif key == 9:   #cierra el bucle
        print('Cerrando programa..\nDesarrollado por Felipe Vásquez\nRUT 21.706.087-7')
        break