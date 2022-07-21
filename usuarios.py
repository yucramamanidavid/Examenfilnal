from models import Usuario
from utils import limpiarPantalla

ruta_archivo = "./archivos/usuarios.txt"


def crearUsuario():

    dni = input("DNI: ")
    password = input("Password: ")
    tipo = input("Tipo: ")
    nombres_apellidos = input("Nombres y Apellidos: ")
    direccion = input("Dirección: ")
    telefono = input("Telefono: ")
    email = input("E-mail: ")

    usuario = Usuario(
        dni, password, tipo, nombres_apellidos, direccion, telefono, email
    )

    archivoUsuario = open(ruta_archivo, "a")
    archivoUsuario.write(str(usuario))
    archivoUsuario.close


def buscarUsuario(dni):
    archivoUsuarios = open(ruta_archivo, "r")
    for linea in archivoUsuarios.readlines():
        fila = linea.split(";")
        # print(atributo)
        if fila[0] == dni:
            print("Usuario encontrado")
            print(fila[0])
            return True
    return False


def ValidarAcceso(dni, password):
    archivoUsuarios = open(ruta_archivo, "r")
    for linea in archivoUsuarios.readlines():
        fila = linea.split(";")
    if fila[0] == dni and fila[1] == password and fila[2] == "ADMIN":
            return True
    return False

def gestionUsuarios():
    while True:
        print("Sub Menu: GESTION DE USUARIOS")
        print("1. Ingresar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario por DNI")
        print("4. regresar al menu principal")
        op = input("Ingrese una opcion: ")

        match (op):
            case "1":
                limpiarPantalla()
                crearUsuario()
            case "2":
                limpiarPantalla()
                archivoUsuarios = open(ruta_archivo, "r")
                print("DNI\tNombres_Apellidos\t\tDireccion\t\t\tTelefono\tGemail")
                for linea in archivoUsuarios.readlines():
                    atributos = linea.split(";")
                    print(
                        "{}\t{}\t\t{}\t\t\t{}\t{}".format(
                            atributos[0], atributos[1], atributos[2], atributos[3], atributos[4]
                        )
                    )     
                archivoUsuarios.close()
                break               
                print("aqui se mostraran los clientes")
            case "3":
                limpiarPantalla()
                print("buscar por DNI")
                dni = input("Ingrese DNI: ")
                if buscarUsuario(dni):
                    print(dni)
                    print("Existe")
                else:
                    print("No existe")

            case "4":
                break
            case _:
                print("opcion no disponible")
