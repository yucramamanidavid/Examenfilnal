import time
from utils import limpiarPantalla
from models import Servicio
from EditarServicio import editarservicios


ruta_archivo = "./archivos/servicios.txt"


def crearservicio():

    codigo = input("Codigo: ")
    servicio = input("Servicio: ")
    detalle = input("Detalle: ")
    precio = input("Precio: ")
    hora = input("Tiempo: ")

    servicios = Servicio(codigo, servicio, detalle, precio, hora)

    archivoServicios = open(ruta_archivo, "a")#Guardar los servicios
    archivoServicios.write(str(servicios))
    archivoServicios.close

#
def BuscarServicio(codigo):
    servicios = None#(denota falta de valor)
    archivoServicios = open(ruta_archivo, "r")
    for linea in archivoServicios.readlines():
        atributos = linea.split(";")
        if codigo == atributos[0]:
            servicios = Servicio(atributos[0], atributos[1], atributos[2], atributos[3], atributos[4])
            break
    archivoServicios.close()

    return servicios


def gestionServicios():
    limpiarPantalla()
    while True:
        print("\033[49;32m"+"="*33 + "\033[49;32m")
        print("\033[0m")
        print("\033[49;96m"+"SUBMENU: GESTION DE LOS SERVICIOS "+ "\033[49;96m")
        print("\033[49;32m"+"="*33 + "\033[49;32m")
        print("\033[0m")
        print("| 1. Ingresar el Servicio       |")
        print("| 2. Mostrar los Servicios      |")
        print("| 3. Busca Servicios            |")
        print("| 4. Editar los Servicios       |")
        print("| 5. eleminar servicio")
        print("| 6. Regresar al menu principal |")
        print("\033[49;96m"+"="*33 + "\033[49;96m")
        print("\033[0m")
        op = int(input("Opción: "))

        match (op):
            case 1:
                limpiarPantalla()
                crearservicio()
                print("Creado Correctamente!!!")
            case 2:
                limpiarPantalla()
                archivoServicios = open(ruta_archivo, "r")
                print("Código\t\tServicio\t\tDetalle\t\t\t\t\tPrecio\t\t\tTiempo")
                for linea in archivoServicios.readlines():
                    atributos = linea.split(";")
                    print("\033[49;96m"+"="*120 + "\033[49;96m")
                    print("\033[0m")
                    print(
                        "{}\t\t{}\t\t{}\t\t{}\t\t{}".format(
                            atributos[0], atributos[1], atributos[2], atributos[3], atributos[4]
                        )
                    )
                    print("\033[0m")
                    print("\033[49;96m"+"="*120 + "\033[49;96m")     
                archivoServicios.close() 
            case 3:
                limpiarPantalla()
                print("buscar por codigo")
                codigo = input("Ingrese codigo: ")
                if BuscarServicio(codigo):
                    print("Existe")
                    print(BuscarServicio(codigo))
                else:
                    print("No existe")               

            

            case 4:
                limpiarPantalla()
                editarservicios()
 
            case 5:
                limpiarPantalla()
                """""
                nombre_articulo = input("nombre del servicio a eliminar: ")
                if nombre del servicio in nombres:
                    indice = nombres.index(nombre_servicio)
                    del nombres[indice]
                    del precios[indice]
                    del cantidades_vendidas[indice]
                    print(f"Se elimina {nombre_servicio}")
                else:
                    print("El nombre no existe")
            
                print("Gracias por usar el submenu")
                time.sleep(2)
                break
            """""
            case 6:
                    limpiarPantalla()
                    time.sleep(1)
                    break
            case _:
                print("opción incorrecta")
                time.sleep(2)
                limpiarPantalla()
