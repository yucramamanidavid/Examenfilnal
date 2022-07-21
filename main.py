#!/usr/bin/env python
# coding: utf-8
# importaciones de librerias
import getpass
import time

from utils import limpiarPantalla
from clientes import gestionClientes
from productos import gestionServicios
from usuarios import gestionUsuarios
from usuarios import ValidarAcceso

def run():
    while True:
        print("\033[93m"+"="*31 + "\033[93m")
        print("\033[1;91m" + "       SPA CIELO AZUL      " + "\033[1;91m")
        print("\033[93m"+"="*31 + "\033[93m")
        print("\033[0m")
        print("\033[49;96m"+"="*31 + "\033[49;96m")
        print("\033[0m")
        print("\033[49;96m"+"|  MENÚ PRINCIPAL DEL SISTEMA |" + "\033[49;96m")
        print("\033[0m")
        print("\033[49;96m"+"|_____________________________|" + "\033[49;96m")
        print("\033[0m")
        print("| 1. Gestión de Clinetes      |")
        print("| 2. Gestión de Usuario       |")
        print("| 3. Gestión de Servicios     |")
        print("| 4. Gestión de Ventas        |")
        print("| 0. Salir                    |")
        print("\033[49;96m"+"="*31 + "\033[49;96m")
        print("\033[0m")
        op = int(input("Opción: "))

        match (op):
            case 1:
                limpiarPantalla()
                gestionClientes() 

            case 2:
                limpiarPantalla()
                gestionUsuarios()
                

            case 3:
                limpiarPantalla()
                gestionServicios()

            case 4:
                limpiarPantalla()
                print("logica para la opcion 3")

            case 0:
                limpiarPantalla()
                print("Saliendo del sistema... hasta pronto")
                break

            case _:
                print("opción incorrecta")
                time.sleep(2)
                limpiarPantalla()


def main():
    acumulador = 0
    while True and acumulador != 3:

        user = input("Ingrese Usuario: ")
        password = getpass.getpass("Ingrese password: ")

        if ValidarAcceso(user, password):
            limpiarPantalla()
            run()
        else:
            print("Contraseña incorrecta")
            acumulador += 1
            time.sleep(2)
            limpiarPantalla()

            # break


if __name__ == "__main__":
    # la funcion que queremos que se ejecute
    main()
