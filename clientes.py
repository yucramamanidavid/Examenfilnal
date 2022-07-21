from models import Cliente
from utils import limpiarPantalla

ruta_archivo = "./archivos/clientes.txt"


def crearCliente():

    dni = input("DNI: ")
    nombres_apellidos = input("Nombres y Apellidos: ")
    direccion = input("Dirección: ")
    telefono = input("Telefono: ")
    email = input("E-mail: ")

    cliente = Cliente(dni, nombres_apellidos, direccion, telefono, email)

    archivoCliente = open(ruta_archivo, "a")
    archivoCliente.write(str(cliente))
    archivoCliente.close

def buscarCliente(dni):
    vector = []
    archivoCliente = open(ruta_archivo, "r")
    for linea in archivoCliente.readlines():
        fila = linea.split(";")
        # print(atributo)
        if fila[0] == dni:
            return True
    return False


def gestionClientes():
    while True:
        print("============================")
        print("Sub Menu: GESTION DE CLIENTES")
        print("1. Ingresar Cliente")
        print("2. Buscar Cliente")
        print("3. Mostrar clientes")
        print("4. regresar al menu principal")
        op = input("Ingrese una opcion: ")

        match (op):
            case "1":
                limpiarPantalla()
                crearCliente()
            case "2":
                limpiarPantalla()
                buscarCliente()
                print("aqui se mostraran los clientes")
            case "3":
                limpiarPantalla()
                archivoCliente = open(ruta_archivo, "r")
                print("DNI\tNombres_Apellidos\t\tDireccion\t\t\tTelefono\tGemail")
                for linea in archivoCliente.readlines():
                    atributos = linea.split(";")
                    print("-"*100)
                    print(
                        "{}\t{}\t\t{}\t\t\t{}\t{}".format(
                            atributos[0], atributos[1], atributos[2], atributos[3], atributos[4]
                        )
                    ) 
                    print("-"*100)    
                archivoCliente.close()
                break
            case "4":
                limpiarPantalla()
                break            
            case _:
                limpiarPantalla()
                print("opcion no disponible")
