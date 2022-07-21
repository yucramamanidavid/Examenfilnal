
class Servicio:
    # atributos
    def __init__(
        self, codigo, servicio, detalle, precio, hora
    ):#__int__(constructor)
        self.codigo = codigo
        self.servicio = servicio
        self.detalle = detalle
        self.precio = precio
        self.hora = hora

#Self: nos ayuda a acceder a los atributos
#------------------------------------------------------------------#
    # metodos
    def __str__(self):
        return "{};{};{};{};{}\n".format(
            self.codigo,
            self.servicio,
            self.detalle,
            self.precio,
            self.hora,
    
        )#Gracias a este metodo se puede imprimir.

class Cliente:
    # atributos
    def __init__(self, dni, nombres_apellidos, direccion, telefono, email):
        self.dni = dni
        self.nombres_apellidos = nombres_apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    # metodos
    def __str__(self):
        return "{};{};{};{};{}\n".format(
            self.dni, self.nombres_apellidos, self.direccion, self.telefono, self.email
        )



class Usuario:
    # atributos
    def __init__(
        self, dni, password, tipo, nombres_apellidos, direccion, telefono, email
    ):
        self.dni = dni
        self.password = password
        self.tipo = tipo
        self.nombres_apellidos = nombres_apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    # metodos
    def __str__(self):
        return "{};{};{};{};{};{};{}\n".format(
            self.dni,
            self.password,
            self.tipo,
            self.nombres_apellidos,
            self.direccion,
            self.telefono,
            self.email,
        )

