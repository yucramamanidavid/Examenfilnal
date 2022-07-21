#!/usr/bin/env python
# coding: utf-8
# importaciones de librerias
import time
from utils import limpiarPantalla
from models import Servicio

ruta_archivo = "./archivos/servicios.txt"

def BuscarServicios(codigo):
    servicios = None
    archivoServicio = open(ruta_archivo, "r")
    for linea in archivoServicio.readlines():
        atributo = linea.split(";")
        if codigo == atributo[0]:
            servicios = Servicio(atributo[0], atributo[1], atributo[2], atributo[3], atributo[4])
            break
    archivoServicio.close()

    return servicios

def imprimirRegistro(ruta):
    archivoServicio = open(ruta_archivo, "r")
    print("código\tServicio\t\tDetalle\t\tPrecio\tTiempo")
    for linea in archivoServicio.readlines():
        atributo = linea.split(";")
        print(
            "{}\t{}\t{}\t\t{}\t{}".format(
                atributo[0], atributo[1], atributo[2], atributo[3], atributo[4] 
            )
        )
    archivoServicio.close()


#----------------------------------------------------------------------------#
def Editar_Codigo(ruta, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta, "r+") as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila - 1].split(";")
            columnas[columna] = nuevo_dato
            contenido[fila - 1] = ";".join(columnas) + "\n"
    with open(ruta, "w") as archivo:
        archivo.writelines(contenido)


#------------------------------------------------------------------------------#

def Editar_Servicio(ruta, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta, "r+") as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila - 1].split(";")
            columnas[columna] = nuevo_dato
            contenido[fila - 1] = ";".join(columnas) + "\n"
    with open(ruta, "w") as archivo:
        archivo.writelines(contenido)


#--------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------#
def Editar_Detalle(ruta, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta, "r+") as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila - 1].split(";")
            columnas[columna] = nuevo_dato
            contenido[fila - 1] = ";".join(columnas) + "\n"
    with open(ruta, "w") as archivo:
        archivo.writelines(contenido)


#---------------------------------------------------------------------#
#-------------------------------------------------------------------------------#
def Editar_Precio(ruta, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta, "r+") as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila - 1].split(";")
            columnas[columna] = nuevo_dato
            contenido[fila - 1] = ";".join(columnas) + "\n"
    with open(ruta, "w") as archivo:
        archivo.writelines(contenido)

#---------------------------------------------------------------------#
#---------------------------------------------------------------------#
def Editar_Tiempo(ruta, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta, "r+") as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila - 1].split(";")
            columnas[columna] = nuevo_dato
            contenido[fila - 1] = ";".join(columnas) + "\n"
    with open(ruta, "w") as archivo:
        archivo.writelines(contenido)
#---------------------------------------------------------------------#
#---------------------------------------------------------------------#

def editarservicios():
    while True:
        print("\033[49;96m"+"="*33 + "\033[49;96m")
        print("\033[0m")
        print("\033[49;35m"+"Sub Menu:EDITAR SERVICIOS" + "\033[49;35m")
        print("\033[0m")
        print("\033[49;96m"+"="*33 + "\033[49;96m")
        print("\033[0m")
        print("1. Editar Código")
        print("2. Editar Servicio")
        print("3. Editar Detalle")
        print("4. Editar Presio")
        print("5. Editar Tiempo")
        print("6. regresar al sub menu principal")
        print("\033[49;96m"+"="*33 + "\033[49;96m")
        print("\033[0m")
        op = input("Ingrese una opcion: ")

        match (op):
            case "1":
            
                    limpiarPantalla()
                    imprimirRegistro(ruta_archivo)
                    #----------------------------------------------------------------------------#
                    print("_"*20)

                    codigo = input("Codigo: ") #código que buscara
                    fila = str(BuscarServicios(codigo))# string o cadena de caracteres, es una secuencia inmutable
                    print(f"{fila}")

                    print("_"*20)
                    output = fila.split(";")#output entrega y es la salida del input

                    print("_"*20)
                    print(output)

                    nCodigo = input("Ingrese nuevo Código: ")

                    nFila = int(input("ingrese fila de registro: "))

                    #etiqueta = int(input("que columna quieres cambiar: "))

                    nFila = list(map(int, str(nFila)))#convierte un string a vector

                    print(type[nFila])#permite examinar el tipo a que corresponde un dato determinado, [vector]

                    Editar_Codigo(ruta_archivo, nFila, 0, nCodigo)
                    imprimirRegistro(ruta_archivo)
                    print("Se cambio correctamente el Codigo del Servicio:)")
            case "2":
                    limpiarPantalla()
                    imprimirRegistro(ruta_archivo)

                    print("_"*20)

                    codigo = input("Codigo: ")
                    fila = str(BuscarServicios(codigo))
                    print(f"{fila}")

                    print("_"*20)
                    output = fila.split(";")

                    print("_"*20)
                    print(output)

                    nServicio = input("Ingrese nuevo Servicio: ")

                    nFila = int(input("ingrese fila de registro: "))

                    nFila = list(map(int, str(nFila)))

                    print(type[nFila])

                    Editar_Servicio(ruta_archivo, nFila, 1, nServicio)
                    imprimirRegistro(ruta_archivo)
                    print("Se cambio correctamente el Servicio del Servicio:)")
            case "3":
                    limpiarPantalla()
                    imprimirRegistro(ruta_archivo)
                    #----------------------------------------------------------------------------#
                    print("_"*20)

                    codigo = input("Codigo: ") #código que buscara
                    fila = str(BuscarServicios(codigo))# string o cadena de caracteres, es una secuencia inmutable
                    print(f"{fila}")

                    print("_"*20)
                    output = fila.split(";")#output entrega y es la salida del input

                    print("_"*20)
                    print(output)

                    nDetalle = input("Ingrese nuevo Detalle: ")

                    nFila = int(input("ingrese fila de registro: "))

                    #etiqueta = int(input("que columna quieres cambiar: "))

                    nFila = list(map(int, str(nFila)))#convierte un string a vector

                    print(type[nFila])#permite examinar el tipo a que corresponde un dato determinado, [vector]

                    Editar_Detalle(ruta_archivo, nFila, 2, nDetalle)
                    imprimirRegistro(ruta_archivo)
                    print("Se cambio correctamente el Detalle del Servicio:)")
            case "4":
                    limpiarPantalla()
                    imprimirRegistro(ruta_archivo)
                    #----------------------------------------------------------------------------#
                    print("_"*20)

                    codigo = input("Codigo: ") #código que buscara
                    fila = str(BuscarServicios(codigo))# string o cadena de caracteres, es una secuencia inmutable
                    print(f"{fila}")

                    print("_"*20)
                    output = fila.split(";")#output entrega y es la salida del input

                    print("_"*20)
                    print(output)

                    nPrecio = input("Ingrese nuevo Precio: ")

                    nFila = int(input("ingrese fila de registro: "))

                    #etiqueta = int(input("que columna quieres cambiar: "))

                    nFila = list(map(int, str(nFila)))#convierte un string a vector

                    print(type[nFila])#permite examinar el tipo a que corresponde un dato determinado, [vector]

                    Editar_Precio(ruta_archivo, nFila, 3, nPrecio)
                    imprimirRegistro(ruta_archivo)
                    print("Se cambio correctamente el Precio del Servicio:)")

            case "5":
                    limpiarPantalla()
                    imprimirRegistro(ruta_archivo)
                    #----------------------------------------------------------------------------#
                    print("_"*20)

                    codigo = input("Codigo: ") #código que buscara
                    fila = str(BuscarServicios(codigo))# string o cadena de caracteres, es una secuencia inmutable
                    print(f"{fila}")

                    print("_"*20)
                    output = fila.split(";")#output entrega y es la salida del input

                    print("_"*20)
                    print(output)

                    nTiempo = input("Ingrese nuevo Tiempo: ")

                    nFila = int(input("ingrese fila de registro: "))

                    #etiqueta = int(input("que columna quieres cambiar: "))

                    nFila = list(map(int, str(nFila)))#convierte un string a vector

                    print(type[nFila])#permite examinar el tipo a que corresponde un dato determinado, [vector]

                    Editar_Tiempo(ruta_archivo, nFila, 4, nTiempo)
                    imprimirRegistro(ruta_archivo)
                    print("Se cambio correctamente el Timepo del Servicio:)")
            case 6:
                limpiarPantalla()
                time.sleep(1)
                break
            case _:
                limpiarPantalla()
                time.sleep(1)
                break